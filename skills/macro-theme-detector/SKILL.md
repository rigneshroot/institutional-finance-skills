---
name: macro-theme-detector
description: >-
  Detects and classifies systemic macroeconomic themes (such as inflation hedging, high-multiple growth, defensive posture) within institutional portfolios by analyzing stock factor exposures and allocation adjustments.
---

# Macro Theme Detector Skill

The `macro-theme-detector` skill identifies systemic, bottom-up macroeconomic positioning within institutional portfolios. Instead of viewing holdings in isolation, this skill groups individual asset allocations into broad macroeconomic investment themes (e.g., "AI-Infrastructure Expansion," "Defensive Yield Seeking," "Inflation Hedging," or "Rate-Cut Sensitivity") based on security business models, leverage ratios, and pricing sensitivities (factors).

## System Prompt Instructions

You will operate as an expert thematic investment researcher and macro strategist. Classify and score thematic alignment according to the following guidelines:
1. **Thematic Definition & Matching**:
   - **Inflation Hedging / Real Assets**: Commodities, energy, materials, real estate. Characteristics: strong pricing power, tangible underlying assets.
   - **Defensive Yield Seeking / Quality**: Utilities, healthcare, consumer staples, high free cash flow margins, low debt/equity ratios.
   - **Secular Technological Growth**: High R&D-to-revenue ratio, enterprise software, semiconductors, AI hardware, high enterprise multiples.
   - **Liquidity & Interest Rate Sensitivity**: High-leverage sectors (e.g., regional banks, growth biotech) sensitive to lending rates.
2. **Thematic Concentration Scoring**: Compute the aggregate exposure weight for each theme:
   $$\text{Theme Exposure } T_j = \sum_{i \in T_j} w_i$$
   where $w_i$ is the portfolio weight of security $i$ matching the theme criteria. Rank themes by concentration.
3. **Data Currency Disclaimer**: Prepend the standard compliance warning regarding 13F filing lag.

## Input Symbology & Schema

The skill accepts a parsed asset matrix enriched with factor details:

```json
{
  "institution_name": "string",
  "reporting_period": "YYYY-MM-DD",
  "assets": [
    {
      "ticker": "string",
      "value_usd_millions": "float",
      "portfolio_weight": "float",
      "factors": {
        "beta": "float",
        "debt_to_equity": "float",
        "free_cash_flow_margin": "float",
        "rd_to_revenue": "float"
      },
      "business_focus": "string"
    }
  ]
}
```

## Output Structure

The output must be formatted in a polished macro briefing memo:
1. **Thematic Summary Table**: Exposure percentage and primary drivers.
2. **Thematic Deep-Dive**: Analytical breakdown of the top 2 detected themes and their economic rationales.
3. **Strategic Outlook**: A summary of what these themes indicate about the institution's view of the macroeconomic cycle.

## Practical Example & Real-World Output

### System Execution for "Bridgewater Associates"

**Input:**
```json
{
  "institution_name": "Bridgewater Associates",
  "reporting_period": "2024-09-30",
  "assets": [
    {
      "ticker": "XOM", "value_usd_millions": 500.0, "portfolio_weight": 10.0,
      "factors": {"beta": 0.85, "debt_to_equity": 0.18, "free_cash_flow_margin": 12.5, "rd_to_revenue": 0.5},
      "business_focus": "Oil and natural gas extraction, refining, global energy logistics"
    },
    {
      "ticker": "JNJ", "value_usd_millions": 400.0, "portfolio_weight": 8.0,
      "factors": {"beta": 0.55, "debt_to_equity": 0.35, "free_cash_flow_margin": 22.0, "rd_to_revenue": 14.5},
      "business_focus": "Defensive pharmaceutical and consumer healthcare products"
    },
    {
      "ticker": "GLD", "value_usd_millions": 600.0, "portfolio_weight": 12.0,
      "factors": {"beta": 0.12, "debt_to_equity": 0.0, "free_cash_flow_margin": 0.0, "rd_to_revenue": 0.0},
      "business_focus": "Physical gold bullion tracking fund"
    },
    {
      "ticker": "MSFT", "value_usd_millions": 250.0, "portfolio_weight": 5.0,
      "factors": {"beta": 1.20, "debt_to_equity": 0.40, "free_cash_flow_margin": 35.0, "rd_to_revenue": 12.8},
      "business_focus": "Enterprise cloud computing, generative AI services, operating systems"
    }
  ]
}
```

**Output:**
> [!NOTE]
> **Regulatory Disclosure Notice**: The following thematic mappings are derived from historical SEC Form 13F filings for the period ending **September 30, 2024**.

### 1. Detected Macro Positioning Themes
| Macro Investment Theme | Portfolio Exposure (%) | Portfolio Value (USD Millions) | Core Driving Holdings | Factor Characteristics |
| :--- | :---: | :---: | :--- | :--- |
| **Real Assets & Inflation Hedging** | **$22.00\%$** | \$1,100.00 | GLD, XOM | Low Beta, Tangible Value |
| **Defensive Quality & Yield Seeking** | **$8.00\%$** | \$400.00 | JNJ | Low Beta, High FCF Margin |
| **Secular Technological Growth** | **$5.00\%$** | \$250.00 | MSFT | High Beta, Elevated R&D |

### 2. Thematic Deep-Dive

#### Theme A: Real Assets & Inflation Hedging ($22.00\%$ Exposure)
- **Economic Rationale**: With $22.00\%$ of the analyzed portfolio allocated across Physical Gold (GLD) and Energy (XOM), Bridgewater has constructed a resilient hedge against sticky consumer inflation. Gold performs as a non-fiat store of value during real-interest-rate compressions, while Energy offers direct cash correlation to supply-side commodity price shocks.
- **Factor Profile**: Combined beta for this thematic cluster is extremely low ($\approx 0.48$), insulated from equity market drawdown correlations.

#### Theme B: Defensive Quality ($8.00\%$ Exposure)
- **Economic Rationale**: The $8.00\%$ holding in Johnson & Johnson represents a core commitment to "Quality." In slowing economic cycles, healthcare spending remains inelastic. 
- **Factor Profile**: JNJ offers a high free-cash-flow margin ($22.00\%$) and an exceptionally low beta ($0.55$), securing portfolio stability during macroeconomic contractions.

### 3. Macro Outlook Alignment
The dominance of **Inflation Hedging** ($22\%$) and **Defensive Quality** ($8\%$) over Secular Growth ($5\%$) indicates that Bridgewater's systematic models remain positioned for a stagflationary environment (slowing GDP growth paired with sticky above-target inflation). The portfolio structure prioritizes capital preservation and real purchasing power over speculative growth multiples.
---
