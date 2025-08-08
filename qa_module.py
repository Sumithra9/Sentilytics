import os
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

import streamlit as st
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama3-70b-8192")

def ask_groq(query, feedback_list):
    joined_feedback = "\n".join(feedback_list[:200])  # Limit size
    prompt = f"You are analyzing customer feedback. Here is the feedback:\n\n{joined_feedback}\n\nUser's question: {query}"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that answers questions based on customer feedback."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 800
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"


def generate_summary(feedback_list):
    full_text = " ".join(feedback_list)[:8000]
    prompt = f"Summarize the following customer feedback in a few paragraphs:\n\n{full_text}"
    response = llm.invoke(prompt)
    return response.content

def generate_swot(feedback_list):
    full_text = " ".join(feedback_list)[:8000]
    prompt = f"Generate a SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) from the following customer feedback:\n\n{full_text}"
    response = llm.invoke(prompt)
    return response.content

