# Visitor Counter Cloud
### Kubernetes Deployment, Hybrid Cloud Simulation & Cost Optimization

**Python · Flask · Redis · Docker · Kubernetes · Minikube · HPA**

---

## Project Details

| Detail | Information |
|---|---|
| Project Name | Visitor Counter Cloud |
| Student Name | Abhay Shakya |
| Roll Number | 2410031084 |
| Course | B.Tech CSE Core |
| Section | 3CSE23 |
| Subject | Cloud Computing |
| Application | Flask + Redis |
| Deployment Platform | Docker & Kubernetes |
| Cloud Simulation | Private and Public Minikube Clusters |

## 1. Project Overview

**Visitor Counter Cloud** is a cloud-native web application designed to count website visitors using Python Flask and Redis.

The application is first containerized using Docker and Docker Compose. It is then deployed on Kubernetes, where multiple Flask application pods handle incoming requests while Redis provides centralized visitor count storage.

The project demonstrates important cloud computing concepts, including containerization, orchestration, workload management, self-healing, horizontal autoscaling, resource monitoring, and hybrid-cloud deployment.

A hybrid-cloud environment is simulated using two independent Minikube clusters representing private and public cloud environments. The application is deployed on both clusters, and manual failover is demonstrated by stopping the private cluster and accessing the application through the public cluster.

The project also explores cost-conscious infrastructure management through lightweight Docker images, Kubernetes resource requests and limits, and automatic scaling.

## 2. Problem Statement

Traditional web applications may experience performance problems when incoming traffic increases. Deploying and maintaining multiple application instances manually can also increase operational complexity and resource consumption.

A scalable application requires a deployment environment that can:

- Handle multiple incoming user requests.
- Maintain application availability when an application instance fails.
- Automatically adjust the number of application instances according to workload.
- Monitor and manage CPU and memory consumption.
- Support deployment across separate cloud environments.
- Use infrastructure resources efficiently.

This project addresses these challenges by developing a Flask and Redis application and deploying it using Docker and Kubernetes.

## 3. Project Objectives

1. Develop a visitor counter web application using Flask and Redis.
2. Containerize the application using Docker.
3. Use Docker Compose to manage Flask and Redis services.
4. Deploy the application using Kubernetes Deployments and Services.
5. Configure multiple Flask application replicas.
6. Implement Kubernetes self-healing and health probes.
7. Configure Horizontal Pod Autoscaling with a CPU target of 50%.
8. Perform load testing to observe automatic scaling.
9. Monitor Kubernetes resource consumption.
10. Simulate private and public cloud environments using two Minikube clusters.
11. Demonstrate manual failover between the simulated environments.
12. Apply Docker image and Kubernetes resource optimization techniques.

## 4. System Architecture

### 4.1 Application Architecture

The application follows a simple three-layer architecture:

- **User layer:** A browser sends requests to the visitor counter application.
- **Application layer:** Flask processes requests and updates the visitor count.
- **Storage layer:** Redis stores the visitor count and provides fast in-memory access.

In the Kubernetes environment, the Flask application runs through multiple pods. A Kubernetes Service distributes incoming requests across the available application pods.

### 4.2 Autoscaling Architecture

The Horizontal Pod Autoscaler monitors CPU utilization using metrics provided by Kubernetes Metrics Server.

When CPU utilization increases beyond the configured target, Kubernetes increases the number of Flask replicas. When the workload decreases, the HPA can reduce the number of replicas.

### 4.3 Hybrid-Cloud Architecture

Two independent Minikube clusters are used:

- `visitor-private` represents the private cloud.
- `visitor-public` represents the public cloud simulation.

Both environments contain their own Flask and Redis deployments. The public environment is used to demonstrate manual failover when the private environment is stopped.

See [Architecture Diagram](documentation/architecture.md).

## 5. How the Application Works

1. The user opens the visitor counter website.
2. The Flask application receives the HTTP request.
3. Flask increments the visitor count stored in Redis.
4. Redis returns the updated count.
5. Flask displays the updated visitor count.
6. Kubernetes Services route requests to available Flask pods.
7. Kubernetes maintains the desired number of application replicas.
8. Metrics Server collects CPU and memory usage information.
9. HPA adjusts the number of Flask replicas according to CPU utilization.

The application also provides health-check endpoints:

| Endpoint | Purpose |
|---|---|
| `/` | Displays the visitor counter |
| `/health` | Checks application and Redis connectivity |
| `/live` | Provides application liveness status |

