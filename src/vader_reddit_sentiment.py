
import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

vader = SentimentIntensityAnalyzer()
REDDIT_DIR = "data/reddit"

def analyze_reddit_sentiment(file_path):
    df = pd.read_csv(file_path)
    df['full_text'] = df['title'].fillna('') + '. ' + df['selftext'].fillna('')
    sentiments = df['full_text'].apply(vader.polarity_scores)
    sentiment_df = pd.DataFrame(sentiments.tolist())

    df = pd.concat([df, sentiment_df], axis=1)
    df.to_csv(file_path.replace(".csv", "_vader.csv"), index=False)
    print(f"✅ Processed: {file_path}")

for file in os.listdir(REDDIT_DIR):
    if file.endswith(".csv"):
        analyze_reddit_sentiment(os.path.join(REDDIT_DIR, file))
