# NEXUS – Network Monitoring & Incident Detection System

A real-time network monitoring solution built using Python, Prometheus, Grafana, and Docker Compose.

## Project Overview

NEXUS monitors network endpoint availability and latency, collects metrics, and visualizes network health through a Grafana Network Operations Center (NOC) dashboard.

## Architecture

- **Python Exporter:** Performs TCP connectivity checks and exposes Prometheus metrics.
- **Prometheus:** Scrapes metrics and evaluates alert rules.
- **Grafana:** Provides a real-time NOC dashboard.
- **Docker Compose:** Runs and manages all project services.

## Features

- Real-time endpoint availability monitoring
- Network latency monitoring
- Online and offline target detection
- Network failure counters
- Critical and warning alert rules
- Grafana NOC dashboard
- Docker-based deployment

## Technologies Used

Python, Prometheus, Grafana, Docker, Docker Compose, PromQL, YAML.

## Project Structure

```text
network-monitoring/
├── app/
│   ├── monitor.py
│   ├── requirements.txt
│   └── Dockerfile
├── prometheus/
│   ├── prometheus.yml
│   └── rules/
│       └── alerts.yml
├── grafana/
│   └── provisioning/
│       ├── datasources/
│       │   └── prometheus.yml
│       └── dashboards/
│           ├── dashboard.yml
│           └── nexus-noc.json
├── screenshots/
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Run Locally

Requirements: Docker Desktop and Docker Compose.

```bash
git clone YOUR_REPOSITORY_URL
cd network-monitoring
docker compose up -d --build
```

## Access Services

| Service | URL |
|---|---|
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |
| Python Exporter | http://localhost:8000/metrics |

## Prometheus Metrics

- `network_check_success`
- `network_latency_ms`
- `network_failures_total`

## Alert Rules

- NetworkTargetDown – critical alert when a target is unreachable.
- HighNetworkLatency – warning alert when latency exceeds 500 ms.
- MultipleTargetsDown – include if configured in your final alert rules.

## Testing

The project was tested by introducing a temporary unreachable network target and verifying offline detection and critical alert visibility in Grafana.

## Dashboard

The NEXUS dashboard provides endpoint status, availability, latency, active alerts, critical alerts, and network performance visualizations.

## Future Enhancements

- Email and notification integrations
- More network endpoints
- Historical performance analysis
- Network device monitoring through SNMP

## Author

Simran