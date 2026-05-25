# 🚀 Getting Started Guide

Equipping your Claude AI assistant with these analytical capabilities is highly straightforward. You can activate these skills using Claude.ai Projects or Developer System Prompts.

---

## 🛠️ Prerequisites

To run the automated data ingestion pipeline (`run.py`), you only need a standard Python 3.9+ installation and the lightweight **`requests`** library. All other parsing routines use Python's built-in standard library (like `json`, `os`, and `xml.etree.ElementTree`).

Install the single external dependency:
```bash
pip install requests
```

---

## 📥 Loading Skills into Claude (Select One Option)

### Option A: Claude.ai Projects (Recommended)
1. Navigate to **[Claude.ai](https://claude.ai)** and open or create a **Project** (available on Pro/Team tiers).
2. Click **Add Content** under the Project Knowledge section.
3. Upload the `.md` files of the specific skills you wish to activate from the [`skills/`](../skills/) directory (e.g., `skills/institutional-rationale-engine/SKILL.md`).
4. Claude will automatically index these files, equipping itself with the structural schemas, persona constraints, and analytical workflows defined within the skills.

### Option B: Developer API / System Instructions
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

👉 Next: **[How to Use Guide](how_to_use.md)**
