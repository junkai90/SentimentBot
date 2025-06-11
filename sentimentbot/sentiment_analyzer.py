from __future__ import annotations

from typing import List, Dict

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

SENTIMENT_PROMPT = PromptTemplate.from_template(
    """
You are a financial analyst specializing in energy markets. Assess the sentiment of the following news article.
Return ONLY a sentiment label (Positive, Negative, or Neutral) followed by a short justification.

News: {text}
"""
)


def analyze_sentiment(news_items: List[Dict]) -> List[Dict]:
    """Analyze sentiment for a list of news items using Mistral via Ollama."""
    llm = Ollama(model="mistral")
    results = []
    for item in news_items:
        prompt = SENTIMENT_PROMPT.format(text=item.get("content", ""))
        sentiment = llm.invoke(prompt)
        results.append({**item, "sentiment": sentiment.strip()})
    return results
