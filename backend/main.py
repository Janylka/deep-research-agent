import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from agent import DeepResearchAgent

# Load environment variables
load_dotenv()

app = FastAPI(title="Deep Research Agent API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agent
SERP_API_KEY = os.getenv("SERP_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not SERP_API_KEY or not ANTHROPIC_API_KEY:
    raise ValueError("Missing API keys. Set SERP_API_KEY and ANTHROPIC_API_KEY in .env file")

agent = DeepResearchAgent(SERP_API_KEY, ANTHROPIC_API_KEY)


class ResearchRequest(BaseModel):
    query: str


class ResearchResponse(BaseModel):
    query: str
    search_results: list
    sources: list
    report: str


@app.get("/")
def read_root():
    return {
        "service": "Deep Research Agent",
        "status": "running",
        "version": "1.0.0"
    }


@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):
    """Execute deep research on a query"""
    if not request.query or len(request.query.strip()) < 3:
        raise HTTPException(status_code=400, detail="Query must be at least 3 characters")

    try:
        result = agent.research(request.query.strip())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Research failed: {str(e)}")


@app.get("/cache/clear")
def clear_cache():
    """Clear the Context7 cache"""
    try:
        agent.cache.clear()
        return {"status": "success", "message": "Cache cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to clear cache: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
