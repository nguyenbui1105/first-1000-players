# 🎮 First 1000 Players

[English](README.md) · **Tiếng Việt**

> AI giúp làm game dễ hơn bao giờ hết. Nhưng để có người chơi thì vẫn khó.
> **First 1000 Players** là bộ agent skill giúp các vibecoder làm game bằng AI đưa game từ "chạy được" đến 1.000 người chơi thật đầu tiên — minh bạch, không spam.

Năm 2025 có khoảng 20.000 game ra mắt trên Steam. Chỉ ~3% đạt 1.000 review, và game trung vị chỉ kiếm được vài trăm đô ([số liệu](references/market.md)). Làm game không còn là nút thắt. **Được người chơi nhìn thấy mới là nút thắt.**

Đã có bộ skill marketing cho SaaS, đã có bộ skill để code game. Bộ này lo đúng khâu ở giữa: **phân phối cho game nhỏ làm bằng AI** — web portal, itch.io, Steam, video ngắn, cộng đồng, và câu hỏi "có nên khai dùng AI không" mà vibecoder nào cũng gặp.

## Các skill

| Skill | Dùng khi bạn muốn… |
|---|---|
| [`game-context`](skills/game-context/SKILL.md) | mô tả game một lần, để mọi skill khác biết thể loại, người chơi mục tiêu, nền tảng và việc dùng AI |
| [`platform-picker`](skills/platform-picker/SKILL.md) | chọn nơi phát hành trước (CrazyGames, Poki, itch.io, Steam…) và bước tiếp theo |
| [`hook-finder`](skills/hook-finder/SKILL.md) | tìm khoảnh khắc khiến người lạ dừng lướt, rồi biến thành clip TikTok/Shorts |
| [`community-launcher`](skills/community-launcher/SKILL.md) | giới thiệu game trên Reddit, Discord, nhóm Việt Nam mà không vi phạm luật (chỉ soạn nháp) |
| [`ai-disclosure`](skills/ai-disclosure/SKILL.md) | viết phần khai báo AI trung thực cho Steam, itch.io, Reddit và giảm phản ứng tiêu cực |

Sắp có: `steam-page-wishlist`, `web-portal-publisher`, `feedback-analytics`, `launch-checklist`, `devlog-buildinpublic`, `creator-outreach`, `sea-vietnam-playbook`.

## Cài đặt

Thay `your-username` bằng tài khoản GitHub chứa repo này.

**Claude Code (plugin)**
```
/plugin marketplace add your-username/first-1000-players
/plugin install first-1000-players@first-1000-players
```

**Agent hỗ trợ chuẩn mở [Agent Skills](https://agentskills.io)**
```bash
npx skills add your-username/first-1000-players
```

**Thủ công** — chép các thư mục trong `skills/` vào:
- Claude Code: `.claude/skills/` (theo project) hoặc `~/.claude/skills/` (dùng chung)
- Codex: `.agents/skills/`
- Cursor: `.cursor/skills/`

## Bắt đầu nhanh

Mở project game cùng agent của bạn và gõ:

```
Giúp tôi tìm những người chơi đầu tiên cho game.
```

Agent sẽ chạy `game-context`, tạo file `.agents/game-context.md`, rồi gợi ý `platform-picker` và `hook-finder`. Skill trả lời bằng tiếng Việt nếu bạn viết tiếng Việt.

## Nguyên tắc

1. **Soạn nháp, không làm bot.** Skill không bao giờ tự đăng bài, bình luận hay nhắn tin thay bạn. Bạn là người đăng.
2. **Minh bạch về AI.** Không skill nào giúp che giấu việc dùng AI. Bị phát hiện còn tệ hơn tự khai.
3. **Số liệu có ngày.** Mọi con số đều có nguồn và ngày kiểm tra (`last_checked`). Nền tảng thay đổi liên tục, nên skill luôn nhắc bạn kiểm tra lại.
4. **Không hứa viral.** Câu chuyện viral là của số ít người sống sót. Skill đặt mục tiêu thực tế và đo lường.
5. **Ngôn ngữ của bạn.** Skill trả lời theo ngôn ngữ bạn dùng. Tài liệu có tiếng Anh và tiếng Việt, hoan nghênh thêm ngôn ngữ khác.

## Case study

Mọi skill được thử trước trên một game thật: game trồng tiêu góc nhìn thứ nhất lấy bối cảnh Đắk Lắk. Theo dõi nhật ký công khai tại [`case-studies/pepper-farm-daklak`](case-studies/pepper-farm-daklak/README.md), kể cả số liệu xấu.

## Cấu trúc repo

```
skills/          mỗi skill một thư mục (SKILL.md + references/ + scripts/)
references/      số liệu thị trường dùng chung, có nguồn
evals/           ít nhất 3 câu test cho mỗi skill
scripts/         validate_skills.py
case-studies/    nhật ký phân phối thật
```

## Đóng góp

Cập nhật luật của một cộng đồng? Có case study của game bạn? Xem [CONTRIBUTING.md](CONTRIBUTING.md). Chạy `python3 scripts/validate_skills.py` trước khi mở PR.

## Giấy phép

MIT
