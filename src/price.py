import yfinance as yf
import os
import pandas as pd
from datetime import datetime

# Optional mapping
TICKER_MAP = {
    "Nvidia": "NVDA",
    "Apple": "AAPL",
    "Meta": "META",
    "Tesla": "TSLA",
    "Amazon": "AMZN",
    "Microsoft": "MSFT",
    "Google": "GOOGL"
}

def fetch_stock_data(company, start_date, end_date):
    print(f"📈 Fetching price data for: {company}")
    ticker = TICKER_MAP.get(company, company)

    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            print(f"⚠️ No data found for {company}")
            return

        data.reset_index(inplace=True)
        data["Date"] = data["Date"].dt.strftime("%Y-%m-%d")

        os.makedirs("data/price", exist_ok=True)
        file_path = f"data/price/{company.lower()}_price.csv"
        data.to_csv(file_path, index=False)
        print(f"✅ Saved {len(data)} rows to {file_path}")
    except Exception as e:
        print(f"❌ Failed to fetch data for {company}: {e}")

if __name__ == "__main__":
    companies = input("Enter company names (comma-separated):\n> ").split(",")
    companies = [c.strip() for c in companies if c.strip()]

    start_date = input("Enter start date (YYYY-MM-DD):\n> ")
    end_date = input("Enter end date (YYYY-MM-DD):\n> ")

    for company in companies:
        fetch_stock_data(company, start_date, end_date)
