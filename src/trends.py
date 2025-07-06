from pytrends.request import TrendReq
import pandas as pd
import os
import time
import random
from datetime import datetime
from pytrends.exceptions import TooManyRequestsError

pytrends = TrendReq(hl='en-US', tz=330)

def fetch_trends(company, start_date, end_date, retries=3):
    kw_list = [company]
    timeframe = f"{start_date} {end_date}"

    for attempt in range(retries):
        try:
            pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')
            data = pytrends.interest_over_time()

            if data.empty:
                print(f"⚠️ No trend data for {company}")
                return

            data = data.drop(columns=['isPartial'])
            os.makedirs("data/trends", exist_ok=True)
            file_path = f"data/trends/{company.lower()}_trends.csv"
            data.to_csv(file_path)
            print(f"✅ Saved trend data to {file_path}")
            return

        except TooManyRequestsError:
            wait = random.randint(5, 15)
            print(f"⏳ Rate limited. Waiting {wait} seconds before retrying...")
            time.sleep(wait)
        except Exception as e:
            print(f"❌ Error fetching {company}: {e}")
            return

    print(f"❌ Failed to fetch trend data for {company} after {retries} retries.")

if __name__ == "__main__":
    companies = input("Enter company names (comma-separated):\n> ").split(",")
    companies = [c.strip() for c in companies if c.strip()]
    start_date = input("Enter start date (YYYY-MM-DD):\n> ")
    end_date = input("Enter end date (YYYY-MM-DD):\n> ")

    for company in companies:
        fetch_trends(company, start_date, end_date)
        delay = random.uniform(5, 10)
        print(f"🌙 Sleeping for {round(delay, 2)} seconds...\n")
        time.sleep(delay)
