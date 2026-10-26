# xiaowang-gongzuo-biji

🌐 中文版: [README.md](README.md)

> AI Data Analysis Case Studies (Power & Renewables, Coal, Shipping, Finance, Real Estate) + AI Getting-Started, AI-Assisted Exam-Paper Authoring & Mock Papers, AI Programming Tutorials, AIGC Content Creation, and AI Automation Task Engineering (self-media publishing automation, Marvis dev-environment setup).
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
│   ├── 房产数据 (Real-Estate Data)
│   └── 理财分析 (Personal Finance)
├── ai-getting-started/        # AI getting-started materials
│   ├── 01_教程文档/           # How to do data analysis / AI getting-started
│   │   ├── 如何用AI做数据分析.md         (How to do data analysis with AI)
│   │   ├── AI写小说思路文字稿.md         (How to write novels with AI)
│   │   ├── ChatGPT安装过程记录.md        (ChatGPT install notes)
│   │   └── 概率校准与期望校准误差（ECE）.md (Probability calibration & ECE)
│   └── 02_出题与试卷/          # AI-assisted exam-paper authoring
│       ├── 01_出题思路/        (CET-4 / calculus paper-authoring specs)
│       └── 02_模拟试卷/        (Mock paper A / limit-topic sample paper)
├── ai-programming-tutorials/  # Full AI programming tutorial series (01~08)
│   └── Lessons 01~08 (Markdown prompting / AI workflows / SQL / frontend / backend / testing & review / vector DB / ima customer service)
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
| 房产数据 | Bayuquan second-hand housing transaction analysis (wps source / xlsx report / interactive dashboard / workflow report) |
| 理财分析 | Personal finance analysis workflow |

### ai-getting-started

- `01_教程文档/`: AI getting-started & data-analysis tutorial docs, including:
  - `如何用AI做数据分析.md`: How to do data analysis with AI (step-by-step)
  - `AI写小说思路文字稿.md`: Methodology notes for writing novels with AI
  - `ChatGPT安装过程记录.md`: Notes on local ChatGPT-class tool installation
  - `概率校准与期望校准误差（ECE）.md`: Model probability calibration & Expected Calibration Error (ECE)
- `02_出题与试卷/`: AI-assisted exam-paper authoring (methodology + mock papers). See the folder's own `README.md`:
  - `01_出题思路/`: `大学英语四级出题思路 v1.2.md` (CET-4 structure spec + external difficulty anchoring), `高等数学出题思路 v0.3.5.md` (final exam / Liaoning top-up degree / postgraduate exam + six-step verification)
  - `02_模拟试卷/`: `试卷-模拟卷A.md` (CET-4 mock paper A), `样例01-极限五题-考研.md` (sample paper validating the verification pipeline)

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
| 07 | Vector database principles & practice |
| 08 | Building an AI customer-service system on ima |

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

### 2026-10-26

- **File organization**: the 4 loose exam-authoring docs at the root of `ai-getting-started/` were consolidated into a dedicated sub-module `02_出题与试卷/`:
  - `01_出题思路/`: `大学英语四级出题思路 v1.2.md`, `高等数学出题思路 v0.3.5.md`
  - `02_模拟试卷/`: `试卷-模拟卷A.md`, `样例01-极限五题-考研.md`
  - Added a folder `README.md` documenting scope (home-made practice specs, not official), file list, and naming conventions
- `ai-data-analysis/如何用AI分析上网侧电价/` sub-directory numbering aligned with the rest of the repo:
  - `_元信息/` → `01_元信息/`
  - `②分析处理/` → `02_分析处理/`
  - Relative path references updated in `01_元信息/工作流映射.md` and `02_分析处理/辽宁省上网侧电价2026年7月分析报告.md`
- Repo tree synced: `ai-getting-started/` now shows both sub-directories; removed the non-existent `如何用AI做数据分析_海报_3x4.png` entry
- `index.html` landing page fixed and extended:
  - Fixed 11 broken links (`汽车视频/` → `汽车运镜视频/`; `AI写小说思路文字稿.md` moved into `01_教程文档/`)
  - Added an "AI-Assisted Exam-Paper Authoring" section (4 specs and mock papers)
  - Added two previously missing analysis entries: feed-in tariff report and the real-estate interactive dashboard

### 2026-10-09

- `ai-programming-tutorials/` courseware completed to **01~08**: former "supplementary" `向量数据库.html` promoted to official Lesson **07** with standardized naming; full set complete
- `ai-getting-started/01_教程文档/` added `概率校准与期望校准误差（ECE）.md`; `AI写小说思路文字稿.md` and `ChatGPT安装过程记录.md` moved here for unified management
- `ai-data-analysis/` added **房产数据 (Real-Estate Data)** case: `房产数据/` ships Bayuquan second-hand housing xlsx report, interactive dashboard (html), workflow report, plus `.wps` source data and a module README

### 2026-09-25

- `ai-getting-started/` added `ChatGPT安装过程记录.md` (local install notes)

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
