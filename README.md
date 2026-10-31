# Qikou (气口)

[中文](#中文) | [English](#english)

---

## 中文

Qikou（气口）是一个基于**物理多模态发声（TTS）**与**自然呼吸节奏**的去 AI 味双 Agent 工作流。

通过本地语音合成将平面文字转化为时间流音频，借助多模态大模型的听觉感知理解真实语流停顿与呼吸节拍，消除纯文本自回归生成中的八股句式与机械套路。

### 核心机制

```
[子 Agent 1: 提取事实清单]
       │
       ▼
[物理层 TTS: 本地 SAPI 生成真实 .wav 音频]
       │
       ▼
[子 Agent 2: 盲听重述]
 (★ 物理隔离：仅接收音频文件与事实清单，不看原文文本)
       │
       ▼
    交付成果
```

1. **事实提取 (Agent 1)**：依据 ASD-STE100 规范提取原子化硬核事实清单，剥离主观修辞、文学比喻与套路过渡词，严禁近义词随意轮换。
2. **物理发声 (TTS)**：通过本地系统接口（Windows SAPI）将输入文本合成为真实 16-bit PCM WAV 音频文件。
3. **盲听隔离重构 (Agent 2)**：子 Agent 2 处于严格物理隔离环境，不接触原文文本。其输入仅为真实音频与事实清单，依据人类自然口语节奏重构散文。

### 目录结构

```text
qikou/
├── SKILL.md                          # Skill 完整规范与执行准则
├── references/
│   └── prompt-templates.md           # 双 Agent 提示词模板
└── scripts/
    └── run_deai.py                   # Windows 本地 SAPI 音频合成脚本
```

### 快速开始

#### 1. 环境要求
- Windows 操作系统（用于 SAPI 本地语音合成）
- Python 3.8+
- 安装依赖：
  ```bash
  pip install pywin32
  ```

#### 2. 本地音频合成
```bash
# 将文本文件转换为 wav 音频
python scripts/run_deai.py <input_text_path> [output_wav_path]

# 或通过命令行字符串直接生成
python scripts/run_deai.py "待转换的文本内容" output.wav
```

#### 3. 作为 Agent Skill 使用
将本仓库克隆至你的 Agent Skills 目录下：
```bash
git clone https://github.com/Joffoo/qikou.git .agents/skills/qikou
```

---

## English

**Qikou** is a dual-agent de-AI writing workflow driven by **physical TTS audio synthesis** and **natural speech cadence**.

By converting 2D text into temporal audio streams, Qikou leverages multimodal LLMs' auditory perception to understand natural breathing pauses and spoken rhythm, breaking free from clichéd patterns and robotic autoregressive habits.

### Architecture

```
[Subagent 1: Fact Extraction]
       │
       ▼
[Physical TTS: Local SAPI synthesizes .wav audio]
       │
       ▼
[Subagent 2: Blind Auditory Reconstruction]
 (★ Complete Isolation: Reads audio & fact sheet only, no raw text)
       │
       ▼
     Output
```

1. **Fact Extraction (Agent 1)**: Extracts an atomic, unadorned fact sheet based on ASD-STE100 principles, stripping away rhetorical flourishes and filler transitions.
2. **Physical TTS**: Synthesizes genuine 16-bit PCM WAV audio via local system speech synthesis (Windows SAPI).
3. **Blind Auditory Reconstruction (Agent 2)**: Subagent 2 operates in strict isolation with no access to raw text. Receiving only the audio file and fact sheet, it reconstructs natural prose guided by physiological breathing cadence.

### Directory Structure

```text
qikou/
├── SKILL.md                          # Full Skill specification and execution rules
├── references/
│   └── prompt-templates.md           # Dual-agent prompt templates
└── scripts/
    └── run_deai.py                   # Local Windows SAPI audio synthesis script
```

### Quick Start

#### 1. Requirements
- Windows OS (for Windows SAPI speech engine)
- Python 3.8+
- Install dependencies:
  ```bash
  pip install pywin32
  ```

#### 2. Local Audio Generation
```bash
# Convert a text file into wav audio
python scripts/run_deai.py <input_text_path> [output_wav_path]

# Or generate directly from text string
python scripts/run_deai.py "Text content to speak" output.wav
```

#### 3. Install as an Agent Skill
Clone into your agent's skills directory:
```bash
git clone https://github.com/Joffoo/qikou.git .agents/skills/qikou
```

---

## License

[MIT](LICENSE)
