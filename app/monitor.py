
import time
import socket
from prometheus_client import start_http_server, Gauge, Counter

network_status = Gauge(
    "network_check_success",
    "Network availability",
    ["target"]
)

network_latency = Gauge(
    "network_latency_ms",
    "Connection latency in milliseconds",
    ["target"]
)

network_failures = Counter(
    "network_failures_total",
    "Total connection failures",
    ["target"]
)

TARGETS = [
    ("google.com", 443),
    ("cloudflare.com", 443),
    ("github.com", 443)
]

def check_network(host, port):
    try:
        start = time.perf_counter()

        with socket.create_connection(
            (host, port), timeout=3
        ):
            pass

        latency = (time.perf_counter() - start) * 1000

        network_status.labels(target=host).set(1)
        network_latency.labels(target=host).set(latency)

        print(f"{host}: ONLINE | {latency:.2f} ms")

    except OSError as error:
        network_status.labels(target=host).set(0)
        network_latency.labels(target=host).set(0)
        network_failures.labels(target=host).inc()

        print(f"{host}: OFFLINE | {error}")

if __name__ == "__main__":
    start_http_server(8000)

    print("Network Monitoring Started")

    while True:
        for host, port in TARGETS:
            check_network(host, port)

        time.sleep(10)
