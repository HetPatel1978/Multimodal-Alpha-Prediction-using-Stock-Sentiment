import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# === Init VADER ===
vader = SentimentIntensityAnalyzer()

# === Input Directory ===
NEWS_DIR = "data/news"

# === Apply Sentiment ===
def analyze_news_sentiment(file_path):
    df = pd.read_csv(file_path)
    
    # Handle missing columns
    if 'title' not in df.columns:
        df['title'] = ''
    if 'summary' not in df.columns:
        if 'description' in df.columns:
            df['summary'] = df['description']
        else:
            df['summary'] = ''
    
    # Combine text
    df['full_text'] = df['title'].fillna('') + '. ' + df['summary'].fillna('')
    
    # Compute sentiment
    sentiments = df['full_text'].apply(vader.polarity_scores)
    sentiment_df = pd.DataFrame(sentiments.tolist())

    df = pd.concat([df, sentiment_df], axis=1)
    df.to_csv(file_path.replace(".csv", "_vader.csv"), index=False)
    print(f"✅ Processed: {file_path}")

# === Process All News Files ===
for file in os.listdir(NEWS_DIR):
    if file.endswith(".csv"):
        analyze_news_sentiment(os.path.join(NEWS_DIR, file))
