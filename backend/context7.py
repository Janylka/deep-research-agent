import json
import os
from typing import Dict, Optional
from datetime import datetime

class Context7Cache:
    """
    Lightweight cache for storing summaries of processed sources.
    Prevents reprocessing and minimizes token usage.
    """

    def __init__(self, cache_file: str = "context7_cache.json"):
        self.cache_file = cache_file
        self.cache: Dict[str, dict] = self._load_cache()

    def _load_cache(self) -> Dict[str, dict]:
        """Load cache from file"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_cache(self):
        """Save cache to file"""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving cache: {e}")

    def get(self, url: str) -> Optional[dict]:
        """Get cached summary for URL"""
        return self.cache.get(url)

    def set(self, url: str, summary: list, title: str = ""):
        """Cache summary for URL"""
        self.cache[url] = {
            "title": title,
            "summary": summary,
            "cached_at": datetime.now().isoformat()
        }
        self._save_cache()

    def exists(self, url: str) -> bool:
        """Check if URL is cached"""
        return url in self.cache

    def clear(self):
        """Clear all cache"""
        self.cache = {}
        self._save_cache()
