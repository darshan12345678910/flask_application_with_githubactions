# Flask Application with GitHub Actions CI/CD

This project is a Dockerized Flask application that performs basic calculations. The app includes a CI/CD pipeline set up with GitHub Actions to automatically build, test, and push a Docker image to Docker Hub on each push or pull request to the main branch.

## Features
- Simple calculator app with addition, subtraction, multiplication, and division functions.
- Dockerized setup for easy deployment.
- CI/CD pipeline with GitHub Actions to ensure continuous integration and delivery.

## Prerequisites

1. **Docker**: Ensure Docker is installed and running on your machine.
2. **GitHub Account**: Required for GitHub Actions setup.
3. **Docker Hub Account**: Required to store the Docker image.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/flask_application_with_githubactions.git
   cd flask_application_with_githubactions

2. **Install Dependencies** (Optional for local testing):
   - If you want to run the application locally without Docker, you can install the dependencies with:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application Locally**:
   - You can start the Flask app by running:
     ```bash
     python app.py
     ```
   - The application should be accessible at `http://localhost:5000`.

4. **Run Tests Locally**:
   - To ensure everything is working correctly, run the tests:
     ```bash
     pytest
     ```

## Docker Usage

1. **Build the Docker Image**:
   ```bash
   docker build -t flasktest-app .
# CI/CD Pipeline with GitHub Actions

The `.github/workflows/main.yml` file defines the CI/CD pipeline, which is triggered on pushes and pull requests to the `main` branch.

## Workflow Jobs

### 1. `build_and_test`
- **Description**: Checks out the repository, sets up Python, installs dependencies, and runs unit tests to verify the application's functionality.
- **Steps**:
  - Checks out the repository code.
  - Sets up a Python environment.
  - Installs project dependencies from `requirements.txt`.
  - Runs unit tests using `pytest` to ensure code correctness.

### 2. `build_and_push_docker`
- **Description**: Builds and pushes the Docker image to Docker Hub. Requires Docker Hub credentials to be securely stored as GitHub secrets.
- **Steps**:
  - Builds the Docker image.
  - Logs in to Docker Hub.
  - Pushes the Docker image to your Docker Hub repository.

## Setting Up GitHub Secrets

To allow GitHub Actions to authenticate with Docker Hub, you need to set up secrets in your GitHub repository.

1. Go to your repository on GitHub.
2. Navigate to **Settings** > **Secrets** > **Actions**.
3. Add the following secrets:
   - **DOCKER_HUB_USERNAME**: Your Docker Hub username.
   - **DOCKER_HUB_PASSWORD**: Your Docker Hub password.

## Triggering the Workflow

The CI/CD pipeline is triggered automatically in the following scenarios:
- When you **push** changes to the `main` branch.
- When you **open a pull request** targeting the `main` branch.

This setup ensures that the application is tested and deployed seamlessly, providing continuous integration and delivery.
   

   
