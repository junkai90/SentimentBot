from __future__ import annotations

from pathlib import Path
from typing import List, Dict

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS

from .news_loader import load_news


def build_vectorstore(news_items: List[Dict]) -> FAISS:
    """Create a vector store from news items."""
    texts = [item.get("content", "") for item in news_items]
    meta = [{"title": item.get("title", "")} for item in news_items]
    embeddings = OllamaEmbeddings(model="mistral")
    vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=meta)
    return vectorstore


def create_agent() -> ConversationalRetrievalChain:
    news_items = load_news()
    vectorstore = build_vectorstore(news_items)

    llm = Ollama(model="mistral")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return chain
