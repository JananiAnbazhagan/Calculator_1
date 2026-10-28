# Student Grade Calculator - CI/CD Pipeline Lab

This repository is ready to fulfill the 5-stage deployment pipeline using VS Code, Git, GitHub Actions, Docker Hub, and Kubernetes.

## How to follow the 2-Push constraint:

### 1️⃣ Push 1 Setup (Total & Average only)
1. Open `app.py` and comment out or remove the Grade logic inside the calculation block.
2. Open `templates/index.html` and comment out the `{% if result.grade %}` block.
3. Commit and push this to GitHub. This triggers your initial pipeline build and maps version 1 to Kubernetes.

### 2️⃣ Push 2 Setup (Grade Feature Addition)
1. Re-introduce the Grade logic back into `app.py` and `templates/index.html`.
2. Commit and push this next increment. The Github Workflow file will automatically rebuild the container image using the updated unique git reference commit (`${{ github.sha }}`) and refresh the active cluster deployment without downtime!
