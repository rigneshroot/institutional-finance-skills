import os
import sys
import json
import argparse
import requests
import xml.etree.ElementTree as ET

# Standard headers required by SEC EDGAR API
HEADERS = {"User-Agent": "Institutional Research Agent research@example.com"}

def get_company_cik(ticker_or_name):
    """Retrieve the 10-digit SEC Central Index Key (CIK) for a given ticker or company name."""
    url = "https://www.sec.gov/files/company_tickers.json"
    try:
        r = requests.get(url, headers=HEADERS)
        if r.status_code == 200:
            data = r.json()
            for k, v in data.items():
                if v['ticker'] == ticker_or_name.upper() or v['title'].lower().startswith(ticker_or_name.lower()):
                    return str(v['cik_str']).zfill(10)
    except Exception as e:
        print(f"Error resolving CIK: {e}")
    return None

def fetch_13f_filing_xml(cik):
    """Fetch the latest Form 13F XML submission from SEC EDGAR."""
    submissions_url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    r = requests.get(submissions_url, headers=HEADERS)
    if r.status_code != 200:
        raise Exception(f"Failed to retrieve SEC submissions for CIK {cik}.")
    
    recent_filings = r.json()["filings"]["recent"]
    
    # Locate the latest 13F-HR (Holdings Report) filing
    latest_13f_index = None
    for idx, form in enumerate(recent_filings["form"]):
        if form == "13F-HR":
            latest_13f_index = idx
            break
            
    if latest_13f_index is None:
        raise Exception("No Form 13F-HR filings located for this institution.")
        
    accession_raw = recent_filings["accessionNumber"][latest_13f_index]
    accession = accession_raw.replace("-", "")
    filing_date = recent_filings["filingDate"][latest_13f_index]
    
    # List documents in the filing submission
    doc_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession}/index.json"
    doc_resp = requests.get(doc_url, headers=HEADERS)
    if doc_resp.status_code != 200:
        raise Exception("Failed to access filing document directory.")
        
    # Find the XML information table file (typically ends in XML or informationtable.xml)
    xml_filename = None
    for file_info in doc_resp.json()["directory"]["item"]:
        name = file_info["name"].lower()
        if "informationtable" in name and name.endswith(".xml"):
            xml_filename = file_info["name"]
            break
        elif name.endswith(".xml") and not name.startswith("form13f"):
            xml_filename = file_info["name"]
            
    if not xml_filename:
        # Fallback to standard information table naming
        xml_filename = "informationtable.xml"
        
    xml_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession}/{xml_filename}"
    xml_resp = requests.get(xml_url, headers=HEADERS)
    if xml_resp.status_code != 200:
        raise Exception(f"Failed to retrieve XML table data from {xml_url}.")
        
    return xml_resp.text, filing_date

def parse_13f_xml(xml_content):
    """Parse the SEC Form 13F information table XML and extract tickers and weights."""
    root = ET.fromstring(xml_content)
    
    # SEC XML schemas typically use a namespace. We extract it automatically.
    namespace = ""
    if root.tag.startswith("{"):
        namespace = root.tag.split("}")[0] + "}"
        
    holdings = []
    total_value = 0.0
    
    # Loop through each security entry (infoTable node)
    for info_table in root.findall(f"{namespace}infoTable"):
        issuer_name = info_table.find(f"{namespace}nameOfIssuer").text
        cusip = info_table.find(f"{namespace}cusip").text
        value = float(info_table.find(f"{namespace}value").text) * 1000  # SEC values are reported in thousands
        
        shrs_node = info_table.find(f"{namespace}shrsOrPrnAmt")
        shares = int(float(shrs_node.find(f"{namespace}sshPrnAmt").text))
        
        # Fallback sector classification
        sector = "Financials" if "bank" in issuer_name.lower() or "corp" in issuer_name.lower() else "Information Technology"
        
        holdings.append({
            "company": issuer_name,
            "cusip": cusip,
            "shares": shares,
            "value_usd": value,
            "sector": sector
        })
        total_value += value
        
    # Map raw holdings to standard tickers (Mock mapping using standard identifiers for demo simplicity)
    ticker_map = {"AAPL": "Apple Inc.", "MSFT": "Microsoft Corp.", "AMZN": "Amazon.com Inc.", "NVDA": "NVIDIA Corp."}
    for h in holdings:
        h["ticker"] = "AAPL" if "apple" in h["company"].lower() else ("MSFT" if "micro" in h["company"].lower() else "UNKNOWN")
        
    return holdings, total_value

def generate_simple_dashboard(institution, holdings, total_val, date, limit=10):
    """Generate a clean terminal dashboard of the portfolio."""
    print("=" * 80)
    print(f"PORTFOLIO DASHBOARD: {institution.upper()}")
    print(f"SEC 13F Filing Date: {date} | Total Analyzed Equity Assets: ${total_val/1e6:.2f} Million")
    print("=" * 80)
    
    # Sort by value descending
    sorted_holdings = sorted(holdings, key=lambda x: x["value_usd"], reverse=True)
    
    print(f"{'Company Name':<35} | {'Shares':<12} | {'Value ($M)':<12} | {'Weight':<8}")
    print("-" * 80)
    for h in sorted_holdings[:limit]:
        weight = (h["value_usd"] / total_val) * 100
        print(f"{h['company'][:35]:<35} | {h['shares']:<12,} | ${h['value_usd']/1e6:<11.2f} | {weight:.2f}%")
    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="Institutional Intelligence Skills - Simple CLI Ingest Runner")
    parser.add_argument("institution", help="Company Name (e.g., 'Berkshire Hathaway') or Ticker")
    parser.add_argument("--limit", type=int, default=10, help="Number of holdings to display (default: 10)")
    args = parser.parse_args()
    
    print(f"Resolving CIK for '{args.institution}'...")
    cik = get_company_cik(args.institution)
    if not cik:
        print(f"Error: Could not resolve CIK for '{args.institution}'. Try using the exact company name or registered ticker.")
        sys.exit(1)
        
    print(f"Resolved CIK: {cik}")
    try:
        xml_content, filing_date = fetch_13f_filing_xml(cik)
        holdings, total_value = parse_13f_xml(xml_content)
        
        # Output clean terminal summary immediately
        generate_simple_dashboard(args.institution, holdings, total_value, filing_date, args.limit)
        
        # Save structured JSON file automatically so Claude can read it instantly
        filename = f"{args.institution.lower().replace(' ', '_')}_holdings.json"
        with open(filename, "w") as f:
            json.dump({
                "institution_name": args.institution,
                "reporting_period": filing_date,
                "holdings": holdings[:args.limit]
            }, f, indent=2)
        print(f"\n[Success] Structured holdings payload automatically saved to: {os.path.abspath(filename)}")
        print("You can now ask Claude: 'Analyze the portfolio in the saved JSON file'—no copy-paste required!")
        
    except Exception as e:
        print(f"Error during execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
