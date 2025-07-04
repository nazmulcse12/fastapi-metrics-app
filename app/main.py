import asyncio
from app.metrics.system_metrics import collect_system_metrics
from fastapi import FastAPI
from prometheus_client import make_asgi_app
from app.routers import api, health
from app.middleware.metrics_middleware import MetricsMiddleware

app = FastAPI()

app.add_middleware(MetricsMiddleware)

app.include_router(api.router)
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "FastAPI Metrics App is running"}

# Background task to collect system metrics
@app.on_event("startup")
async def start_system_metrics():
    async def collect():
        while True:
            collect_system_metrics()
            await asyncio.sleep(5)  # collect every 5 seconds
    asyncio.create_task(collect())

# Mount /metrics
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
