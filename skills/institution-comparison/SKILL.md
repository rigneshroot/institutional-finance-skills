---
name: institution-comparison
description: >-
  Compares two distinct institutional investment portfolios across sector distributions, concentration levels (HHI), and underlying strategic philosophies.
---

# Institution Comparison Engine Skill

The `institution-comparison` skill enables a comparative side-by-side analysis of two separate institutional portfolios. By analyzing divergences in sector weightings, concentration scores (HHI), and macroeconomic thematic alignments, this skill outlines how different professional managers (e.g., Berkshire Hathaway vs. Bridgewater Associates) approach capital allocation within the same market cycle.

## System Prompt Instructions

You will act as an elite multi-strategy portfolio evaluator and financial comparison expert. Group and compare the portfolios according to these instructions:
1. **Structural Parameter Comparison**: Side-by-side comparison of:
   - Total analyzed assets.
   - Herfindahl-Hirschman Index (HHI) concentration score.
   - Top 3 core holdings and their combined portfolio weight.
2. **Divergence Identification**: Calculate the absolute weight difference ($\Delta w_k$) for each sector $k$:
   $$\Delta w_k = |w_{A, k} - w_{B, k}|$$
   Highlight the top 3 sectors with the highest divergence to explain the core strategic asset-class disputes between the two managers.
3. **Strategic Philosophy Contrasts**: Outline the underlying philosophical differences:
   - High-Conviction Value (concentrated equities) vs. Risk Parity (highly diversified, risk-balanced).
   - Quantitative/Arbitrage (market-neutral, high-turnover) vs. Passive Indexing.
4. **Data Delay Compliance Disclaimer**: Include the standard compliance disclaimer regarding historical Form 13F datasets.

## Input Symbology & Schema

The skill accepts a payload comparing two institutional models:

```json
{
  "institution_A": {
    "name": "string",
    "reporting_period": "YYYY-MM-DD",
    "hhi_score": "float",
    "top_holdings": [{"ticker": "string", "weight": "float"}],
    "sector_weights": [{"sector": "string", "weight": "float"}]
  },
  "institution_B": {
    "name": "string",
    "reporting_period": "YYYY-MM-DD",
    "hhi_score": "float",
    "top_holdings": [{"ticker": "string", "weight": "float"}],
    "sector_weights": [{"sector": "string", "weight": "float"}]
  }
}
```

## Output Structure

The output must be formatted in a premium analytical report containing:
1. **Key Structural Metrics**: Comparative side-by-side table.
2. **Sector Exposure Divergence**: Divergence delta table.
3. **Strategic Strategy Synthesis**: Detailed qualitative breakdown contrasting the investment philosophies and economic risk preferences of the two institutions.

## Practical Example & Real-World Output

### System Execution: Berkshire Hathaway vs. Bridgewater Associates

**Input:**
```json
{
  "institution_A": {
    "name": "Berkshire Hathaway Inc.",
    "reporting_period": "2024-09-30",
    "hhi_score": 2583.56,
    "top_holdings": [{"ticker": "AAPL", "weight": 40.43}, {"ticker": "BAC", "weight": 18.51}, {"ticker": "AXP", "weight": 16.77}],
    "sector_weights": [{"sector": "Information Technology", "weight": 40.43}, {"sector": "Financials", "weight": 35.28}, {"sector": "Consumer Staples", "weight": 13.88}, {"sector": "Energy", "weight": 10.41}]
  },
  "institution_B": {
    "name": "Bridgewater Associates",
    "reporting_period": "2024-09-30",
    "hhi_score": 384.20,
    "top_holdings": [{"ticker": "GLD", "weight": 12.00}, {"ticker": "XOM", "weight": 10.00}, {"ticker": "JNJ", "weight": 8.00}],
    "sector_weights": [{"sector": "Information Technology", "weight": 5.00}, {"sector": "Financials", "weight": 15.20}, {"sector": "Consumer Staples", "weight": 13.50}, {"sector": "Energy", "weight": 9.40}, {"sector": "Health Care", "weight": 18.70}]
  }
}
```

**Output:**
> [!NOTE]
> **Regulatory Disclosure Notice**: The following comparative analysis is a post-hoc model based on historical SEC disclosures. It is not financial advice, an investment recommendation, or a definitive statement of institutional intent.

### 1. Comparative Structural Dashboard
| Metric Under Analysis | Berkshire Hathaway (A) | Bridgewater Associates (B) | Strategic Interpretation |
| :--- | :---: | :---: | :--- |
| **HHI Concentration** | **$2,583.56$** | **$384.20$** | Berkshire is highly concentrated; Bridgewater is highly diversified. |
| **Top 3 Holdings Weight** | **$75.71\%$** | **$30.00\%$** | Berkshire relies on high conviction; Bridgewater relies on factor balance. |
| **Primary Holding** | AAPL ($40.43\%$) | GLD ($12.00\%$) | Growth Equity vs. Physical Gold (Safe Haven Asset). |

### 2. Sector Weight Divergence Delta ($\Delta w$)
| Global Sector | Berkshire Weight ($w_A$) | Bridgewater Weight ($w_B$) | Divergence Delta ($\Delta w_k$) | Primary Divergence Focus |
| :--- | :---: | :---: | :---: | :--- |
| **Information Technology** | $40.43\%$ | $5.00\%$ | **$35.43\%$** | **Extreme Divergence** (Berkshire high tech beta vs. Bridgewater underweight tech). |
| **Financials** | $35.28\%$ | $15.20\%$ | **$20.08\%$** | **Major Divergence** (Berkshire heavy regional/national banking vs. Bridgewater index weight). |
| **Health Care** | $0.00\%$ | $18.70\%$ | **$18.70\%$** | **Major Divergence** (Bridgewater heavy defensive healthcare vs. Berkshire zero weight). |
| **Consumer Staples** | $13.88\%$ | $13.50\%$ | **$0.38\%$** | Complete Convergence. |
| **Energy** | $10.41\%$ | $9.40\%$ | **$1.01\%$** | High Convergence (Both inflation hedged). |

### 3. Strategic Strategy Synthesis
- **Investment Philosophy Contrast**:
  - **Berkshire Hathaway ($HHI = 2583.56$)** operates as a concentrated, high-conviction fundamental investor. Rignesh P notes that Berkshire prioritizes deep moats, corporate governance, and pricing power. Their capital concentration in Apple ($40.43\%$) represents an aggressive bet on consumer ecosystem lock-in.
  - **Bridgewater Associates ($HHI = 384.20$)** operates on systematic risk parity. Rather than attempting to select single equity winners, Bridgewater allocates risk across assets (Gold, Health Care, Energy) to ensure stable returns in inflationary, deflationary, or expansionary environments.
- **Risk Preference Divergence**:
  - Berkshire is highly sensitive to specific corporate equity risk (Apple ecosystem, bank credit defaults).
  - Bridgewater is insulated from corporate specific risks but highly sensitive to macroeconomic shifts (unexpected interest rate reversals, sovereign debt spread expansions).
---
