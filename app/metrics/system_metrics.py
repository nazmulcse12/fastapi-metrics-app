import psutil
from prometheus_client import Gauge, CollectorRegistry, REGISTRY

# Global variables to store metrics
_metrics = {}

def _get_or_create_gauge(name, description):
    """Get existing gauge or create new one if it doesn't exist."""
    if name not in _metrics:
        try:
            _metrics[name] = Gauge(name, description)
        except ValueError:
            # Metric already exists in registry, find it
            for collector in REGISTRY._collector_to_names.keys():
                if hasattr(collector, '_name') and collector._name == name:
                    _metrics[name] = collector
                    break
    return _metrics[name]

def collect_system_metrics():
    # Get or create metrics
    cpu_usage_percent = _get_or_create_gauge("process_cpu_usage_percent", "CPU usage percent")
    memory_used = _get_or_create_gauge("process_resident_memory_bytes", "Physical memory currently used")
    virtual_memory = _get_or_create_gauge("process_virtual_memory_bytes", "Virtual memory allocated")
    process_start_time = _get_or_create_gauge("process_start_time_seconds", "Process start time in seconds since epoch")
    file_descriptors = _get_or_create_gauge("process_open_fds", "Number of open file descriptors")
    thread_count = _get_or_create_gauge("process_threads", "Number of threads")
    
    # Current process
    process = psutil.Process()
    
    # Collect metrics
    cpu_usage_percent.set(psutil.cpu_percent(interval=1))
    memory_used.set(process.memory_info().rss)
    virtual_memory.set(process.memory_info().vms)
    process_start_time.set(process.create_time())
    file_descriptors.set(process.num_fds())
    thread_count.set(process.num_threads())
