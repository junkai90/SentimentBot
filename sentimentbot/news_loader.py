import json
from pathlib import Path
from typing import List, Dict

NEWS_FILE = Path(__file__).resolve().parent.parent / "data" / "news.json"

def load_news() -> List[Dict]:
    """Load news items from the local JSON database."""
    if NEWS_FILE.exists():
        with open(NEWS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
