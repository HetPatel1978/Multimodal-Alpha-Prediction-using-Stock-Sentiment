import os
import pandas as pd
from newsapi import NewsApiClient
from datetime import datetime

# ==== Setup ====
API_KEY = "6af2a108237448349fc5473a532b9d47"  # Replace with your key
newsapi = NewsApiClient(api_key=API_KEY)
output_dir = "data/news"
os.makedirs(output_dir, exist_ok=True)

# ==== User Input ====
companies_input = input("Enter company names (comma-separated):\n> ")
companies = [c.strip() for c in companies_input.split(",") if c.strip()]

from_date = input("Enter start date (YYYY-MM-DD):\n> ").strip()
to_date = input("Enter end date (YYYY-MM-DD):\n> ").strip()

# Validate date format
try:
    datetime.strptime(from_date, "%Y-%m-%d")
    datetime.strptime(to_date, "%Y-%m-%d")
except ValueError:
    print("❌ Error: Date format must be YYYY-MM-DD.")
    exit(1)

# ==== Scraper Function ====
def scrape_company_news(company, from_date, to_date, page_limit=5):
    all_articles = []
    query = f"{company} stock"
    print(f"\n🔍 Scraping news for: {company}")

    for page in range(1, page_limit + 1):
        response = newsapi.get_everything(
            q=query,
            language="en",
            sort_by="relevancy",
            from_param=from_date,
            to=to_date,
            page=page,
            page_size=10,
        )
        for article in response.get("articles", []):
            all_articles.append([
                article["publishedAt"],
                article["title"],
                article["description"],
                company
            ])

    df = pd.DataFrame(all_articles, columns=["timestamp", "title", "description", "company"])
    filename = f"{output_dir}/{company.lower().replace(' ', '_')}_news.csv"
    df.to_csv(filename, index=False)
    print(f"✅ {len(df)} headlines saved → {filename}")

# ==== Main Loop ====
for company in companies:
    scrape_company_news(company, from_date, to_date)
