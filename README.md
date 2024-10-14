# Python Flask Application with MySQL

This project is a Flask web application that connects to a MySQL database. The application creates a database named `test_database` if it does not already exist and responds with a "Hello, World!" message along with database connection status.


## Requirements

- Docker
- Docker Compose
- Python 3.9 or later
- MySQL 5.7
- Kubernetes (optional, for Helm chart deployment)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/mhagi00/python-app

cd python-app
```
## Set Up the Environment

### 1. Build and Run the Application with Docker Compose:

```bash
docker-compose up --build
```

### 2. Access the Application:

Open your web browser and go to http://localhost:8080. You should see a message that includes "Hello, World!" and the database connection status.

## Deploying to Kubernetes (Optional)

### 1. Install Helm (if not already installed):

Follow the instructions at [Helm Installation ](https://helm.sh/docs/intro/install/)to install Helm.

### 2. Deploy the Application using Helm:

Navigate to the `helm-chart` directory:
```bash
cd helm-chart
```
Install the Helm chart:
```bash
helm install python-app .
```
### 3. Verify the Deployment:
After deploying, you can check the status of your pods with:

```bash
kubectl get pods
```

## Pre-commit Hooks
To ensure code quality, this project uses pre-commit for linting and formatting.

## CI/CD

This project includes a GitHub Actions CI workflow defined in .github/workflows/ci.yaml, which runs pre-commit hooks on every push and pull request.