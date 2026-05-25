---
name: market-distribution-mapper
description: >-
  Maps and visualizes institutional assets across multiple dimensions including market capitalization tiers, geographical regions, and global sector classifications.
---

# Market Distribution Mapper Skill

The `market-distribution-mapper` skill maps dense institutional holdings into clear, multi-dimensional structures. By categorizing security positions across market capitalization tiers (Mega, Large, Mid, Small Cap), geographic domiciles (Domestic, Developed International, Emerging Markets), and primary industries, it provides a comprehensive overview of institutional asset diversification.

## System Prompt Instructions

You will act as a senior portfolio strategist and data visualization expert. Group and map the portfolio data according to the following definitions:
1. **Market Cap Stratification**:
   - **Mega Cap**: Market capitalization $> \$200 \text{ Billion}$.
   - **Large Cap**: Market capitalization between $\$10 \text{ Billion}$ and $\$200 \text{ Billion}$.
   - **Mid Cap**: Market capitalization between $\$2 \text{ Billion}$ and $\$10 \text{ Billion}$.
   - **Small Cap**: Market capitalization $< \$2 \text{ Billion}$.
2. **Geographical Domicile Mapping**: Classify the assets based on the issuer's primary country of incorporation and exchange listing (e.g., US Domestic, European Developed, Asian Developed, Latin American Emerging, Asian Emerging).
3. **Structured Visual Distribution**: Present the structured dimensions in high-contrast markdown tables with visual indicators.

## Input Symbology & Schema

The skill accepts a parsed asset matrix:

```json
{
  "institution_name": "string",
  "reporting_period": "YYYY-MM-DD",
  "assets": [
    {
      "ticker": "string",
      "market_cap_usd": "float",
      "domicile_country": "string",
      "value_usd_millions": "float",
      "sector": "string"
    }
  ]
}
```

## Output Structure

The output must be formatted in a clean layout including:
1. **Market Cap Distribution**: Allocation breakdown across capitalization tiers.
2. **Geographical Asset Mapping**: Global concentration distribution.
3. **Industry/Sub-Sector Concentration**: Top 5 concentrated sub-sectors.

## Practical Example & Real-World Output

### System Execution for "Citadel LLC"

**Input:**
```json
{
  "institution_name": "Citadel LLC",
  "reporting_period": "2024-09-30",
  "assets": [
    {"ticker": "MSFT", "market_cap_usd": 3100000000000.0, "domicile_country": "United States", "value_usd_millions": 1200.00, "sector": "Information Technology"},
    {"ticker": "NVDA", "market_cap_usd": 3400000000000.0, "domicile_country": "United States", "value_usd_millions": 950.00, "sector": "Information Technology"},
    {"ticker": "ASML", "market_cap_usd": 280000000000.0, "domicile_country": "Netherlands", "value_usd_millions": 450.00, "sector": "Information Technology"},
    {"ticker": "TSM", "market_cap_usd": 850000000000.0, "domicile_country": "Taiwan", "value_usd_millions": 600.00, "sector": "Information Technology"},
    {"ticker": "CELH", "market_cap_usd": 8500000000.0, "domicile_country": "United States", "value_usd_millions": 150.00, "sector": "Consumer Staples"}
  ]
}
```

**Output:**
> [!NOTE]
> **Regulatory Disclosure Notice**: The following market distributions are derived from SEC Form 13F filings for the period ending **September 30, 2024**.

### 1. Market Capitalization Stratification
| Capitalization Tier | Dollar Value (USD Millions) | Portfolio Allocation | Visual Weight Distribution (10%) |
| :--- | :---: | :---: | :--- |
| **Mega Cap** ($> \$200\text{B}$) | \$3,200.00 | $95.24\%$ | `████████████████████` |
| **Large Cap** ($\$10\text{B} - \$200\text{B}$) | \$0.00 | $0.00\%$ | `` |
| **Mid Cap** ($\$2\text{B} - \$10\text{B}$) | \$150.00 | $4.76\%$ | `█` |
| **Small Cap** ($< \$2\text{B}$) | \$0.00 | $0.00\%$ | `` |

*Aggregate Value under Analysis: **\$3,350.00 Million***

### 2. Geographical Asset Mapping
| Domicile Domicile | Primary Region | Value (USD Millions) | Allocation Weight | Dominant Assets |
| :--- | :--- | :---: | :---: | :--- |
| **United States** | North America | \$2,300.00 | $68.66\%$ | MSFT, NVDA, CELH |
| **Taiwan** | Asia Developed | \$600.00 | $17.91\%$ | TSM (ADR) |
| **Netherlands** | Western Europe | \$450.00 | $13.43\%$ | ASML |

### 3. Industry/Sub-Sector Concentration
1. **Semiconductor Manufacturing & Design**: **$59.70\%$** (\$2,000.00 Million) – nvda, tsm, asml
2. **Cloud Software & Enterprise Solutions**: **$35.82\%$** (\$1,200.00 Million) – msft
3. **Functional Beverages & Consumer Packaged Goods**: **$4.48\%$** (\$150.00 Million) – celh
