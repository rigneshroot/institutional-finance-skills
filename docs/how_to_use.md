# 💻 How to Use Guide

We have eliminated tedious copy-paste workflows. You can interact with these skills using two simple, elegant patterns:

---

## 💡 Input Flexibility: No JSON Required!

> [!TIP]
> While our technical specifications illustrate a structured **JSON input** (ideal for automated API pipelines), **Claude does not require JSON at all**. 
> 
> Because Claude has advanced natural language reasoning, you can feed data in **any format you prefer**:
> * **Plain Text Lists**: Just type: *"Apple: 300M shares, Chevron: 120M shares"*
> * **Copy-Pasted Web Tables**: Directly copy a holdings table from Yahoo Finance, WhaleWisdom, or an Excel grid and paste it into the chat.
> * **Raw CSV / Text Logs**: Upload or paste unformatted comma-separated text.
> 
> Claude will automatically parse the data, organize it internally, and execute the exact analytical steps defined within the skills.

---

## 🤖 Option A: The Agentic Workflow (Zero Clicks / One Prompt)

If you are using an **Agentic AI coding assistant** (such as Claude Code, terminal-connected environments, or Antigravity):
Simply type a single natural-language instruction in your chat:
> *"Run `run.py` to fetch Berkshire Hathaway's latest holdings, then analyze their strategy using the activated skills."*

The AI assistant will automatically run the ingestion script, read the output file, parse the data, and render the complete academic report directly in your chat in a single turn!

---

## 🖥️ Option B: The One-Command CLI Workflow (No Copy-Paste)

If you are working in a standard local terminal, run the unified CLI script to fetch and format live filings in one step:

```bash
# General Usage: python run.py "<Institution Name or Ticker>"
python run.py "Berkshire Hathaway"
```

This will automatically:
1. Contact the **SEC EDGAR API** and resolve the target CIK code.
2. Download and parse the live 13F XML holdings table directly from the SEC directory.
3. Render a beautiful portfolio concentration dashboard directly in your terminal.
4. Export the formatted dataset as a structured file in your workspace, printing the **exact absolute filesystem location** (e.g., `berkshire_hathaway_holdings.json`).

### Interacting in Claude
Once the JSON file is generated in your workspace, you can simply upload the file into Claude or prompt your assistant:
> *"Analyze the portfolio located in `berkshire_hathaway_holdings.json` using the Macro Theme Detector skill."*

Claude will read the file directly, completely eliminating the need to copy-paste thousands of lines of raw JSON payload.

---

👉 Next: **[Sophisticated Conversational Commands](prompt_templates.md)**
