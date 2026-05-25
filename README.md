# Institutional Intelligence Skills: Explainable Institutional Portfolio Intelligence Core

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Rignesh%20P-purple)](institutional_intelligence_skills_research_document.md)
[![Platform](https://img.shields.io/badge/Platform-Claude%20Skills-orange)](skills/)

Welcome to the **Institutional Intelligence Skills** repository, an open-source Explainable AI (XAI) framework built on the **Claude Skills** architecture. Authored by **Rignesh P**, this repository bridges the informational gap between institutional investment giants and independent market researchers by transforming dense, retroactive regulatory filings into structured, macro-contextualized portfolio intelligence.

---

## 📖 Research Foundation

The mathematical models, empirical evaluations, and cognitive frameworks backing this technology are detailed in the accompanying research paper:
👉 **[Institutional Intelligence Skills Research Paper](institutional_intelligence_skills_research_document.md)**

This research introduces a scientific empirical framework using:
- **Independent Variables (IV)**: Explanation Reasoning Paradigms, Macroeconomic Contextualization Depths, and Input Temporal Granularities.
- **Dependent Variables (DV)**: User Comprehension Scores ($\Delta_c$), Calibrated Trust Indices ($T_c$), Downstream Actionability Utility ($U_a$), and Strategic Rationale Strategic Fidelity ($F_s$).
- **Control Variables (CV)**: User Financial Sophistication, Institutional Strategy Archetypes, Baseline Market Regimes, and Model Architectures.

---

## 🎨 Research & Architecture Visualizations

Browse the conceptual, technical, and analytical foundations of our XAI system through this interactive research carousel:

### Conceptual Research Framework (Figure 1)
![Figure 1: Scientific Conceptual Framework](assets/conceptual_framework.png)

### Technical System Architecture (Figure 2)
![Figure 2: Technical System Architecture](assets/system_architecture.png)

### Portfolio Sector Allocation Comparison (Figure 3)
![Figure 3: Portfolio Sector Allocation Comparison](assets/sector_allocation.png)

---

## 🛠️ Claude Skills Core

This repository is engineered as a **Claude Skills-only repository**, containing 6 decoupled, enterprise-grade analytical skills. Each skill is packaged in a self-contained directory containing its isolated `SKILL.md` instruction file:

| Reusable Claude Skill | Location | Analytical Purpose |
| :--- | :--- | :--- |
| **Institution Portfolio Analyzer** | [`skills/institution-portfolio-analyzer/SKILL.md`](skills/institution-portfolio-analyzer/SKILL.md) | Parses raw 13F holdings, aggregates standardized sectors, and evaluates Herfindahl-Hirschman Index (HHI) concentration scores. |
| **Filing Change Detector** | [`skills/filing-change-detector/SKILL.md`](skills/filing-change-detector/SKILL.md) | Tracks quarter-over-quarter share movements, isolating new, increased, reduced, and liquidated holdings. |
| **Institutional Rationale Engine** | [`skills/institutional-rationale-engine/SKILL.md`](skills/institutional-rationale-engine/SKILL.md) | Synthesizes explainable, probabilistic rationales for portfolio shifts using macroeconomic catalysts. |
| **Market Distribution Mapper** | [`skills/market-distribution-mapper/SKILL.md`](skills/market-distribution-mapper/SKILL.md) | Stratifies assets across market-cap brackets, global domicile geographies, and specific sub-industries. |
| **Macro Theme Detector** | [`skills/macro-theme-detector/SKILL.md`](skills/macro-theme-detector/SKILL.md) | Groups positions into broad macroeconomic indicators (e.g., inflation hedges, growth exposure, defensive yield seeking). |
| **Institution Comparison Engine** | [`skills/institution-comparison/SKILL.md`](skills/institution-comparison/SKILL.md) | Performs side-by-side structural comparison and divergent sector weight evaluations of two managers. |

---

## 🚀 Getting Started

Equipping your Claude AI assistant with these analytical capabilities is highly straightforward. You can activate these skills using Claude.ai Projects or Developer System Prompts.

### Prerequisites
To run the automated data ingestion scripts, establish a local Python environment with the required dependencies:
```bash
pip install pandas requests yfinance
```

### Loading Skills into Claude (Select One Option)

#### Option A: Claude.ai Projects (Recommended)
1. Navigate to **Claude.ai** and open or create a **Project** (available on Pro/Team tiers).
2. Click **Add Content** under the Project Knowledge section.
3. Upload the `.md` files of the specific skills you wish to activate from the [`skills/`](skills/) directory (e.g., `skills/institutional-rationale-engine/SKILL.md`).
4. Claude will automatically index these files, equipping itself with the structural schemas, persona constraints, and analytical workflows defined within the skills.

#### Option B: Developer API / System Instructions
If you are interacting with Claude via the Anthropic Developer Console or API, append the contents of the chosen `SKILL.md` file directly into the `system` parameter of your API payload:
```python
import anthropic

client = anthropic.Anthropic()
with open("skills/institutional-rationale-engine/SKILL.md", "r") as f:
    skill_instructions = f.read()

message = client.messages.create(
    model="claude-3-5-sonnet-latest",
    max_tokens=4000,
    system=skill_instructions,
    messages=[
        {"role": "user", "content": "Analyze ExxonMobil allocation shifts using the provided payload..."}
    ]
)
```

---

## 💻 How to Use (Simplified Workflow)

We have eliminated tedious copy-paste workflows. You can interact with these skills using two simple, elegant patterns:

### Option A: The Agentic Workflow (Zero Clicks / One Prompt)
If you are using an **Agentic AI coding assistant** (such as Claude Code, terminal-connected environments, or Antigravity):
Simply type a single natural-language instruction in your chat:
> *"Run `run.py` to fetch Berkshire Hathaway's latest holdings, then analyze their strategy using the activated skills."*

The AI assistant will automatically run the ingestion script, read the output file, parse the data, and render the complete academic report directly in your chat in a single turn!

### Option B: The One-Command CLI Workflow (No Copy-Paste)
If you are working in a standard local terminal, run the unified CLI script to fetch and format live filings in one step:

```bash
# General Usage: python run.py "<Institution Name or Ticker>"
python run.py "Berkshire Hathaway"
```

This will automatically:
1. Contact the **SEC EDGAR API** and resolve the target CIK code.
2. Download and parse the live 13F XML holdings table directly from the SEC directory.
3. Render a beautiful portfolio concentration dashboard directly in your terminal.
4. Export the formatted dataset as a structured file in your workspace: `berkshire_hathaway_holdings.json`.

#### Interacting in Claude
Once the JSON file is generated in your workspace, you can simply upload the file into Claude or prompt your assistant:
> *"Analyze the portfolio located in `berkshire_hathaway_holdings.json` using the Macro Theme Detector skill."*

Claude will read the file directly, completely eliminating the need to copy-paste thousands of lines of raw JSON payload.

---

## 📂 Repository Structure

The workspace is strictly partitioned to adhere to the modular **Claude Skills-only repository** architecture:

```txt
institutional-finance-skills/
├── skills/
│   ├── institution-portfolio-analyzer/
│   │   └── SKILL.md
│   ├── filing-change-detector/
│   │   └── SKILL.md
│   ├── institutional-rationale-engine/
│   │   └── SKILL.md
│   ├── market-distribution-mapper/
│   │   └── SKILL.md
│   ├── macro-theme-detector/
│   │   └── SKILL.md
│   └── institution-comparison/
│       └── SKILL.md
├── assets/
│   ├── conceptual_framework.png
│   ├── system_architecture.png
│   └── sector_allocation.png
├── LICENSE
├── README.md
└── institutional_intelligence_skills_research_document.md
```

---

## ⚖️ License & Disclaimer

This project is licensed under the open-source **MIT License**—see the [`LICENSE`](LICENSE) file for complete details.

### Compliance Disclaimer
The analytical skills and explanations generated within this framework are probabilistic macroeconomic models based on delayed, backward-looking SEC disclosures (Form 13F). This system **does not provide financial advice, active trading commands, or investment predictions**. It is intended solely for academic research and post-hoc strategy interpretation.
