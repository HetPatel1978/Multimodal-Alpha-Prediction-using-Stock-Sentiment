import pandas as pd
import os

def merge_company_data(company_name: str):
    company = company_name.lower()
    print(f"📊 Merging data for: {company_name.title()}")

    # Define paths
    price_path   = f"data/price/{company}_price.csv"
    news_path    = f"data/news/{company}_news_vader.csv"
    reddit_path  = f"data/reddit/{company}_reddit_vader.csv"
    trends_path  = f"data/trends/{company}_trends.csv"

    try:
        # Load price data and format date
        df_price = pd.read_csv(price_path)
        df_price["date"] = pd.to_datetime(df_price["Date"]).dt.date
        df_price = df_price.drop(columns=["Date"])  # remove original 'Date' column

        # Load and preprocess news data
        df_news = pd.read_csv(news_path)
        df_news["timestamp"] = pd.to_datetime(df_news["timestamp"], utc=True)
        df_news["date"] = df_news["timestamp"].dt.date
        df_news_grouped = df_news.groupby("date")["compound"].mean().reset_index().rename(columns={"compound": "news_sentiment"})

        # Load and preprocess Reddit data
        df_reddit = pd.read_csv(reddit_path)
        df_reddit["created_utc"] = pd.to_datetime(df_reddit["created_utc"], utc=True)
        df_reddit["date"] = df_reddit["created_utc"].dt.date
        df_reddit_grouped = df_reddit.groupby("date")["compound"].mean().reset_index().rename(columns={"compound": "reddit_sentiment"})

        # Load Google Trends
        df_trends = pd.read_csv(trends_path)
        df_trends["date"] = pd.to_datetime(df_trends["date"]).dt.date

    except FileNotFoundError as e:
        print(f"❌ Missing file for {company}: {e.filename}")
        return
    except Exception as e:
        print(f"❌ Column error in one of the CSVs: {e}")
        return

    print("✅ All data loaded and preprocessed.")

    # Merge step-by-step
    df_merged = df_price.copy()
    df_merged = df_merged.merge(df_news_grouped, on="date", how="left")
    df_merged = df_merged.merge(df_reddit_grouped, on="date", how="left")
    df_merged = df_merged.merge(df_trends, on="date", how="left")

    # Save merged data
    os.makedirs("data/merged", exist_ok=True)
    output_path = f"data/merged/{company}_merged.csv"
    df_merged.to_csv(output_path, index=False)
    print(f"✅ Merged data saved to: {output_path}")

# === Run interactively ===
if __name__ == "__main__":
    company = input("Enter company name (e.g. Apple, Nvidia):\n> ").strip()
    merge_company_data(company)
