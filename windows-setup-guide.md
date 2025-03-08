# Project Requirements for Windows Users
This document outlines all the resources and tools required to run the code in this project on Windows.

## **1. Prerequisite Check**
First, check which components you already have installed:

```cmd
python --version
git --version
helm version
java --version
docker --version
minikube --version
mysql --version
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
- Helm 3.x
- OpenJDK 17.0.13 or newer (Temurin distribution)
- Docker-Desktop
- minikube
- MySQL 8.0 or newer


## **3.1 Install Missing Dependencies Using Chocolatey**
### **Individual Installation Commands**
Install only what you need:


```cmd
# For Python (3.11+)
choco install python -y

# For Git
choco install git -y

# For Helm
choco install kubernetes-helm -y

# For Java (OpenJDK 17)
choco install temurin17 -y

# For Docker Desktop
choco install docker-desktop -y

# For Kubernetes CLI
choco install minikube -y

# For MySQL
choco install mysql -y
***Ignore the red output***
```




## **3.2 Setup Docker-Desktop **

Docker-desktop need to be open manually to start the engine at the very first time
*after restart you need to start it again or allow it open at startup

## **3.3 Setup minikube **
*minikube is running on docker-desktop make sure it running
```cmd
minikube start
```

## **3.4 Setup mySQL server**

mysql --version
if not regocnized restart localmachine

mysql setup
```cmd
mysql -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';

FLUSH PRIVILEGES;

EXIT;
```

## **6. Jenkins Installation**
- **Purpose**: CI/CD pipeline management.

prerequest :
make a new dir in windows - C:/jenkins-win-agent

### **6.1 deply jenkins machine via helm**
After ensuring Kubernetes is running:

```cmd
helm install jenkins https://raw.githubusercontent.com/ostudent826/devops_experts_project/main/jenkins-5.8.3.tgz

kubectl get pods -w (check pods initilize)
```
connect the jenkins server using minikube tunnel 
do not close the terminal after the command
```cmd
minikube service ofri-custom-jenkins 
```
###6.2 connect the jenkins via u&p**

username: admin
password: admin

*the pipeline will try run right away because they will se change in the github but its only because is a new deployment*

###6.3 init the windows agent of jenkins **

Go to - Manage Jenkins > Nodes > windows-agent


and change the ip and port the customized for your localmachine

![image](https://github.com/user-attachments/assets/a9dd6d40-aa39-4490-b30a-04e2b6b76170)

```cmd
curl -sO http://192.168.49.2:30080/jnlpJars/agent.jar;java -jar agent.jar -url http://192.168.49.2:30080/ -secret 6391e7e6667d3ad1f712eb0777623f0b60ec3373e47a8158dfec743ed5b458ff -name "windows-agent" -webSocket -workDir "C:\jenkins-win-agent"




---
## **7. Final Checklist**
- [ ] All required dependencies are installed and working
- [ ] Docker Desktop is running with Kubernetes enabled
- [ ] MySQL is properly configured and accessible
- [ ] Jenkins is deployed on your Kubernetes cluster
- [ ] All services are verified operational with version checks

---
This document ensures you have all the tools and dependencies needed to run the project successfully on Windows, while avoiding unnecessary reinstallation of components you already have.
