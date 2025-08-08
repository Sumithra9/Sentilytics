import streamlit as st
import pandas as pd
from feedback_parser import parse_feedback_and_analyze_sentiment, generate_wordcloud, plot_sentiment_distribution
from qa_module import ask_groq, generate_summary, generate_swot
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="📊 Customer Feedback Analyzer", layout="wide")
st.title("📊 Customer Feedback Analyzer with Groq QnA")

uploaded_file = st.file_uploader("Upload an Excel or CSV file with customer feedback", type=["xlsx", "csv"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success("File uploaded successfully!")

    df, sentiment_counts = parse_feedback_and_analyze_sentiment(tmp_path)
    st.subheader("Feedback Table with Sentiment")
    st.dataframe(df)

    st.subheader("📊 Sentiment Distribution")
    plot_sentiment_distribution(sentiment_counts)

    st.subheader("☁️ Word Cloud")
    generate_wordcloud(df)

    st.subheader("🧠 AI-Generated Insights")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📄 Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = generate_summary(df["feedback"].tolist())
            st.markdown("**Summary:**")
            st.write(summary)

    with col2:
        if st.button("📌 Generate SWOT Analysis"):
            with st.spinner("Analyzing feedback for SWOT..."):
                swot = generate_swot(df["feedback"].tolist())
            st.markdown("**SWOT Analysis:**")
            st.write(swot)

    st.subheader("💬 Ask a question about the feedback")
    user_query = st.text_input("Enter your question")
    if user_query:
        with st.spinner("Generating answer from Groq..."):
            answer = ask_groq(user_query, df["feedback"].tolist())
        st.success("Answer:")
        st.write(answer)