## 6. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming |
| Flask | Web application framework |
| Redis | Visitor count storage |
| Gunicorn | Production WSGI server |
| Docker | Application containerization |
| Docker Compose | Multi-container application management |
| Kubernetes | Container orchestration |
| Minikube | Local Kubernetes cluster simulation |
| kubectl | Kubernetes resource management |
| Metrics Server | CPU and memory metrics |
| Horizontal Pod Autoscaler | Automatic application scaling |
| YAML | Infrastructure configuration |
| Git & GitHub | Version control and project hosting |

## 7. Project Structure

```text
visitor-counter-cloud/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
│
├── k8s.yaml
├── hpa.yaml
│
├── load-testing/
│   └── load-generator.yaml
│
├── documentation/
│   └── architecture.md
│
├── screenshots/
│   ├── docker-images.png
│   ├── docker-visitor-counter.png
│   ├── kubernetes-pods-running.png
│   ├── self-healing-pod-replacement.png
│   ├── hpa-baseline.png
│   ├── hpa-scale-up.png
│   ├── hpa-six-replicas.png
│   ├── hpa-scale-down.png
│   ├── hybrid-cloud-private-stopped.png
│   ├── public-cloud-website.png
│   └── resource-optimization.png
│
└── README.md
```

## 8. Features and Implementation

### 8.1 Visitor Counter Application

The web application is developed using Flask, while Redis is used as the data storage layer.

Features include:

- Visitor count increases when the homepage is accessed.
- Redis stores the visitor count.
- Flask communicates with Redis to retrieve and update the count.
- Health-check endpoints monitor application availability and Redis connectivity.

### 8.2 Docker Containerization

The application is packaged into a Docker image using a custom Dockerfile.

Implementation includes:

- Python 3.12 slim base image.
- Installation of required Python packages.
- Gunicorn application server.
- Non-root container user.
- Docker health check.
- Lightweight Redis Alpine image.
- Docker Compose configuration for running both services.

The Flask image was measured at **47.4 MB content size**.

### 8.3 Kubernetes Deployment

The application is deployed using Kubernetes resources defined in `k8s.yaml`.

The deployment contains:

- Flask Deployment with 2 initial replicas.
- Redis Deployment with 1 replica.
- Flask ClusterIP Service.
- Redis ClusterIP Service.
- Persistent Volume Claim for Redis storage.
- CPU and memory requests and limits.
- Startup, readiness, and liveness probes.

#### Kubernetes resource configuration

| Resource | Configuration |
|---|---|
| Flask initial replicas | 2 |
| Redis replicas | 1 |
| Flask CPU request | 100m |
| Flask CPU limit | 500m |
| Flask memory request | 96Mi |
| Flask memory limit | 256Mi |
| Redis storage claim | 1Gi |
| Flask application port | 5000 |
| Redis port | 6379 |

### 8.4 Kubernetes Self-Healing

Kubernetes automatically maintains the desired number of application replicas.

To demonstrate self-healing, a running Flask pod was manually deleted.

Kubernetes detected the missing replica and automatically created a replacement pod through its Deployment and ReplicaSet controllers.

**Observed result:** The deleted pod was replaced successfully, and the application returned to its desired state of 2 running Flask replicas.

**Evidence:** `screenshots/self-healing-pod-replacement.png`

### 8.5 Horizontal Pod Autoscaling

Horizontal Pod Autoscaler adjusts the number of Flask application pods according to CPU utilization.

#### HPA configuration

| Configuration | Value |
|---|---|
| Minimum replicas | 2 |
| Maximum replicas | 6 |
| CPU target utilization | 50% |
| Scaling metric | CPU utilization |
| Target deployment | visitor-counter |

A load generator was deployed inside Kubernetes to generate concurrent HTTP requests against the application.

#### Load-testing results

During a recorded load test:

| Metric | Observed result |
|---|---:|
| Completed requests | 33,150 |
| Successful requests | 33,150 |
| Failed requests | 0 |
| Maximum observed Flask replicas | 6 |
| Initial Flask replicas | 2 |
| Final scaled-down replicas | 2 |

During the test, CPU utilization increased above the configured target and HPA scaled the application from 2 to 6 replicas.

After the load stopped, CPU utilization decreased and the application eventually scaled back to 2 replicas.

**Evidence:**
- `screenshots/hpa-baseline.png`
- `screenshots/hpa-scale-up.png`
- `screenshots/hpa-six-replicas.png`
- `screenshots/hpa-scale-down.png`

### 8.6 Resource Monitoring

Kubernetes Metrics Server was enabled to collect CPU and memory usage information.

Resource consumption was inspected using Kubernetes monitoring commands such as:

