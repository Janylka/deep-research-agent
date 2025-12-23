# Deep Research Agent - Architecture

## Purpose
AI-powered research agent that automatically searches, analyzes, and synthesizes information from multiple web sources into comprehensive reports.

## Tools & APIs

### 1. SerpAPI
- **Purpose**: Web search to find relevant sources
- **Usage**: Retrieves top 5 search results for any query
- **Output**: URLs, titles, and snippets

### 2. JinaAI Reader
- **Purpose**: Parse and clean web content
- **Usage**: Converts HTML to clean text (max 5000 chars per source)
- **URL**: `https://r.jina.ai/{url}`

### 3. Claude AI (Anthropic)
- **Haiku**: Fast summarization (5-7 bullets per source)
- **Sonnet**: Deep analysis for final report generation

### 4. Context7 Cache
- **Purpose**: Store source summaries to prevent reprocessing
- **Storage**: Local JSON file (`context7_cache.json`)
- **Benefit**: Saves API calls and tokens on repeated queries

## Workflow Pipeline

```
User Query
    ↓
1. SerpAPI Search (max 5 results)
    ↓
2. For each URL:
   - Check Context7 cache
   - If not cached: JinaAI Reader → parse content
   - Claude Haiku → summarize to 5-7 bullets
   - Store in Context7 cache
    ↓
3. All summaries collected
    ↓
4. Claude Sonnet → generate final report
    ↓
Output: {search_results, sources, report}
```

## Token Optimization Rules

### ❌ Never Store:
- Raw HTML content
- Full webpage text
- Large unprocessed data

### ✅ Always Store:
- Compressed summaries only (5-7 bullets)
- Maximum 5 sources per query
- Cached summaries (prevent reprocessing)

### Optimization Strategies:
1. **Immediate Compression**: JinaAI content → 5000 chars max → 5-7 bullets
2. **Cache First**: Check Context7 before processing
3. **Limit Sources**: Hard cap at 5 results
4. **Small Model First**: Use Haiku for summaries (cheaper, faster)
5. **Sonnet for Reports**: Only use larger model for final synthesis

## API Endpoints

### POST `/research`
```json
Request:
{
  "query": "quantum computing applications"
}

Response:
{
  "query": "quantum computing applications",
  "search_results": [...],
  "sources": [
    {
      "title": "...",
      "url": "...",
      "snippet": "...",
      "summary": ["- bullet 1", "- bullet 2", ...]
    }
  ],
  "report": "# Executive Summary\n..."
}
```

### GET `/cache/clear`
Clears the Context7 cache.

## Performance Metrics

- **Search**: ~1-2s (SerpAPI)
- **Parse per source**: ~2-4s (JinaAI)
- **Summarize per source**: ~3-5s (Claude Haiku)
- **Final report**: ~5-10s (Claude Sonnet)
- **Total**: ~30-60s for 5 sources

## Error Handling

- Failed JinaAI parse: Skip source, continue with others
- API rate limits: Caught and logged
- Cache corruption: Rebuilds from empty cache
- No results: Returns empty report with message

## Security

- API keys in `.env` file (not committed)
- CORS enabled for frontend
- No user data stored (only URL summaries in cache)

## Future Enhancements

- [ ] Parallel source processing
- [ ] Streaming responses
- [ ] PDF export
- [ ] Citation tracking
- [ ] Multi-language support
