
# Project Requirements

This document outlines all the resources and tools required to run the code in this project.

---

## **1. Python**

### **Version Requirement**
- **Python 3.11** or newer.

### **Installation**
1. Download Python from the [official website](https://www.python.org/downloads/).
2. During installation, **check the box** to **Add Python to PATH**.
3. Verify the installation:
   ```bash
   python --version
   ```

---

## **2. pip**
- Ensure pip is installed and available in PATH.

### **Verify Installation**
1. Check if pip is installed:
   ```bash
   pip --version
   ```
2. If pip is not installed, follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

---

## **3. Chocolatey (Windows)**
- **Purpose**: For managing additional tools like Git, kubectl, and Helm.

### **Installation**
1. Open a command prompt as Administrator.
2. Run the following command:
   ```bash
   @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
   ```
3. Verify installation:
   ```bash
   choco --version
   ```

---

## **4. Git**
- **Purpose**: For managing source code and version control.

### **Installation**
1. Install Git via Chocolatey:
   ```bash
   choco install git
   ```
2. Verify installation:
   ```bash
   git --version
   ```

---

## **5. Kubernetes with Docker Desktop**
- **Purpose**: To use Kubernetes as a container orchestration tool on your local machine.

### **Installation**
1. Download and install Docker Desktop: [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Enable Kubernetes in Docker Desktop:
   - Open Docker Desktop.
   - Navigate to **Settings** > **Kubernetes**.
   - Check **Enable Kubernetes**.
   - Click **Apply and Restart**.
3. Verify Kubernetes is running:
   ```bash
   kubectl version --client
   kubectl get nodes
   ```

---

## **6. Helm**
- Simplifies Kubernetes application management.

### **Installation**
```bash
choco install kubernetes-helm
```

### **Verify Installation**
```bash
helm version
```

---


## **Checklist for Windows Users**
- [ ] Install Python 3.11 and ensure it is added to PATH. Python is required for the project, but dependencies will be handled by Jenkins.
- [ ] Install pip and verify it is available in PATH.
- [ ] Install Chocolatey for package management.
- [ ] Install Git for version control.
- [ ] Install Docker Desktop and enable Kubernetes.
- [ ] Install kubectl for Kubernetes CLI.
- [ ] Install Helm for Kubernetes application management.

---

This document ensures you have all the tools and dependencies needed to run the project successfully.
