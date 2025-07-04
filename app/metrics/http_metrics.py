from prometheus_client import Histogram

# Missing HTTP metrics
request_size_histogram = Histogram(
    "http_request_size_bytes",
    "HTTP request size in bytes",
    ["method", "endpoint"]
)

response_size_histogram = Histogram(
    "http_response_size_bytes", 
    "HTTP response size in bytes",
    ["method", "endpoint"]
)