```bash
kubectl top nodes
kubectl top pods -n visitor-counter
```

The Flask application and load generator have configured CPU and memory requests and limits.

During private-cluster observation, the following application pod usage was recorded:

| Component | CPU usage | Memory usage |
|---|---:|---:|
| Flask pod 1 | 5m | 77Mi |
| Flask pod 2 | 4m | 78Mi |
| Redis pod | 8m | 9Mi |

These values represent an observed snapshot, not fixed resource requirements.

**Evidence:** `screenshots/resource-optimization.png`

### 8.7 Hybrid-Cloud Simulation

The project uses two independent Minikube clusters to represent private and public cloud environments.

| Environment | Minikube profile |
|---|---|
| Private cloud simulation | `visitor-private` |
| Public cloud simulation | `visitor-public` |

Both clusters were configured with Flask and Redis deployments.

Each environment contains:

- 2 Flask application replicas.
- 1 Redis replica.
- Kubernetes Deployments.
- Kubernetes Services.

#### Manual failover demonstration

1. The application was deployed on the private cluster.
2. A second Minikube cluster was created to represent the public environment.
3. The application was deployed and tested on the public cluster.
4. The private cluster was stopped.
5. The application was accessed through the public cluster.

**Observed result:** The public cluster continued serving the application while the private cluster was stopped.

**Important limitation:** This is a manual failover simulation. Automatic cross-cluster failover, automated traffic routing, a global load balancer, and Redis data replication between clusters are not implemented.

Both clusters run locally using Minikube; no actual AWS, Azure, or Google Cloud infrastructure is used.

**Evidence:**
- `screenshots/hybrid-cloud-private-stopped.png`
- `screenshots/public-cloud-website.png`

## 9. Cost and Resource Optimization

The project demonstrates three infrastructure optimization techniques.

### 9.1 Docker Image Optimization

The Flask application uses the `python:3.12-slim` base image instead of a full Python base image.

This avoids unnecessary packages and helps reduce the container image footprint.

| Image | Measured content size |
|---|---:|
| Flask optimized image (`visitor-counter:slim`) | 47.4 MB |

The optimized image was built and used for the Docker and Kubernetes deployments.

**Measurement limitation:** A full Python baseline image was not built and measured in this project. Therefore, no percentage reduction is claimed.

### 9.2 Horizontal Pod Autoscaling

The HPA is configured to maintain between 2 and 6 Flask replicas with a CPU utilization target of 50%.

During high demand, replicas increased from 2 to 6. After the workload decreased, the application scaled back to 2 replicas.

This avoids keeping the maximum number of application replicas running when demand is lower.

### 9.3 Kubernetes Resource Requests and Limits

CPU and memory requests and limits were configured for application containers.

| Resource | Flask configuration |
|---|---:|
| CPU request | 100m |
| Memory request | 96Mi |
| CPU limit | 500m |
| Memory limit | 256Mi |

These settings help define the application's resource requirements and constrain container resource consumption.

**Measurement limitation:** No before-and-after cloud billing comparison or verified percentage reduction in resource requests was performed. Actual monetary savings have not been measured because the deployment uses local Minikube clusters.

## 10. Project Results

The implementation successfully demonstrates:

- Flask and Redis visitor counter application.
- Docker containerization and Docker Compose deployment.
- Kubernetes deployment with separate Flask and Redis components.
- Two Flask application replicas.
- Kubernetes self-healing through pod replacement.
- HPA scaling from 2 to 6 replicas.
- HPA scale-down from 6 to 2 replicas.
- CPU and memory monitoring.
- 33,150 successful load-test requests with zero reported failures.
- Lightweight Flask Docker image with 47.4 MB content size.
- Hybrid-cloud simulation using two independent Minikube clusters.
- Manual failover demonstration using the public cluster.

## 11. Screenshots and Evidence

All screenshots documenting the implementation are stored in the `screenshots/` directory.

| Screenshot | Demonstration |
|---|---|
| `docker-visitor-counter.png` | Local visitor counter website |
| `docker-images.png` | Docker image information |
| `kubernetes-pods-running.png` | Kubernetes application and Redis pods |
| `self-healing-pod-replacement.png` | Automatic pod replacement |
| `hpa-baseline.png` | Initial HPA status |
| `hpa-scale-up.png` | HPA scaling under load |
| `hpa-six-replicas.png` | Six running application replicas |
| `hpa-scale-down.png` | HPA scale-down after load |
| `resource-optimization.png` | Kubernetes resource configuration and usage |
| `hybrid-cloud-private-stopped.png` | Private cluster stopped |
| `public-cloud-website.png` | Application running through public cluster simulation |

