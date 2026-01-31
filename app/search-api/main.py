from fastapi import FastAPI, Query
from datetime import datetime
import logging
import os

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
def search(q: str = Query(..., min_length=1)):
    environment = os.getenv("ENVIRONMENT", "dev")

    logger.info(f"[{environment}] Search request | query={q}")

    results = [
        {"id": 1, "title": f"{q} result one"},
        {"id": 2, "title": f"{q} result two"},
        {"id": 3, "title": f"{q} result three"},
    ]

    return {
        "env": environment,  
        "query": q,
        "count": len(results),
        "results": results,
        "cd_test": "deployed via github actions",
        "timestamp": datetime.utcnow()
    }

