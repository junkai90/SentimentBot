import streamlit as st
from sentimentbot.news_loader import load_news
from sentimentbot.sentiment_analyzer import analyze_sentiment
from sentimentbot.agent import create_agent

st.set_page_config(page_title="SentimentBot", page_icon="📰")

st.title("SentimentBot")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

# Load and analyze news on first load
if "news" not in st.session_state:
    news_items = load_news()
    st.session_state.news = analyze_sentiment(news_items)

st.header("Latest News")
for item in st.session_state.news:
    st.subheader(item.get("title", "Untitled"))
    st.write(item.get("content", ""))
    st.write("**Sentiment:**", item.get("sentiment", "Unknown"))

st.divider()

st.header("Ask SentimentBot")
user_input = st.text_input("Your question:")
if st.button("Send") and user_input:
    response = st.session_state.agent.invoke({"question": user_input})
    st.write(response["answer"])
    st.session_state.agent.memory.chat_memory.add_user_message(user_input)
    st.session_state.agent.memory.chat_memory.add_ai_message(response["answer"])
