# SentimentBot

SentimentBot is a simple AI agent that analyzes news about the energy market and evaluates potential impacts on oil prices and other energy commodities.

The app is built with Python using **LangChain** and **Streamlit**. It reads news articles from a local database (a JSON file), assigns sentiment scores using the Mistral model served via **Ollama**, stores article embeddings in a vector store, and keeps conversational memory so users can ask questions about the processed news.

## Setup

1. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

2. Ensure [Ollama](https://ollama.ai) is installed locally and that the `mistral` model is available:

```bash
ollama pull mistral
```

3. Run the Streamlit app:

```bash
streamlit run sentimentbot/main.py
```

## Usage

The dashboard displays loaded news articles along with their sentiment scores. Use the chat box to ask questions such as:

```
Based on the news you read today, do you think there is an impact on the oil price?
```

SentimentBot will reference the stored news and respond using the Mistral language model.
