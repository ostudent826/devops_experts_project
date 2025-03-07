# Project Requirements for Windows Users
This document outlines all the resources and tools required to run the code in this project on Windows.

## **1. Prerequisite Check**
First, check which components you already have installed:

```cmd
wsl --version
python --version
git --version
mysql --version
docker --version
kubectl version --client
helm version
java --version
```

Skip installation steps for any tools that are already correctly installed.

---
## **2. Chocolatey (Required for new installations only)**
- **Purpose**: For managing dependencies like Python, Git, MySQL, Docker, Kubernetes, Helm, and Java.

### **Installation** (Skip if already installed)
1. Open a command prompt as Administrator.
2. Run the following command:
   ```cmd
   @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
   ```
3. Verify installation:
   ```cmd
   choco --version
   ```

---



### **Required Versions**
- Python 3.11 or newer
- Git (latest version)
- MySQL 8.0 or newer
- Docker Desktop with Kubernetes support
- kubectl compatible with your Kubernetes version
- Helm 3.x
- OpenJDK 17.0.13 or newer (Temurin distribution)


## **3.1 Install Missing Dependencies Using Chocolatey**
### **Individual Installation Commands**
Install only what you need:

*For wsl you need install it manually - https://www.youtube.com/watch?app=desktop&v=7KVdJ43dQmE*

```cmd
# For Python (3.11+)
choco install python -y

# For Git
choco install git -y

# For Docker Desktop
choco install docker-desktop -y

# For Kubernetes CLI
choco install minikube -y

# For Helm
choco install kubernetes-helm -y

# For Java (OpenJDK 17)
choco install temurin17 -y

# For MySQL
choco install mysql -y
***Ignore the red output***
```






## **3.2 Setup mySQL server**

mysql --version
if not regocnized restart localmachine

mysql setup
```cmd
mysql -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';

FLUSH PRIVILEGES;

EXIT;
```
## **3.3 Docker-Desktop need open manually to start the engine at the very first time **

---




---



---
## **6. Jenkins Installation**
- **Purpose**: CI/CD pipeline management.

### **Using Helm**
After ensuring Kubernetes is running:

```cmd
helm install jenkins https://raw.githubusercontent.com/ostudent826/devops_experts_project/main/jenkins-5.8.3.tgz -f values.yaml
```

Note: Make sure you have the values.yaml file in your current directory.

---
## **7. Final Checklist**
- [ ] All required dependencies are installed and working
- [ ] Docker Desktop is running with Kubernetes enabled
- [ ] MySQL is properly configured and accessible
- [ ] Jenkins is deployed on your Kubernetes cluster
- [ ] All services are verified operational with version checks

---
This document ensures you have all the tools and dependencies needed to run the project successfully on Windows, while avoiding unnecessary reinstallation of components you already have.
