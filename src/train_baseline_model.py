import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import warnings

warnings.filterwarnings("ignore")

def train_model_for_company(file_path, company_name):
    print(f"\n📊 Training model for: {company_name.title()}")

    try:
        df = pd.read_csv(file_path, parse_dates=["date"])
    except Exception as e:
        print(f"❌ Could not read {company_name} file: {e}")
        return

    # Drop rows with any missing values
    df_clean = df.dropna()

    if df_clean.empty:
        print(f"❌ No complete data to train on for {company_name}")
        return

    print(f"✅ Using {len(df_clean)} clean rows")

    # Dynamically find the trends column (case-insensitive match)
    trend_column = None
    for col in df_clean.columns:
        if col.lower() == company_name.lower():
            trend_column = col
            break

    if not trend_column:
        print(f"❌ Trend column for {company_name} not found in file.")
        return

    # Feature and target selection
    feature_cols = ['news_sentiment', 'reddit_sentiment', trend_column]
    target_col = 'Close'

    try:
        X = df_clean[feature_cols]
        y = df_clean[target_col]

        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)
        mse = mean_squared_error(y, y_pred)

        print(f"📈 MSE for {company_name.title()}: {mse:.4f}")
    except Exception as e:
        print(f"❌ Error training {company_name}: {e}")

if __name__ == "__main__":
    print("🚀 Running Baseline Model for All Companies...")

    companies = {
        "apple": "data/merged/apple_merged.csv",
        "meta": "data/merged/meta_merged.csv",
        "nvidia": "data/merged/nvidia_merged.csv"
    }

    for name, path in companies.items():
        if os.path.exists(path):
            train_model_for_company(path, name)
        else:
            print(f"❌ File not found: {path}")
