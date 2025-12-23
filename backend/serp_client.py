import os
from typing import List, Dict
from serpapi import GoogleSearch

class SerpAPIClient:
    """Client for searching with SerpAPI"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Search using SerpAPI and return top results

        Args:
            query: Search query
            max_results: Maximum number of results (default 5)

        Returns:
            List of dicts with 'title', 'url', 'snippet'
        """
        params = {
            "q": query,
            "api_key": self.api_key,
            "num": max_results,
            "engine": "google"
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()

            organic_results = results.get("organic_results", [])

            output = []
            for result in organic_results[:max_results]:
                output.append({
                    "title": result.get("title", ""),
                    "url": result.get("link", ""),
                    "snippet": result.get("snippet", "")
                })

            return output
        except Exception as e:
            print(f"SerpAPI error: {e}")
            return []
