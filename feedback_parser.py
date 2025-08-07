import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

def get_sentiment(text):
    try:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"
    except:
        return "Neutral"

def parse_feedback_and_analyze_sentiment(file_path):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    if "feedback" not in df.columns:
        raise ValueError("Excel must have a 'feedback' column")

    df["feedback"] = df["feedback"].astype(str)
    df["sentiment"] = df["feedback"].apply(get_sentiment)
    sentiment_counts = df["sentiment"].value_counts().to_dict()
    return df, sentiment_counts

def plot_sentiment_distribution(sentiment_counts):
    fig, ax = plt.subplots(figsize=(4, 4))  # Smaller size
    labels = sentiment_counts.keys()
    sizes = sentiment_counts.values()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig, use_container_width=False)  # Prevent full width stretch


def generate_wordcloud(df):

    text = " ".join(df["feedback"].tolist())
    wordcloud = WordCloud(width=500, height=250, background_color="white").generate(text)

    fig, ax = plt.subplots(figsize=(6, 3))  # Smaller size
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig, use_container_width=False)  # Don't auto-stretch

