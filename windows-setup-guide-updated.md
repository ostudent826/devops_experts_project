# 🖥️ Project Setup Guide for Windows Users

This document outlines all the tools and setup steps required to run this project successfully on Windows.

---

## **1. Prerequisite Check ✅**

Before installing anything, check if you already have the required tools:

```cmd
python --version
git --version
helm version
java --version
docker --version
mysql --version
```

> Skip installation steps for any tools already installed and functional.

---

## **2. Install Chocolatey (If Not Installed)**

**Purpose**: A package manager for installing tools like Python, Git, Docker, Helm, MySQL, and Java.

### Steps:
1. Open a **Command Prompt as Administrator**.
2. Run:

```cmd
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

3. Confirm installation:

```cmd
choco --version
```

---

## **3. Install Required Dependencies**

### ✅ Required Versions

| Tool           | Version                    |
|----------------|----------------------------|
| Python         | 3.11 or newer              |
| Git            | Latest                     |
| Helm           | 3.x                        |
| Java (Temurin) | 17.0.13 or newer           |
| Docker Desktop | Latest                     |
| MySQL          | 8.0 or newer               |

### 🔧 Install with Chocolatey

Install only the tools you need:

```cmd
choco install python -y
choco install git -y
choco install kubernetes-helm -y
choco install temurin17 -y
choco install docker-desktop -y
choco install mysql -y
```

> ⚠️ Ignore red output for mysql install.

---

## **4. Docker Desktop Setup**

### 4.1 Start Docker Engine

Open Docker Desktop manually the first time.

> 💡 To start it automatically on boot, enable it in Docker settings.

### 4.2 Enable Kubernetes in Docker Desktop

1. Go to: `Settings` → `Kubernetes`  
2. Check **Enable Kubernetes**  
3. Click **Apply & Restart**

Wait until the status changes to "Kubernetes is running".

---

## **5. MySQL Setup**

1. Check installation:

```cmd
mysql --version
```

> If not recognized, restart your computer.

2. Initialize MySQL:

```cmd
mysql -u root -p

ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
FLUSH PRIVILEGES;
EXIT;
```

---

## **6. Jenkins Installation**

**Purpose**: To run CI/CD pipelines using Kubernetes.

### 📁 Prerequisite

Create a folder: `C:\jenkins-win-agent`

---

### **6.1 Deploy Jenkins via Helm**

After confirming Docker Desktop & Kubernetes are running:

```cmd
helm install jenkins https://raw.githubusercontent.com/ostudent826/devops_experts_project/main/jenkins-5.8.3.tgz

```

> ⏳ **WAIT:** Jenkins pods are initializing. This may take a minute.


### **6.2 Access Jenkins in Browser**

Once deployed, open:  
**[http://localhost:30080](http://localhost:30080)**

**Login:**
- Username: `admin`
- Password: `admin`

> ⚠️ The pipeline may auto-trigger due to initial GitHub webhook sync — this is normal.

---

### **6.3 Configure Jenkins Windows Agent**

1. Navigate to:  
   `Manage Jenkins` → `Nodes` → `windows-agent`

2. Update IP/Port to match your local machine.  
   Example:  
   ![agent config screenshot](https://github.com/user-attachments/assets/411cfd39-4d21-49c2-98af-a25c98d3cbac)

3. Start the Jenkins agent:

```cmd
curl.exe -sO http://127.0.0.1:51580/jnlpJars/agent.jar & java -jar agent.jar -url http://127.0.0.1:51580/ -secret 4b4ba9340cc6d89ca3fa520b2a95b844a1b3c3616f0725ae9c774771f9f97513 -name "windows-agent" -webSocket -workDir "C:\jenkins-win-agent"
```

> ❗ **Do not close this terminal** — the agent disconnects if the process stops.

Agent running example:  
![agent running](https://github.com/user-attachments/assets/733e6e55-acb5-477c-9035-0fdf03e2120e)

---

## ✅ Final Checklist

- [ ] All required tools are installed
- [ ] Docker Desktop is running with Kubernetes enabled
- [ ] MySQL server is set up and accessible
- [ ] Jenkins is deployed on your Kubernetes cluster
- [ ] Jenkins agent is connected and running

---

This guide ensures a complete and reproducible setup for running your project on Windows — no reinstallation of existing tools necessary.
