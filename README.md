# Visitor Counter Web Application

## Project Overview
A Flask and Redis based Visitor Counter deployed using Docker and Kubernetes. The project demonstrates containerization, orchestration, self-healing, autoscaling, hybrid-cloud simulation and resource optimization.

## Technologies Used
- Python Flask
- Redis
- Docker and Docker Compose
- Kubernetes and Minikube
- Horizontal Pod Autoscaler

## Project Structure
- app.py: Flask application
- requirements.txt: Python dependencies
- Dockerfile: Container configuration
- docker-compose.yml: Docker Compose configuration
- k8s.yaml: Kubernetes deployments and services
- hpa.yaml: Autoscaling configuration
- load-testing/: Load testing configuration
- documentation/: Project documentation
- screenshots/: Project evidence

## Deployment Features

### Docker
Flask and Redis run as separate containers using Docker Compose.

### Kubernetes
- Flask deployment with 2 initial replicas.
- Redis deployment with persistent storage.
- Kubernetes Services.
- CPU and memory requests and limits.
- Readiness and liveness probes.

### Self-Healing
Kubernetes automatically replaced a deleted Flask pod.

### Horizontal Pod Autoscaling
- Minimum replicas: 2
- Maximum replicas: 6
- Target CPU utilization: 50%
- Demonstrated scaling from 2 to 6 and back to 2 replicas.

### Hybrid Cloud Simulation
Two Minikube clusters represent private and public cloud environments. The application was deployed on both. The private cluster was stopped while the application remained accessible on the public cluster.

This is a manual failover simulation, not automated production failover.

### Cost Optimization
1. Lightweight Docker image using python:3.12-slim (47.4 MB content size).
2. Resource requests and limits: CPU 100m/500m, memory 96Mi/256Mi.
3. HPA reduces replicas from 6 to 2 when workload decreases.

These are local resource optimizations, not measured cloud billing savings.

## Test Results
- Docker deployment successful.
- Kubernetes pods reached Running state.
- Self-healing verified.
- HPA scaling verified.
- Public cluster remained accessible with private cluster stopped.

## Future Scope
- Deployment on actual cloud infrastructure.
- Automated cross-cluster failover.
- Prometheus and Grafana monitoring.
- CI/CD integration.

## Conclusion
The project demonstrates containerization, orchestration, autoscaling, self-healing and hybrid-cloud simulation using Flask, Redis, Docker and Kubernetes.
