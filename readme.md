# 📈 Multimodal Stock Alpha Score Prediction Pipeline

A full end-to-end system that predicts **stock price movement** and lays the foundation for **alpha score generation** by combining multiple alternative data sources:

* 📰 News headlines
* 🧠 Reddit discussions
* 📊 Google Trends interest
* 📉 Historical stock prices

This project simulates a **quantitative sentiment-driven strategy** and prepares a structure for more advanced alpha-generating models used in real-world financial research and trading.

---

## 🔍 Overview

This pipeline:

* Scrapes relevant **news** and **Reddit posts** for selected companies
* Performs **sentiment analysis** using VADER (a lightweight rule-based model)
* Fetches **Google search trends** via PyTrends
* Downloads **stock prices** using Yahoo Finance
* Merges all data by date
* Trains a **baseline Linear Regression model** using sentiment + trend features
* Evaluates performance with **MSE** and prepares for future **alpha/backtest** integration

While current data size is limited, the pipeline architecture is fully functional and can be scaled to historical data for robust alpha prediction and Sharpe ratio analysis.

---

## 💠 Tech Stack

| Tool          | Purpose                  |
| ------------- | ------------------------ |
| Python        | Core programming         |
| NewsAPI       | News headline scraping   |
| Reddit PRAW   | Reddit post scraping     |
| PyTrends      | Google Trends extraction |
| yFinance      | Stock price download     |
| VADER         | Sentiment analysis       |
| Pandas, NumPy | Data processing          |
| scikit-learn  | ML model training        |

---

## 📂 Folder Structure

```
project/
 data/
  news/              # Raw news articles
  reddit/            # Reddit posts
  price/             # Yahoo Finance stock prices
  trends/            # Google Trends interest
  merged/            # Final merged dataset for modeling
Src/
 news.py
 reddit.py
 price.py
 trends.py
 vader_news_sentiment.py
 vader_reddit_sentiment.py
 merge_company_data.py
 train_baseline_model.py
 README.md
```

---

## 🔄 End-to-End Pipeline Flow

```
[NewsAPI + Reddit + Google Trends + yFinance]
        ↓
[Sentiment Analysis using VADER]
        ↓
[Daily Merging by Date]
        ↓
[Train ML Model (Sentiment + Trend → Stock Price)]
        ↓
[Foundation for Alpha Score Calculation]
```

---

## 📈 Model Objective: Predicting Alpha

> **Alpha** is the excess return of a stock relative to a benchmark (e.g., S\&P 500 or SPY ETF).

This project:

* Trains a baseline model to predict stock price movement from sentiment/trend signals
* Prepares the merged data for **daily return and alpha score computation**
* Sets the groundwork to calculate:

  * **Alpha** = $\text{Stock Return} - \text{Benchmark Return}$
  * **Sharpe Ratio**, **Directional Accuracy**, and more

---

## 📊 Example Features Used

* `news_sentiment`: daily VADER average from scraped news
* `reddit_sentiment`: daily VADER average from Reddit posts
* `Google Trends`: search interest for the company name
* `Close`: actual closing price (target)

---

## 🚀 How to Run the Project

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Fetch Raw Data

```bash
python news.py
python reddit.py
python price.py
python trends.py
```

### 3. Run Sentiment Analysis

```bash
python vader_news_sentiment.py
python vader_reddit_sentiment.py
```

### 4. Merge All Sources

```bash
python merge_company_data.py
```

### 5. Train Baseline Model

```bash
python train_baseline_model.py
```

---

## 📉 Limitations

* Current merged dataset is small (\~30–90 daily records), limiting training power.
* VADER is a rule-based sentiment tool; lacks domain-specific nuance.
* No direct benchmark comparison (e.g., SPY returns) yet for alpha calculation.

---

---

## 📌 Sample Resume Line

> Developed a multimodal sentiment-based alpha prediction pipeline using news, Reddit, Google Trends, and stock prices. Merged and modeled real-time data for financial signal generation. Built foundation for benchmark-based alpha scoring and backtesting.

---

## 📬 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/yourprofile) or check out my other finance projects on [GitHub](https://github.com/yourgithub).

---

## 📜 License

MIT License — free to use, adapt, and build on.

Copyright (c) 2025 HET PATEL
