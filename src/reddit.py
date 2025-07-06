import praw
import os
import pandas as pd
from datetime import datetime
from time import sleep

# === Your Reddit API Credentials ===
REDDIT_CLIENT_ID = "ErL9C.................."  # 🔒 Replace with your actual Reddit client ID
REDDIT_CLIENT_SECRET = "dOZf8w-2o.........."   # 🔒 Replace with your actual Reddit client secret
REDDIT_USERNAME = "Swimm......."  # Your Reddit username
REDDIT_PASSWORD = "........."  # 🔒 Replace with your actual Reddit password
REDDIT_USER_AGENT = "........"  # A user agent string for your application

# === Optional company → ticker mapping ===
TICKER_MAP = {
    "Nvidia": "NVDA",
    "Apple": "AAPL",
    "Meta": "META",
    "Tesla": "TSLA",
    "Amazon": "AMZN",
    "Microsoft": "MSFT",
    "Google": "GOOGL"
}

# === Reddit API Initialization ===
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

# === Main Scraping Function ===
def scrape_reddit(company, start_date, end_date, max_posts=100):
    print(f"🔍 Scraping Reddit for: {company}")
    query = f"${TICKER_MAP.get(company, company)}"

    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    posts = []
    for submission in reddit.subreddit("all").search(query, sort="relevance", time_filter="month", limit=max_posts):
        post_date = datetime.fromtimestamp(submission.created_utc)
        if start_dt <= post_date <= end_dt:
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "score": submission.score,
                "created_utc": post_date.strftime("%Y-%m-%d %H:%M:%S"),
                "url": submission.url
            })

    if not posts:
        print(f"⚠️ No posts found for {company}")
        return

    os.makedirs("data/reddit", exist_ok=True)
    file_path = f"data/reddit/{company.lower()}_reddit.csv"
    pd.DataFrame(posts).to_csv(file_path, index=False)
    print(f"✅ Saved {len(posts)} posts to {file_path}")

# === Input Runner ===
if __name__ == "__main__":
    companies = input("Enter company names (comma-separated):\n> ").split(",")
    companies = [c.strip() for c in companies if c.strip()]

    start_date = input("Enter start date (YYYY-MM-DD):\n> ")
    end_date = input("Enter end date (YYYY-MM-DD):\n> ")
    max_posts = int(input("Enter max posts per company (e.g. 100):\n> "))

    for company in companies:
        scrape_reddit(company, start_date, end_date, max_posts)
        sleep(1)  # Reddit API rate limit protection
