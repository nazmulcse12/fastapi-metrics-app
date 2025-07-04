from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import Counter, Histogram
from app.metrics.http_metrics import request_size_histogram, response_size_histogram
import time

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency (seconds)",
    ["method", "endpoint"]
)

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        method = request.method
        path = request.url.path

        # Track request size
        request_size = int(request.headers.get("content-length", 0))
        request_size_histogram.labels(method, path).observe(request_size)

        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        status_code = response.status_code

        # Track response size
        response_size = len(response.body) if hasattr(response, 'body') else 0
        response_size_histogram.labels(method, path).observe(response_size)

        REQUEST_COUNT.labels(method, path, status_code).inc()
        REQUEST_LATENCY.labels(method, path).observe(duration)

        return response
