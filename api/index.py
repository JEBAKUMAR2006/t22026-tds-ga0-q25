from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 124.11,
    "uptime_pct": 99.009,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 179.98,
    "uptime_pct": 97.852,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 190.88,
    "uptime_pct": 97.244,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 162.66,
    "uptime_pct": 98.849,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 215.39,
    "uptime_pct": 99.251,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 109.31,
    "uptime_pct": 98.611,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 166.72,
    "uptime_pct": 97.559,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 179.9,
    "uptime_pct": 99.006,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 158.02,
    "uptime_pct": 99.075,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 132.76,
    "uptime_pct": 99.034,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 129.05,
    "uptime_pct": 97.283,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 121.29,
    "uptime_pct": 99.209,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 202.57,
    "uptime_pct": 99.488,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 182.68,
    "uptime_pct": 97.698,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 157.43,
    "uptime_pct": 97.501,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 166.33,
    "uptime_pct": 98.988,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 111.01,
    "uptime_pct": 99.025,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 146.41,
    "uptime_pct": 97.474,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 114.78,
    "uptime_pct": 98.496,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 168.49,
    "uptime_pct": 97.974,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 177.08,
    "uptime_pct": 98.436,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 173.89,
    "uptime_pct": 99.362,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 104.63,
    "uptime_pct": 98.609,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 112.97,
    "uptime_pct": 97.28,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 198.87,
    "uptime_pct": 99.181,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 158.78,
    "uptime_pct": 98.326,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 121.16,
    "uptime_pct": 99.31,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 223.61,
    "uptime_pct": 99.119,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 160.5,
    "uptime_pct": 98.116,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 216.09,
    "uptime_pct": 97.361,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 129.52,
    "uptime_pct": 97.909,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 206.38,
    "uptime_pct": 98.482,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 214.99,
    "uptime_pct": 97.429,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 180.48,
    "uptime_pct": 98.569,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 187.8,
    "uptime_pct": 98.519,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 118.45,
    "uptime_pct": 97.957,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
