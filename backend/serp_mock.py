from typing import List, Dict

class MockSerpAPIClient:
    """Mock client for testing without SerpAPI key"""

    def __init__(self, api_key: str = "mock"):
        self.api_key = api_key

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Return mock search results for testing

        Args:
            query: Search query
            max_results: Maximum number of results (default 5)

        Returns:
            List of dicts with 'title', 'url', 'snippet'
        """
        print(f"[MOCK MODE] Simulating search for: {query}")

        # Mock search results based on query
        mock_results = [
            {
                "title": f"Article about {query} - Wikipedia",
                "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
                "snippet": f"Comprehensive information about {query} including history, applications, and future developments."
            },
            {
                "title": f"{query}: Complete Guide (2024)",
                "url": "https://www.ibm.com/topics/artificial-intelligence",
                "snippet": f"Learn everything about {query} with our detailed guide covering fundamentals and advanced concepts."
            },
            {
                "title": f"Latest Research on {query}",
                "url": "https://arxiv.org/list/cs.AI/recent",
                "snippet": f"Recent scientific papers and research findings about {query} from leading institutions."
            },
            {
                "title": f"{query} Applications and Use Cases",
                "url": "https://www.mckinsey.com/capabilities/quantumblack/our-insights",
                "snippet": f"Real-world applications of {query} in business, healthcare, and technology sectors."
            },
            {
                "title": f"Future of {query} - Expert Analysis",
                "url": "https://www.wired.com/tag/artificial-intelligence/",
                "snippet": f"Expert perspectives on the future trends and developments in {query} technology."
            }
        ]

        return mock_results[:max_results]
