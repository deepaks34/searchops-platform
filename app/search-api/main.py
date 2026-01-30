from fastapi import FastAPI, Query
from datetime import datetime
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("search-api")

app = FastAPI(title="SearchOps API")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "search-api",
        "timestamp": datetime.utcnow()
    }


@app.get("/search")
def search(
    q: str = Query(..., min_length=1, description="Search query")
):
    logger.info(f"Search request received | query={q}")

    # Simulated search results
    results = [
        {"id": 1, "title": f"{q} result one"},
        {"id": 2, "title": f"{q} result two"},
        {"id": 3, "title": f"{q} result three"},
    ]

    return {
        "query": q,
        "count": len(results),
        "results": results,
        "timestamp": datetime.utcnow()
    }

