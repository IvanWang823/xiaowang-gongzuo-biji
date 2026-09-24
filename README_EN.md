# xiaowang-gongzuo-biji

🌐 中文版: [README.md](README.md)

> AI Data Analysis Case Studies (Power & Renewables, Coal, Shipping, Finance) + AI Getting-Started, AI Programming Tutorials, AIGC Content Creation, and AI Automation Task Engineering (self-media publishing automation, Marvis dev-environment setup).
> Author: Douyin (TikTok CN) channel "小王工作笔记" (ID: 163277992)

## Project Overview

This repository collects **practical thinking and methodology** for AI-assisted data analysis and programming. Raw business data and final output charts are excluded, so the workflows are easy to learn from and reuse.

## Repository Structure

```
xiaowang-gongzuo-biji/
├── README.md / README_EN.md
├── index.html               # GitHub Pages landing page
├── assets/                     # Shared static assets
│   └── donate/                # Donation QR codes
│       ├── alipay.jpg         # Alipay
│       └── IMG_1534.JPG       # WeChat
├── ai-data-analysis/          # Data analysis case studies (methods)
│   ├── 光伏风电出力预测 (Wind & Solar Output Forecast)
│   ├── 如何用AI分析上网侧电价 (Feed-in Tariff Analysis)
│   ├── 弃风弃光率 (Curtailment Rate)
│   ├── 海运价格分析 (Shipping Price)
│   ├── 煤炭价格分析 (Coal Price)
│   └── 理财分析 (Personal Finance)
├── ai-getting-started/        # AI getting-started materials
│   ├── 01_教程文档/           # How to do data analysis with AI
│   └── AI写小说思路文字稿.md   (How to write novels with AI)
├── ai-programming-tutorials/  # Full AI programming tutorial series
│   └── Lessons 01~06 (Markdown prompting / AI workflows / SQL / frontend / backend / testing & review)
├── aigc-getting-started/      # AIGC content creation materials
│   ├── 汽车运镜视频/          # Car short-video storyboard kit
│   │   ├── 汽车视频制作总表.xlsx  (Master storyboard sheet)
│   │   └── 分镜图/               (9 storyboard reference images)
│   ├── 首尾帧练习/            # First/last frame generation practice
│   │   ├── 提示词.txt            (Prompt samples)
│   │   └── 首尾帧素材/           (first.png / last.jpg)
│   ├── 换装特效/              # AI outfit / try-on effects practice
│   │   ├── 图片/                (5 outfit reference images)
│   │   └── 文档/                (Storyboard & prompt table.xlsx)
│   └── AI视频制作全流程标准化/  # Standardized AI video production guide
│       └── AI视频制作全流程标准化-内容整理.md
└── ai-automated-tasks/        # AI automation task engineering (publishing + Marvis setup)
```

## Contents

### ai-data-analysis

| Case | Content |
| --- | --- |
| 光伏风电出力预测 | Analysis approach for wind & solar output forecast |
| 如何用AI分析上网侧电价 | Feed-in tariff (generation side) data analysis |
| 弃风弃光率 | Curtailment rate analysis workflow |
| 海运价格分析 | Shipping price analysis approach |
| 煤炭价格分析 | Coal price analysis framework & handbook |
| 理财分析 | Personal finance analysis workflow |

### ai-getting-started

- `01_教程文档/`: How to do data analysis with AI (tutorial docs)
- `AI写小说思路文字稿.md`: Methodology notes for writing novels with AI

### ai-programming-tutorials

AI-assisted programming courseware series. See the module's own README for details:

| Lesson | Topic |
| --- | --- |
| 01 | Why feed AI with Markdown prompts (and how) |
| 02 | Building your own AI workflow |
| 03 | Auto-generating SQL scripts with AI |
| 04 | AI frontend web project in practice |
| 05 | AI-assisted backend code development |
| 06 | Code testing & compliance review |

### aigc-getting-started

- **`汽车运镜视频/`**: Full car short-video creation kit
  - `汽车视频制作总表.xlsx`: Master storyboard sheet (shot no., description, reference image, AI-generated video, prompt, duration, status) for fast shot planning and reusable prompts.
  - `分镜图/`: 9 reference images — car body, rear, logo, front/rear wheel, left/right headlight, steering wheel, interior.
- **`首尾帧练习/`**: First/last frame generation practice pack
  - `提示词.txt`: Prompt templates for practice
  - `首尾帧素材/`: Sample images `首帧.png`, `尾帧.jpg` for first/last-frame exercises
