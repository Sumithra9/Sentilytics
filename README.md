# 📊 Sentilytics: Comprehensive Feedback Analyzer

Sentilytics is an **AI-powered feedback analysis tool** that transforms raw customer feedback into **actionable insights** using **Sentiment Analysis, Summarization, SWOT Analysis, WordCloud visualization, and LLM-powered QnA**.

---

## 🚀 Features

- **Sentiment Analysis** – Classifies feedback into Positive, Negative, or Neutral using NLP.
- **Summarization** – Generates concise summaries from bulk feedback.
- **SWOT Analysis** – Extracts Strengths, Weaknesses, Opportunities, and Threats from customer input.
- **WordCloud Generation** – Visualizes the most common words in feedback.
- **LLM-Powered QnA** – Ask natural language questions about feedback and get AI-driven answers.
- **Sentiment Distribution Graphs** – Visual representation of feedback sentiment trends.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **NLP:** TextBlob, HuggingFace Transformers
- **Visualization:** Matplotlib, WordCloud
- **LLM API:** Groq (LLaMA 3)
- **Others:** dotenv for environment variables

---

## 📦 Installation



1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Sentilytics.git
cd contractgenie
pip install -r requirements.txt

```
2.**Create and activate a virtual environment**
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3.**Install dependencies**
```bash
pip install -r requirements.txt
```
4.**Set your Groq API key**
```bash
GROQ_API_KEY="your-groq-api-key-here"
```
5. **Run Streamlit App**
```bash
streamlit run app.py
```