## 12. Running the Project Locally

### Prerequisites

Install the following tools:

- Docker Desktop
- Docker Compose
- Minikube
- kubectl

### Step 1: Clone the repository

```bash
git clone https://github.com/Abhay-Shakya-Code/visitor-counter-cloud.git
cd visitor-counter-cloud
```

### Step 2: Run using Docker Compose

```bash
docker compose up --build -d
```

### Step 3: Open the application

Open the following URL in your browser:

```text
http://localhost:5001
```

### Step 4: Check container status

```bash
docker compose ps
```

### Step 5: Stop the application

```bash
docker compose down
```

## 13. Kubernetes Deployment

The following example deploys the application to a private Minikube cluster.

### Step 1: Build the application image

```bash
docker build -t visitor-counter:slim .
```

### Step 2: Start the private cluster

```bash
minikube start -p visitor-private --driver=docker --cpus=2 --memory=2500 --disk-size=20g
```

### Step 3: Load the application image

```bash
minikube image load visitor-counter:slim -p visitor-private
```

### Step 4: Enable Metrics Server

```bash
minikube addons enable metrics-server -p visitor-private
```

### Step 5: Deploy Kubernetes resources

```bash
kubectl --context=visitor-private apply -f k8s.yaml
```

### Step 6: Configure autoscaling

```bash
kubectl --context=visitor-private apply -f hpa.yaml
```

### Step 7: Check pods

```bash
kubectl --context=visitor-private get pods -n visitor-counter
```

### Step 8: Check services

```bash
kubectl --context=visitor-private get services -n visitor-counter
```

### Step 9: Check HPA

```bash
kubectl --context=visitor-private get hpa -n visitor-counter
```

### Step 10: Access the application

```bash
kubectl --context=visitor-private port-forward -n visitor-counter svc/visitor-counter 8080:80
```

Open:

```text
http://localhost:8080
```

**Note:** These commands describe a fresh private-cluster deployment. The load generator can be started separately using `kubectl --context=visitor-private apply -f load-testing/load-generator.yaml`. For the public simulation, create and configure the separate `visitor-public` profile and deploy the same Kubernetes resources there.

## 14. Monitoring Commands

### View CPU and memory usage

```bash
kubectl top pods -n visitor-counter
```

### View deployments

```bash
kubectl get deployments -n visitor-counter
```

### View HPA status

```bash
kubectl get hpa -n visitor-counter
```

### View services

```bash
kubectl get services -n visitor-counter
```

### View cluster nodes

```bash
kubectl get nodes
```

## 15. Limitations

- Both cloud environments are simulated using local Minikube clusters.
- No actual AWS, Azure, or Google Cloud infrastructure is used.
- Automatic cross-cluster failover is not implemented.
- Traffic routing between clusters is performed manually.
- Redis data is not replicated between the two clusters.
- Actual cloud billing savings have not been measured.
- Docker image reduction against a full Python baseline has not been measured.
- HPA testing and its recorded scaling evidence are from the private cluster.

## 16. Future Scope

The project can be extended through:

1. Deployment on actual AWS, Azure, or Google Cloud infrastructure.
2. Automated failover using cloud load balancers and health-based routing.
3. Cross-cluster traffic management.
4. Redis replication and data synchronization between environments.
5. Persistent and highly available Redis storage.
6. Prometheus and Grafana for advanced monitoring.
7. CI/CD automation using GitHub Actions.
8. Centralized logging and alerting.
9. Cloud billing analysis and actual cost comparisons.
10. Security enhancements using HTTPS, authentication, and secrets management.

## 17. Conclusion

The Visitor Counter Cloud project demonstrates the practical implementation of a cloud-native web application using Flask, Redis, Docker, and Kubernetes.

It covers containerization, application deployment, service communication, self-healing, horizontal autoscaling, resource monitoring, and hybrid-cloud simulation.

The successful load-testing and scaling demonstrations show how Kubernetes can manage application workloads dynamically. The two-cluster deployment further demonstrates the concept of running an application across separate cloud environments and manually switching access when one environment is unavailable.

Overall, this project provides practical exposure to container orchestration, cloud-native deployment, workload management, and infrastructure optimization.

---

## Author

**Abhay Shakya**

B.Tech CSE Core  
Section: 3CSE23  
Roll Number: 2410031084

**GitHub Repository:**  
https://github.com/Abhay-Shakya-Code/visitor-counter-cloud

**Project:** Visitor Counter Cloud  
**Subject:** Cloud Computing
