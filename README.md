# FastAPI Metrics Monitoring System

## Overview
A comprehensive FastAPI application with built-in Prometheus metrics collection for system and HTTP monitoring.

## Features
- System resource monitoring (CPU, memory, file descriptors, threads)
- HTTP request metrics (volume, latency, sizes)
- Prometheus metrics exposition
- Docker deployment ready

## Quick Start

### Using Docker Compose
```bash
docker-compose up -d --build
```

### Local Development
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Metrics Available

### System Metrics
- `process_cpu_usage_percent`: CPU usage percentage
- `process_resident_memory_bytes`: Physical memory usage
- `process_virtual_memory_bytes`: Virtual memory usage
- `process_start_time_seconds`: Process start time
- `process_open_fds`: Open file descriptors
- `process_threads`: Thread count

### HTTP Metrics
- `http_requests_total`: Total HTTP requests
- `http_request_duration_seconds`: Request latency histogram
- `http_request_size_bytes`: Request size histogram
- `http_response_size_bytes`: Response size histogram

## Endpoints
- `GET /`: Root endpoint
- `GET /health`: Health check
- `GET /metrics`: Prometheus metrics
- `GET /data`: Sample data endpoint
- `POST /data`: Sample data processing

## Prometheus Integration
Access Prometheus at http://localhost:9090 after running docker-compose.

## Example Queries
```promql
# 95th percentile latency
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{endpoint="/data",method="GET"}[5m])) by (le))

# Request rate
rate(http_requests_total[5m])
```
