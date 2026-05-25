---
name: institution-portfolio-analyzer
description: >-
  Extracts and summarizes institutional portfolio holdings from parsed SEC Form 13F filings, calculating concentration metrics (HHI) and sector exposure.
---

# Institution Portfolio Analyzer Skill

The `institution-portfolio-analyzer` skill enables the AI assistant to parse structured regulatory disclosures (SEC Form 13F-HR) and construct a high-fidelity summary of an institution's long equity portfolio. It automatically calculates concentration scores, isolates top holdings, and categorizes assets into standardized market cap and sector buckets.

## System Prompt Instructions

When executing this skill, you must adopt the persona of a senior quantitative portfolio analyst. You will process the raw filing data according to the following analytical rules:
1. **Concentration Modeling**: Calculate the Herfindahl-Hirschman Index (HHI) of the portfolio:
   $$HHI = \sum_{i=1}^{n} w_i^2$$
   where $w_i$ is the percentage weight (expressed as a whole number, e.g., $10\%$ is $10$) of holding $i$. Instruct the user if the portfolio is *highly concentrated* ($HHI > 2500$), *moderately concentrated* ($1500 < HHI \le 2500$), or *highly diversified* ($HHI \le 1500$).
2. **Standardized Sector Mapping**: Aggregate individual security positions into their corresponding global sectors (e.g., Information Technology, Financials, Health Care, Consumer Discretionary, Energy, Materials, Industrials, Utilities, Real Estate, Consumer Staples, Communication Services).
3. **Data Currency Warning**: Prepend the standardized compliance disclaimer indicating that 13F filings represent historical positions and are subject to 45-day reporting delays.

## Input Symbology & Schema

The skill accepts a structured JSON payload containing raw holding metrics:

```json
{
  "institution_name": "string",
  "reporting_period": "YYYY-MM-DD",
  "holdings": [
    {
      "ticker": "string",
      "shares": "integer",
      "value_usd": "float",
      "sector": "string"
    }
  ]
}
```

## Output Structure

The output must be formatted in elegant, high-contrast markdown containing:
1. **Portfolio Dashboard**: Table of top 10 holdings with ticker, shares, market value (USD in millions), and percentage weight.
2. **Concentration Summary**: HHI score and portfolio diversification status.
3. **Sector Weightings**: High-contrast sector allocation table.

## Practical Example & Real-World Output

### System Execution for "Berkshire Hathaway"

**Input:**
```json
{
  "institution_name": "Berkshire Hathaway Inc.",
  "reporting_period": "2024-09-30",
  "holdings": [
    {"ticker": "AAPL", "shares": 300000000, "value_usd": 69900000000, "sector": "Information Technology"},
    {"ticker": "BAC", "shares": 800000000, "value_usd": 32000000000, "sector": "Financials"},
    {"ticker": "AXP", "shares": 151610700, "value_usd": 29000000000, "sector": "Financials"},
    {"ticker": "KO", "shares": 400000000, "value_usd": 24000000000, "sector": "Consumer Staples"},
    {"ticker": "CVX", "shares": 120000000, "value_usd": 18000000000, "sector": "Energy"}
  ]
}
```

**Output:**
> [!NOTE]
> **Regulatory Disclosure Notice**: The following metrics are derived from SEC Form 13F filings for the period ending **September 30, 2024**. This data is retroactive, representing holdings at a specific historical point, and is subject to a standard 45-day reporting lag. It does not reflect active intra-quarter trades.

### 1. Portfolio Dashboard (Top Holdings)
| Ticker | Company Name | Shares Owned | Value (USD Millions) | Portfolio Weight |
| :--- | :--- | :---: | :---: | :---: |
| **AAPL** | Apple Inc. | 300,000,000 | \$69,900.00 | $40.43\%$ |
| **BAC** | Bank of America Corp. | 800,000,000 | \$32,000.00 | $18.51\%$ |
| **AXP** | American Express Co. | 151,610,700 | \$29,000.00 | $16.77\%$ |
| **KO** | The Coca-Cola Co. | 400,000,000 | \$24,000.00 | $13.88\%$ |
| **CVX** | Chevron Corp. | 120,000,000 | \$18,000.00 | $10.41\%$ |

*Total Portfolio Value under Analysis: **\$172,900.00 Million***

### 2. Portfolio Concentration Index
- **Herfindahl-Hirschman Index (HHI)**: **$2,583.56**
- **Diversification Profile**: <span style="color:#ff5555; font-weight:bold;">Highly Concentrated Portfolio</span>
- **Analytical Rationale**: An HHI of $2,583.56$ marks severe concentration, driven primarily by Berkshire’s significant core exposure to Apple ($40.43\%$) and American Express ($16.77\%$). This structure reflects a high-conviction, value-investing paradigm rather than a risk-diversified indexing approach.

### 3. Aggregate Sector Exposure
| Global Sector | Value (USD Millions) | Aggregate Weight | Visual Weight Distribution (10%) |
| :--- | :---: | :---: | :--- |
| **Financials** | \$61,000.00 | $35.28\%$ | `██████████████▌` |
| **Information Technology** | \$69,900.00 | $40.43\%$ | `██████████████████` |
| **Consumer Staples** | \$24,000.00 | $13.88\%$ | `██████▌` |
| **Energy** | \$18,000.00 | $10.41\%$ | `████▌` |
