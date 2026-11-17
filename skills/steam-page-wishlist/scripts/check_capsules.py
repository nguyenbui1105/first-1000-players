#!/usr/bin/env python3
"""Check Steam store/library images in a folder against the required pixel sizes.

Usage:
  python3 check_capsules.py path/to/steam-assets/

Reads PNG and JPEG sizes without extra packages and matches each file to a
Steam asset by exact size. Reports which required assets are missing and which
files have an unknown size (a common cause of rejected uploads).
The library logo is not checked: it is a transparent PNG whose size limits
are described on the Steamworks library assets page.
Sizes last checked 2026-11-14; confirm on partner.steamgames.com/doc/store/assets.
"""
import pathlib
import struct
import sys

ASSETS = {
    (920, 430): ("Header capsule / Library header", True),
    (462, 174): ("Small capsule", True),
    (1232, 706): ("Main capsule", True),
    (748, 896): ("Vertical capsule", True),
    (600, 900): ("Library capsule", True),
    (3840, 1240): ("Library hero", True),
}


def image_size(path: pathlib.Path):
    with path.open("rb") as f:
        head = f.read(26)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", head[16:24])
            return w, h
        if head[:2] == b"\xff\xd8":
            f.seek(2)
            while True:
                marker = f.read(2)
                if len(marker) < 2 or marker[0] != 0xFF:
                    return None
                code = marker[1]
                if code in (0xD8, 0x01) or 0xD0 <= code <= 0xD7:
                    continue
                length = struct.unpack(">H", f.read(2))[0]
                if code in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    f.read(1)
                    h, w = struct.unpack(">HH", f.read(4))
                    return w, h
                f.seek(length - 2, 1)
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    folder = pathlib.Path(sys.argv[1])
    if not folder.is_dir():
        print(f"Not a folder: {folder}")
        return 2

    found = {}
    unknown = []
    for p in sorted(folder.iterdir()):
        if p.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        size = image_size(p)
        if size in ASSETS:
            found.setdefault(size, []).append(p.name)
        else:
            unknown.append((p.name, size))

    print("Matched assets:")
    for size, (label, _) in ASSETS.items():
        if size in found:
            print(f"  ✓ {label:32} {size[0]}x{size[1]}  ← {', '.join(found[size])}")
    missing = [(label, size) for size, (label, required) in ASSETS.items() if required and size not in found]
    if missing:
        print("\nMissing required assets:")
        for label, size in missing:
            print(f"  ✗ {label:32} needs {size[0]}x{size[1]}")
    if unknown:
        print("\nFiles with a size Steam will not accept as a capsule:")
        for name, size in unknown:
            shown = f"{size[0]}x{size[1]}" if size else "unreadable"
            print(f"  ? {name} ({shown})")
    print("\nAlso check by eye: title legible at small size, no text besides the title, genre obvious.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
