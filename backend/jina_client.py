import requests
from typing import List, Optional

class JinaAIReader:
    """Client for parsing web content with JinaAI Reader"""

    def __init__(self):
        self.base_url = "https://r.jina.ai"

    def read_url(self, url: str) -> Optional[str]:
        """
        Parse URL content using JinaAI Reader

        Args:
            url: URL to parse

        Returns:
            Cleaned text content or None on error
        """
        try:
            jina_url = f"{self.base_url}/{url}"
            headers = {
                "X-Return-Format": "text"
            }

            response = requests.get(jina_url, headers=headers, timeout=30)
            response.raise_for_status()

            # Return first 5000 chars to minimize tokens
            content = response.text.strip()
            return content[:5000] if len(content) > 5000 else content

        except Exception as e:
            print(f"JinaAI error for {url}: {e}")
            return None
