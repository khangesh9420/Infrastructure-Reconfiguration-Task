
#  CI/CD Infrastructure Setup with Azure, Jenkins, Docker, SonarQube, Flask, and NGINX
The Project consists of setting up a complete CI/CD infrastructure using Azure virtual machines (VMs), Jenkins, Docker, SonarQube, and a Flask application.

---

## 1️⃣ Create Azure Virtual Machines

### VM1: Jenkins & Web/API Tools
- Use Azure to create a VM named `jenkins-CI`
- Install:
  - Jenkins (natively)
  - Java (required by Jenkins)
  - Docker (to run containers)
- This VM hosts:
  - Jenkins (Native tool for CI/CD)
  - SonarQube (as a container)
  - Flask API (as a container)
  - NGINX (as reverse proxy)

### VM2: Jenkins Build Agent
- Use Azure to create another VM named `azureagent`
- Connect this VM to Jenkins as a build agent
- Restrict **all public access** to this VM (only accessible internally)

---

## 2️⃣ Install Required Software on Jenkins VM

### Install Java
```bash
sudo apt update
sudo apt install openjdk-21-jdk -y
```

### Install Jenkins
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

### Install Docker
```bash
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
```

---

## 3️⃣ Run SonarQube in Docker
```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube
```

---

## 4️⃣ Flask Application

- A simple Flask app is created and Dockerized.

- Run Flask App:
```bash
docker build -t flask-App
docker run -d --name flask-App -p 5000:5000 flask-App
```

---

## 5️⃣ Configure NGINX for Reverse Proxy

**DNS used:**  
`jenkinsgui.westeurope.cloudapp.azure.com`
`sonarqube.westeurope.cloudapp.azure.com`
`api.westeurope.cloudapp.azure.com`

**Directory Structure:**
- Jenkins config: `/etc/nginx/jenkins/jenkins.conf`
- SonarQube config: `/etc/nginx/jenkins/sonarqube.conf`
- Flask API config: `/etc/nginx/jenkins/api.conf`

### Sample Configs

**jenkins.conf**
```nginx
location /jenkins/ {
    server {
    listen 80;
    server_name jenkins.jenkinsgui.westeurope.cloudapp.azure.com;

    location / {
        proxy_pass http://localhost:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
}
```

**sonarqube.conf**
```nginx
location /sonarqube/ {
    proxy_pass http://localhost:9000/;
    proxy_set_header Host $host;
}
```

**api.conf**
```nginx
location /api/ {
    proxy_pass http://localhost:5000/;
    proxy_set_header Host $host;
}
```

### Include these in the main NGINX config:
In `/etc/nginx/nginx.conf` or a site-enabled config:
```nginx
http {
    include /etc/nginx/jenkins/*.conf;
    ...
}
```

### Test and Start/Reload NGINX
```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

## 6️⃣ Configure SonarQube

- Access via `http://jenkinsgui.westeurope.cloudapp.azure.com/sonarqube/`
- Generate a token from your user profile
- Use the token in Jenkins SonarQube scanner setup to analyze your project

---
## 7 CI/CD pipeline

- Run CI/CD pipeline
- It consists of stages like checkout, Build, Test, Deploy 
- Use the manage credentials in jenkins for secure build process

---
## 8 Bottlenecks and Issue of the architecture

- Single Point of failure :The current Jenkins architecture is highly dependent on a single primary VM. If this VM experiences downtime or a failure, it could bring the entire CI/CD pipeline to a halt, affecting Jenkins, SonarQube, and hosted applications. This creates a critical risk to system availability and reliability.
- Manual Scaling: Static VMs for agents and services can’t scale efficiently.
- Configuration Drift:Manual setup of NGINX and virtual machines increases the risk of configuration drift. Without proper infrastructure automation, it becomes difficult to track who made changes, when they were made, or why — leading to inconsistencies and potential reliability or security issues
- No Monitoring or Logging for VMs :- Without proper monitoring: You can't detect when a VM is overloaded, down, or misbehaving, lack visibility into CPU, memory, disk, or network usage There are no logs collected, so troubleshooting is manual and reactive .

## 9 Architecture of current project
  <img width="638" alt="image" src="https://github.com/user-attachments/assets/6daf77c6-6ff4-4767-b259-072799ca0f47" />