- **`AI视频制作全流程标准化/`**: Standardized AI video production materials — integrates 8 source docs (docx/pptx/txt) covering AI image/video principles, folder conventions, numbering rules, Excel master-sheet design (character/shot/dialogue tables), multi-person collaboration, FAQ, and recommended tool list. See `AI视频制作全流程标准化-内容整理.md`.
- **`换装特效/`**: AI outfit / try-on effects practice pack
  - `图片/`: 5 outfit reference images (`01-街景背景.png` + 02~05, four outfits: striped shirt & khaki pants, black knit & white dress, grey knit knot dress, sleeveless plaid skirt)
  - `文档/`: `分镜提示词表.xlsx` storyboard & prompt practice table

### ai-automated-tasks

AI-assisted self-media operations and dev-environment automation: flow docs and final engineering deliverables:

| Doc | Content |
| --- | --- |
| Marvis 安装教程（MySQL + Python + Java） | Prompt set + 3-step method (install / config / verify) for Marvis dev-environment setup; Windows / macOS / Linux |
| 小红书 AI 图文发布流程 v4.2（工程交付终版） | Xiaohongshu image-text auto-publishing flow; publish button stays manual; includes assets / changelog / publish-record schema, state machine, and exception recovery |
| 抖音图文发布自动化计划 v1.2（工程交付定稿版） | Douyin image-text auto-publish plan; three red lines + upload decision tree; AI drafts handed to human for the final click |

## Support the Author

If this repository helps you, you're welcome to buy me a coffee ☕ Donations are entirely voluntary and never affect free access to any content.

<div align="center">
<table cellpadding="12">
  <tr>
    <td align="center">
      <img src="assets/donate/alipay.jpg" alt="Alipay donation QR" width="240"><br>
      <b>Alipay</b>
    </td>
    <td align="center">
      <img src="assets/donate/IMG_1534.JPG" alt="WeChat donation QR" width="240"><br>
      <b>WeChat</b>
    </td>
  </tr>
</table>
</div>

---

## Notes

1. `ai-data-analysis/` and `ai-getting-started/` keep only methods / workflows / thinking; **no raw business data or final charts**.
2. `ai-programming-tutorials/` is the AI programming column, hosting the full courseware set: Markdown prompting, AI workflows, SQL scripts, frontend/backend dev, code testing & review.
3. `aigc-getting-started/` holds AIGC practice materials — car storyboard sheets, reference images, standardized AI video production docs — ready to reuse.
4. Repo name `xiaowang-gongzuo-biji` matches the author's Douyin channel "小王工作笔记".

## Changelog

> Reverse-chronological change log for traceability.

### 2026-09-24

- `aigc-getting-started/` added **换装特效 (outfit / try-on effects)** practice kit: `图片/` (5 outfit reference images) + `文档/分镜提示词表.xlsx`
- New top-level module `ai-automated-tasks/`: AI automation task engineering docs
  - `Marvis 安装教程（MySQL + Python + Java）.md`: Marvis prompt set for setting up a dev environment for beginners (install / config / verify, cross Windows / macOS / Linux)
  - `小红书 AI 图文发布流程 v4.2（工程交付终版）.md`: Xiaohongshu image-text auto-publishing flow (publish button stays manual)
  - `抖音图文发布自动化计划 v1.2（工程交付定稿版）.md`: Douyin image-text auto-publish plan (three red lines + upload decision tree)

### 2026-09-22

- Renamed folders under `aigc-getting-started/`: 「汽车视频」→ **汽车运镜视频**; 「首尾帧」→ **首尾帧练习**, moving `提示词.txt` inside for unified management
- Added first/last frame practice materials: `首尾帧素材/` (sample images `首帧.png`, `尾帧.jpg`) + `提示词.txt`
- Added **AI视频制作全流程标准化** materials: 8 source docs merged into `AI视频制作全流程标准化-内容整理.md`
- `ai-programming-tutorials/` added `如何基于ima创建AI智能客服系统.html`
- Added "Support the Author" section + Alipay QR `assets/donate/alipay.jpg`
- `ai-programming-tutorials/` added `向量数据库.html`

### 2026-09-21

- New top-level module `ai-programming-tutorials/`, on par with the data-analysis module; lessons 01–06 courseware:
  - 01 Why use Markdown to feed AI
  - 02 Why build an AI workflow
  - 03 AI-generated SQL scripts
  - 04 AI frontend web development
  - 05 AI-generated backend code
  - 06 Testing & review
