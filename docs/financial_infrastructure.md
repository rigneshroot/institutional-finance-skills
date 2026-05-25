# 🏦 Core Financial Infrastructure & Resources

To understand how our Explainable AI (XAI) pipeline operates, it is helpful to outline the primary financial database and symbology systems we rely upon, alongside recommended search portals:

---

## 1. SEC Form 13F
**SEC Form 13F** is a quarterly regulatory filing required by the **U.S. Securities and Exchange Commission (SEC)**.
* **Who must file**: Any institutional investment manager (e.g., hedge funds, mutual funds, trust companies, pension funds) overseeing at least **$100 million** in qualifying U.S. equity assets.
* **What is disclosed**: Standard long equity holdings, share counts, options (puts/calls), and convertible debt weights. 
* **The Structural Limitations (Why we need XAI)**: 
  - **Reporting Latency**: Managers have up to **45 days** after the close of each fiscal quarter to file. Therefore, a filing represents a retroactive historical snapshot, not active real-time positioning.
  - **Zero Context**: The filing is purely a numeric tabular table. It contains no strategic rationale, risk parameters, or explanations for portfolio rotations.
  - **Exclusions**: 13F filings exclude short positions, non-U.S. listings, and cash balances.

---

## 2. OpenFIGI (Financial Instrument Global Identifier)
**OpenFIGI** is an open-source, standardized global symbology framework maintained by Bloomberg and the Object Management Group.
* **Why it is critical to this project**: Raw SEC 13F filings do not list familiar stock tickers (like `AAPL` or `MSFT`). Instead, regulatory tables list assets using their **CUSIP** numbers (a unique 9-digit alphanumeric security identifier) or the issuer's registered corporate name.
* **How we use it**: The `market-distribution-mapper` and standard parsers in our CLI pipeline connect to the OpenFIGI API to dynamically translate complex CUSIP identifiers into standard, human-readable tickers and their global primary exchange listings in real time.

---

## 🌐 Recommended Reference Resources

To benchmark your results, verify CIK identifiers, or configure your Claude environment, we recommend referring to the following primary websites:

### Ingestion & Search Databases
* **[SEC EDGAR Company Search](https://www.sec.gov/edgar/searchedgar/companysearch)**:
  The official U.S. government database. Use this to lookup any institutional manager (e.g., searching "Bridgewater" or "Citadel"), copy their official **10-digit Central Index Key (CIK)**, and inspect raw Form 13F-HR XML tables directly from the filing directory.
* **[WhaleWisdom Portfolio Tracker](https://whalewisdom.com)**:
  The industry-standard public platform for institutional disclosures. Highly recommended for cross-referencing your parsed output, verifying historical HHI concentration indices, and checking sector-rotation heatmaps.

### Financial Symbology & Tickers
* **[OpenFIGI Search Registry](https://openfigi.com)**:
  Use this portal to lookup security tickers, cross-reference 9-digit CUSIPs with Financial Instrument Global Identifiers (FIGI), and inspect exchange-listing details.

### Claude Skills & Environment Setup
* **[Anthropic Claude Projects Guide](https://support.anthropic.com)**:
  Refer to the official support documentation for details on setting up **Claude Projects**, configuring workspace custom instructions, and managing uploaded knowledge databases.
