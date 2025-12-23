import os
from typing import List, Dict
# Toggle between real and mock SerpAPI:
# from serp_client import SerpAPIClient  # Real SerpAPI
from serp_mock import MockSerpAPIClient as SerpAPIClient  # Mock for testing
from jina_client import JinaAIReader
from context7 import Context7Cache
import anthropic

class DeepResearchAgent:
    """
    Deep Research Agent with token optimization

    Pipeline:
    1. User Query → SerpAPI (top 5 results)
    2. URLs → JinaAI Reader (parse content)
    3. Content → Claude (summarize to 5-7 bullets per source)
    4. Summaries → Claude (generate final report)
    """

    def __init__(self, serp_api_key: str, anthropic_api_key: str):
        self.serp_client = SerpAPIClient(serp_api_key)
        self.jina_reader = JinaAIReader()
        self.cache = Context7Cache()
        self.claude = anthropic.Anthropic(api_key=anthropic_api_key)
        self.max_sources = 5

    def _summarize_source(self, content: str, title: str, url: str) -> List[str]:
        """Summarize source to 5-7 bullet points"""
        try:
            prompt = f"""Summarize this content into exactly 5-7 concise bullet points.
Each bullet should be a single line, maximum 15 words.
Focus on key facts and insights only.

Title: {title}
Content: {content}

Return ONLY the bullet points, one per line, starting with '- '."""

            message = self.claude.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )

            summary_text = message.content[0].text
            bullets = [line.strip() for line in summary_text.split('\n') if line.strip().startswith('-')]

            return bullets[:7]  # Ensure max 7 bullets

        except Exception as e:
            print(f"Summarization error for {url}: {e}")
            return [f"- Error summarizing content: {str(e)[:50]}"]

    def _generate_report(self, query: str, sources: List[Dict]) -> str:
        """Generate final research report from summaries"""
        try:
            sources_text = ""
            for i, source in enumerate(sources, 1):
                sources_text += f"\n\n**Source {i}: {source['title']}**\n"
                sources_text += f"URL: {source['url']}\n"
                for bullet in source['summary']:
                    sources_text += f"{bullet}\n"

            prompt = f"""You are a research analyst. Create a comprehensive report based on these sources.

Research Query: {query}

Sources:{sources_text}

Generate a well-structured report with:
1. Executive Summary (2-3 sentences)
2. Key Findings (organized by theme)
3. Conclusion

Be concise, factual, and cite sources as [1], [2], etc."""

            message = self.claude.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )

            return message.content[0].text

        except Exception as e:
            print(f"Report generation error: {e}")
            return f"Error generating report: {str(e)}"

    def research(self, query: str) -> Dict:
        """
        Execute deep research pipeline

        Returns:
            Dict with search_results, sources (with summaries), and final_report
        """
        print(f"🔍 Starting research: {query}")

        # Step 1: Search with SerpAPI
        print("📡 Searching with SerpAPI...")
        search_results = self.serp_client.search(query, max_results=self.max_sources)

        if not search_results:
            return {
                "query": query,
                "search_results": [],
                "sources": [],
                "report": "No search results found."
            }

        # Step 2: Parse and summarize each source
        print(f"📚 Processing {len(search_results)} sources...")
        sources = []

        for idx, result in enumerate(search_results, 1):
            url = result['url']
            title = result['title']

            print(f"  [{idx}/{len(search_results)}] Processing: {title[:50]}...")

            # Check cache first
            if self.cache.exists(url):
                print(f"    ✓ Using cached summary")
                cached = self.cache.get(url)
                sources.append({
                    "title": title,
                    "url": url,
                    "snippet": result['snippet'],
                    "summary": cached['summary']
                })
                continue

            # Parse with JinaAI
            content = self.jina_reader.read_url(url)
            if not content:
                print(f"    ✗ Failed to parse")
                continue

            # Summarize with Claude
            summary = self._summarize_source(content, title, url)

            # Cache summary
            self.cache.set(url, summary, title)

            sources.append({
                "title": title,
                "url": url,
                "snippet": result['snippet'],
                "summary": summary
            })

            print(f"    ✓ Summarized to {len(summary)} bullets")

        # Step 3: Generate final report
        print("📝 Generating final report...")
        report = self._generate_report(query, sources)

        print("✅ Research complete!")

        return {
            "query": query,
            "search_results": search_results,
            "sources": sources,
            "report": report
        }
