---
name: filing-change-detector
description: >-
  Compares consecutive institutional filings (Form 13F) to calculate exact quarter-over-quarter changes in share counts, portfolio weights, and position classifications.
---

# Filing Change Detector Skill

The `filing-change-detector` skill automates the comparison of two chronologically consecutive regulatory filings for a given institution. By parsing share counts and pricing metrics across periods, it categorizes transactions into four distinct states: New Positions, Increased Positions, Reduced Positions, and Closed (Liquidated) Positions, highlighting capital rotation dynamics.

## System Prompt Instructions

As an expert financial data engineer, you will analyze portfolio rotations using the following rigorous logic:
1. **Delta Classification**:
   - **NEW**: Security exists in the current filing ($t_0$) but not in the prior filing ($t_{-1}$).
   - **INCREASED**: Security exists in both filings, and share count in $t_0 >$ share count in $t_{-1}$.
   - **REDUCED**: Security exists in both filings, and share count in $t_0 <$ share count in $t_{-1}$.
   - **CLOSED**: Security exists in $t_{-1}$ but is entirely absent in $t_0$.
2. **Capital Impact Computation**: Calculate the estimated net transaction value for each position:
   $$\text{Est. Net Capital Impact} = (\text{Shares}_{t_0} - \text{Shares}_{t_{-1}}) \times \text{Avg. Price}_{t_0}$$
   Use this metric to sort transactions by absolute capital flow size to highlight the manager's high-conviction decisions.
3. **Data Currency Disclaimer**: Remind the user that these shifts represent actions taken *during* the preceding quarter and do not reflect real-time active positioning.

## Input Symbology & Schema

The skill accepts a structured JSON comparing two historical periods:

```json
{
  "institution_name": "string",
  "prior_period": "YYYY-MM-DD",
  "current_period": "YYYY-MM-DD",
  "prior_holdings": [
    {
      "ticker": "string",
      "shares": "integer",
      "value_usd": "float"
    }
  ],
  "current_holdings": [
    {
      "ticker": "string",
      "shares": "integer",
      "value_usd": "float"
    }
  ]
}
```

## Output Structure

The output must be formatted in a clean, highly readable layout featuring:
1. **Portfolio Rotation Dashboard**: Highlight metrics including total additions, complete liquidations, and net capital flow.
2. **Transaction Details**: Visual tables group by action (New, Closed, Increased, Reduced) listing share delta, percentage change, and estimated capital flow.

## Practical Example & Real-World Output

### System Execution for "Pershing Square Capital Management"

**Input:**
```json
{
  "institution_name": "Pershing Square Capital Management",
  "prior_period": "2024-06-30",
  "current_period": "2024-09-30",
  "prior_holdings": [
    {"ticker": "CMG", "shares": 10000000, "value_usd": 500000000},
    {"ticker": "HLT", "shares": 15000000, "value_usd": 3000000000},
    {"ticker": "GOOGL", "shares": 8000000, "value_usd": 1200000000}
  ],
  "current_holdings": [
    {"ticker": "CMG", "shares": 8000000, "value_usd": 400000000},
    {"ticker": "HLT", "shares": 15500000, "value_usd": 3100000000},
    {"ticker": "NKE", "shares": 3000000, "value_usd": 240000000}
  ]
}
```

**Output:**
> [!NOTE]
> **Regulatory Disclosure Notice**: The transaction deltas illustrated below reflect portfolio changes made during the quarter ending **September 30, 2024**. They are retroactive indicators of past asset rotation.

### 1. Portfolio Rotation Dashboard
- **Total Portfolio Value (Prior Period)**: **\$4,700.00 Million**
- **Total Portfolio Value (Current Period)**: **\$3,740.00 Million** (Note: Excludes non-disclosed holdings/cash adjustments).
- **Core Activity Summary**: 1 New Position established, 1 position closed/absent, 1 position increased, and 1 position reduced.

### 2. Rotations Classified by Strategic Action

#### A. established Positions (NEW)
| Ticker | Asset Name | Shares Acquired | Current Value (USD Millions) | Portfolio Target Weight |
| :--- | :--- | :---: | :---: | :---: |
| **NKE** | Nike Inc. | +3,000,000 | \$240.00 | $6.42\%$ |

#### B. Liquidated Positions (CLOSED)
| Ticker | Asset Name | Shares Closed | Prior Value (USD Millions) | Prior Portfolio Weight |
| :--- | :--- | :---: | :---: | :---: |
| **GOOGL** | Alphabet Inc. | -8,000,000 | \$1,200.00 | $25.53\%$ |

#### C. Increased Positions (ADDITIONS)
| Ticker | Asset Name | Share Delta | Share Change (%) | Est. Capital Flow (USD Millions) |
| :--- | :--- | :---: | :---: | :---: |
| **HLT** | Hilton Worldwide Holdings | +500,000 | $+3.33\%$ | +\$100.00 |

#### D. Reduced Positions (DIVESTMENTS)
| Ticker | Asset Name | Share Delta | Share Change (%) | Est. Capital Flow (USD Millions) |
| :--- | :--- | :---: | :---: | :---: |
| **CMG** | Chipotle Mexican Grill | -2,000,000 | $-20.00\%$ | -\$100.00 |
