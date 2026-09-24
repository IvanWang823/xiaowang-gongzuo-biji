# xiaowang-gongzuo-biji

> 📖 本说明同时提供 **[中文](#项目简介)** 与 **[English](#english-version)** 两个版本，内容一致，可按需阅读。
> AI 数据分析实战案例集，覆盖电力新能源、煤炭、海运、理财多个领域；同时包含 AI 入门指南、AI 编程实操教程、AIGC 内容创作实战案例，以及 AI 自动化任务工程交付（自媒体发布流程自动化、Marvis 开发环境安装）。
> 作者：抖音「小王工作笔记」（ID：163277992）

## 项目简介

本仓库沉淀 **AI 辅助数据分析与程序开发的实践思路、工作方法**，项目内不包含原始业务数据以及最终生成的可视化图表，方便大家学习借鉴、二次复用。

## 目录结构

```
xiaowang-gongzuo-biji/
├── README.md                # 本文件（中文 + English 双语）
├── index.html               # GitHub Pages 落地页
├── assets/                 # 公共静态资源
│   └── donate/                 # 打赏二维码
│       ├── alipay.jpg          # 支付宝
│       └── IMG_1534.JPG        # 微信
├── ai-data-analysis/       # 数据分析实战案例（分析思路 & 方法论）
│   ├── 光伏风电出力预测
│   ├── 如何用 AI 分析上网侧电价
│   ├── 弃风弃光率
│   ├── 海运价格分析
│   ├── 煤炭价格分析
│   └── 理财分析
├── ai-getting-started/     # AI 应用入门学习资料
│   ├── 01_教程文档/            # AI 赋能数据分析实操指南
│   └── AI写小说思路文字稿.md
├── ai-programming-tutorials/  # AI 辅助编程全套教程
│   └── 01~06 课件（Markdown 向 AI 输入提示、AI 工作流、SQL、前端、后端、测试审查）
├── aigc-getting-started/   # AIGC 内容创作实战素材
│   ├── 汽车运镜视频/          # 汽车短视频分镜方案与配套素材
│   │   ├── 汽车视频制作总表.xlsx  # 分镜总表（镜头编号 / 分镜参考图 / AI 提示词 / 镜头时长 / 执行状态）
│   │   └── 分镜图/               # 9 张汽车主题分镜参考素材图
│   ├── 首尾帧练习/            # 视频首尾帧生成练习资料
│   │   ├── 提示词.txt            # 首尾帧生成提示词参考
│   │   └── 首尾帧素材/           # 首帧.png / 尾帧.jpg
│   ├── 换装特效/              # AI 换装 / 穿搭特效练习素材
│   │   ├── 图片/                # 5 张穿搭参考图（街景背景 + 4 套穿搭）
│   │   └── 文档/                # 分镜提示词表.xlsx（练习用表格）
│   └── AI视频制作全流程标准化/  # AI 视频项目制作规范与协作指南
│       └── AI视频制作全流程标准化-内容整理.md  # 8 份源文档整合：原理 / 文件夹规范 / 编号规则 / Excel 总表 / 协作 / FAQ / 工具清单
└── ai-automated-tasks/     # AI 自动化任务工程交付（自媒体发布流程 + Marvis 环境安装）
```

## 内容说明

### ai-data-analysis ｜ 数据分析案例库

| 案例名称           | 内容简介              |
| -------------- | ----------------- |
| 光伏风电出力预测       | 风光发电出力预测完整分析思路    |
| 如何用 AI 分析上网侧电价 | 发电侧上网电价数据分析方法论    |
| 弃风弃光率          | 弃风弃光率指标分析完整流程     |
| 海运价格分析         | 海运市场价格分析思路框架      |
| 煤炭价格分析         | 煤炭价格分析框架与实操手册     |
| 理财分析           | AI 辅助理财分析标准化工作流文档 |

### ai-getting-started ｜ AI 入门资料

- `01_教程文档/`：手把手讲解如何借助 AI 开展数据分析工作
- `AI写小说思路文字稿.md`：利用 AI 进行小说创作的方法论文档

### ai-programming-tutorials ｜ AI 编程教程

AI 辅助编程系列课程课件，详细内容可查阅模块内部 README 文档：

| 课时  | 课程主题                        |
| --- | --------------------------- |
| 01  | 使用 Markdown 给 AI 输入提示的优势与实践 |
| 02  | 搭建专属 AI 工作流的意义与方法           |
| 03  | 使用 AI 自动生成 SQL 脚本           |
| 04  | AI 生成前端网页项目实战               |
| 05  | AI 辅助后端代码开发                 |
| 06  | 代码的测试与合规审查                  |

### aigc-getting-started ｜ AIGC 创作实战

- **`汽车运镜视频/`**：汽车类短视频全套创作素材
  - `汽车视频制作总表.xlsx`：分镜规划总表（Sheet「分镜表」），涵盖镜头编号、内容描述、分镜参考图、AI 生成视频、提示词、时长、状态等字段，用于快速规划汽车短视频镜头，沉淀可复用 AI 提示词。
  - `分镜图/`：共 9 张参考图，包含车身、车尾、汽车 logo、前轮毂、后轮毂、左大灯、右大灯、方向盘、内饰素材。
- **`首尾帧练习/`**：AI 视频首尾帧生成练习素材包
  - `提示词.txt`：练习可用的提示词范本
  - `首尾帧素材/`：样例图片 `首帧.png`、`尾帧.jpg`，用来练习 AI 视频首尾帧生成。
- **`AI视频制作全流程标准化/`**：AI 视频项目制作标准化资料集，整合自「AI视频制作全流程标准化」文件夹下 8 份文档（docx / pptx / txt），涵盖 AI 生图与视频原理、项目文件夹规范、角色库 / 分镜库编号规则、Excel 总表设计（角色表 / 分镜表 / 台词表字段明细）、多人协作流程与版本管理、常见问题速查与推荐工具清单。详见 `AI视频制作全流程标准化-内容整理.md`。
- **`换装特效/`**：AI 换装 / 穿搭特效练习素材包
  - `图片/`：5 张穿搭参考图，含 `01-街景背景.png` 及 `02~05` 四套穿搭（条纹衬衫卡其裤、黑色针织白裙、灰色针织扭结裙、无袖格纹半裙）
  - `文档/`：`分镜提示词表.xlsx`：换装镜头分镜与提示词练习表

### ai-automated-tasks ｜ AI 自动化任务工程交付

AI 辅助自媒体运营与开发环境搭建的自动化方案、流程文档与工程交付终版：

| 文档                                 | 内容简介                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------- |
| Marvis 安装教程（MySQL + Python + Java） | 用 Marvis（马维斯）帮小白安装开发环境的提示词与三步法（安装 / 配置 / 检查），覆盖 Windows / macOS / Linux |
| 小红书 AI 图文发布流程 v4.2（工程交付终版）         | 小红书图文自动发布流程，发布按钮永留人工；含素材 / 变更日志 / 发布记录 Schema、状态机与异常恢复                  |
| 抖音图文发布自动化计划 v1.2（工程交付定稿版）          | 抖音图文自动发布计划，三条红线 + 上传决策树；AI 到草稿后移交人工点击发布                                 |

## 打赏支持

如果本仓库对你有所帮助，欢迎请作者喝一杯咖啡 ☕。打赏完全自愿，不会影响仓库全部内容的免费阅读与使用。

<div align="center">
<table cellpadding="12">
  <tr>
    <td align="center">
      <img src="assets/donate/alipay.jpg" alt="支付宝打赏码" width="240"><br>
      <b>支付宝</b>
    </td>
    <td align="center">
      <img src="assets/donate/IMG_1534.JPG" alt="微信打赏码" width="240"><br>
      <b>微信</b>
    </td>
  </tr>
</table>
</div>

---

## 项目补充说明

1. `ai-data-analysis/` 和 `ai-getting-started/` 仅留存思路、流程、方法论，**不包含原始业务数据与最终输出图表**。
2. `ai-programming-tutorials/` 为 AI 编程专题栏目，收纳全套 AI 编程课件：Markdown 提示输入、AI 工作流、SQL 脚本、前后端开发、代码测试审查。
3. `aigc-getting-started/` 存放 AIGC 实操素材，例如汽车短视频分镜表、参考图片、AI 视频制作全流程标准化文档，可直接拿来复用练习。
4. 仓库名称 `xiaowang-gongzuo-biji`，对应作者抖音账号「小王工作笔记」。

## 更新日志

> 按时间倒序记录版本变更，方便追溯迭代历史

### 2026-09-24

- `aigc-getting-started/` 新增 **换装特效** 练习素材：含 `图片/`（5 张穿搭参考图）与 `文档/分镜提示词表.xlsx`
- 新增一级模块 `ai-automated-tasks/`：收纳 AI 自动化任务工程交付文档
  - `Marvis 安装教程（MySQL + Python + Java）.md`：Marvis 帮小白装开发环境提示词（安装 / 配置 / 检查三步法，跨 Windows / macOS / Linux）
  - `小红书 AI 图文发布流程 v4.2（工程交付终版）.md`：小红书图文自动发布流程（发布按钮永留人工）
  - `抖音图文发布自动化计划 v1.2（工程交付定稿版）.md`：抖音图文自动发布计划（三条红线 + 上传决策树）

### 2026-09-22

- 重构 `aigc-getting-started/` 目录命名：原「汽车视频」重命名为 **汽车运镜视频**；原「首尾帧」重命名为 **首尾帧练习**，将 `提示词.txt` 归入该文件夹内统一管理
- `aigc-getting-started/` 新增首尾帧练习素材：`首尾帧素材/` 目录（样例图片 `首帧.png`、`尾帧.jpg`）+ 提示词文档 `提示词.txt`
- `aigc-getting-started/` 新增 **AI视频制作全流程标准化** 资料集：整合 8 份源文档为 `AI视频制作全流程标准化-内容整理.md`
- `ai-programming-tutorials/` 新增补充文档：`如何基于ima创建AI智能客服系统.html`
- 新增「打赏支持」板块，增加支付宝打赏资源文件 `assets/donate/alipay.jpg`
- `ai-programming-tutorials/` 新增补充文档：`向量数据库.html`

### 2026-09-21

- 新增一级模块 `ai-programming-tutorials/`，与数据分析模块平级；收录 AI 编程第 1–6 课全套课件：
  - 01 为何用 Markdown 喂 AI
  - 02 为何要创建 AI 工作流
  - 03 AI 生成 SQL 脚本
  - 04 AI 生成前端网页实战
  - 05 AI 生成后端代码
  - 06 测试与审查

---

# English Version

> AI Data Analysis Case Studies (Power & Renewables, Coal, Shipping, Finance) + AI Getting-Started, AI Programming Tutorials, AIGC Content Creation, and AI Automation Task Engineering (self-media publishing automation, Marvis dev-environment setup).
> Author: Douyin (TikTok CN) channel "小王工作笔记" (ID: 163277992)

## Project Overview

This repository collects **practical thinking and methodology** for AI-assisted data analysis and programming. Raw business data and final output charts are excluded, so the workflows are easy to learn from and reuse.

## Repository Structure

```
xiaowang-gongzuo-biji/
├── README.md                # This file (Chinese + English)
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
