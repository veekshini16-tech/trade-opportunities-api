
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from app.services.news_service import get_sector_news
from app.services.analysis_service import generate_analysis
from app.core.rate_limit import RateLimiter
from app.core.sessions import SessionTracker

app = FastAPI(title="Trade Opportunities API V2")

security = HTTPBearer()
rate_limiter = RateLimiter(10, 60)
sessions = SessionTracker()

class ReportResponse(BaseModel):
    sector: str
    report_markdown: str

def auth(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != "demo-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/analyze/{sector}", response_model=ReportResponse)
async def analyze(sector: str, request: Request, token: str = Depends(auth)):

    client = request.client.host

    if not rate_limiter.allow(client):
        raise HTTPException(status_code=429, detail="Too many requests")

    sessions.track(client)

    news = get_sector_news(sector)
    analysis = generate_analysis(sector, news)

    report = f"""
# Market Trade Opportunities Report

## Sector
{sector}

## Recent Market News
{news}

## AI Market Analysis
{analysis}

## Possible Trade Strategies
- Identify companies with strong earnings
- Watch government policy announcements
- Track export demand trends
"""

    return {"sector": sector, "report_markdown": report}
