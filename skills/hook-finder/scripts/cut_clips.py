#!/usr/bin/env python3
"""Cut vertical 9:16 short-form clips from a landscape gameplay recording.

Usage:
  python3 cut_clips.py INPUT --clip START DURATION NAME [--clip ...] [--out DIR] [--no-crop]

START accepts seconds (72) or HH:MM:SS (00:01:12). DURATION is in seconds.
By default the centre of the frame is cropped to 9:16. With --no-crop the full
frame is scaled down and padded (letterbox) to 1080x1920.
Requires ffmpeg on PATH.
"""
import argparse
import pathlib
import re
import shutil
import subprocess
import sys

CROP = "crop=ih*9/16:ih,scale=1080:1920"
PAD = "scale=1080:-2,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black"


def safe_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", name).strip("-") or "clip"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="landscape recording (mp4, mov, mkv...)")
    parser.add_argument("--clip", nargs=3, action="append", metavar=("START", "DURATION", "NAME"), required=True)
    parser.add_argument("--out", default="clips", help="output folder (default: clips)")
    parser.add_argument("--no-crop", action="store_true", help="letterbox instead of centre crop")
    args = parser.parse_args()

    if shutil.which("ffmpeg") is None:
        print("ffmpeg not found. Install it first (https://ffmpeg.org/download.html).", file=sys.stderr)
        return 1
    src = pathlib.Path(args.input)
    if not src.is_file():
        print(f"Input not found: {src}", file=sys.stderr)
        return 1

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    vf = PAD if args.no_crop else CROP

    failures = 0
    for start, duration, name in args.clip:
        try:
            if float(duration) <= 0:
                raise ValueError
        except ValueError:
            print(f"Skipping {name}: duration must be a positive number of seconds", file=sys.stderr)
            failures += 1
            continue
        dest = out_dir / f"{safe_name(name)}.mp4"
        cmd = [
            "ffmpeg", "-y", "-loglevel", "error",
            "-ss", start, "-i", str(src), "-t", duration,
            "-vf", vf,
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
            "-c:a", "aac", "-b:a", "160k",
            "-movflags", "+faststart",
            str(dest),
        ]
        result = subprocess.run(cmd)
        if result.returncode == 0:
            print(f"✓ {dest}")
        else:
            print(f"✗ {name} failed (ffmpeg exit {result.returncode})", file=sys.stderr)
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
