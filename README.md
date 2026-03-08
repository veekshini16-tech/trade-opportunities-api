
# Trade Opportunities API (FastAPI)

## Setup

Install dependencies:

pip install -r requirements.txt

Run server:

python -m uvicorn app.main:app --reload

## Endpoint

GET /analyze/{sector}

Example:
http://127.0.0.1:8000/analyze/technology

## Authorization Header

Authorization: Bearer demo-token
