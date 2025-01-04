
# Project Requirements for Windows Users

This document outlines all the resources and tools required to run the code in this project on Windows.

---

## **1. Python**

### **Version Requirement**
- **Python 3.11** or newer.

### **Installation**
1. Download Python from the [official website](https://www.python.org/downloads/).
2. During installation, **check the box** to **Add Python to PATH**.
3. Verify the installation:
   ```cmd
   python --version
   ```

---

## **2. pip**
- Ensure pip is installed and available.

### **Verify Installation**
1. Check if pip is installed:
   ```cmd
   pip --version
   ```
2. If pip is not installed, use:
   ```cmd
   python -m ensurepip --upgrade
   ```

---

## **3. Chocolatey**
- **Purpose**: For managing additional tools like Git, kubectl, and Helm.

### **Installation**
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

## **4. Git**
- **Purpose**: For managing source code and version control.

### **Installation**
1. Install Git via Chocolatey:
   ```cmd
   choco install git
   ```
2. Verify installation:
   ```cmd
   git --version
   ```

---

## **5. MySQL**
- **Purpose**: To provide a database for the application.

### **Installation**
1. Install MySQL via Chocolatey:
   ```cmd
   choco install mysql
   ```
2. Start the MySQL service:
   ```cmd
   net start mysql
   ```
3. Secure MySQL installation:
   ```cmd
   mysql_secure_installation
   ```
4. Set up the database with the required credentials:
   - Root username: `root`
   - Root password: `123456`
   - Alternatively, use:
     - Username: `admin`
     - Password: `123456`
5. Verify MySQL is running on port `3306`:
   ```cmd
   mysqladmin -u root -p status
   ```

---

## **6. Kubernetes with Docker Desktop**
- **Purpose**: To use Kubernetes as a container orchestration tool on your local machine.

### **Installation**
1. Download and install Docker Desktop: [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Enable Kubernetes in Docker Desktop:
   - Open Docker Desktop.
   - Navigate to **Settings** > **Kubernetes**.
   - Check **Enable Kubernetes**.
   - Click **Apply and Restart**.
3. Verify Kubernetes is running:
   ```cmd
   kubectl version --client
   kubectl get nodes
   ```

---

## **7. Helm**
- Simplifies Kubernetes application management.

### **Installation**
1. Install Helm via Chocolatey:
   ```cmd
   choco install kubernetes-helm
   ```
2. Verify installation:
   ```cmd
   helm version
   ```

---

## **Checklist for Windows Users**
- [ ] Install Python 3.11 and ensure it is added to PATH. Python is required for the project, but dependencies will be handled by Jenkins.
- [ ] Install pip and verify it is available.
- [ ] Install Chocolatey for package management.
- [ ] Install Git for version control via Chocolatey.
- [ ] Install MySQL and configure it to run on port `3306` with the appropriate credentials.
- [ ] Install Docker Desktop and enable Kubernetes.
- [ ] Install kubectl for Kubernetes CLI via Chocolatey.
  ```cmd
  choco install kubernetes-cli
  ```
- [ ] Install Helm for Kubernetes application management via Chocolatey.
  ```cmd
  choco install kubernetes-helm
  ```

---

This document ensures you have all the tools and dependencies needed to run the project successfully on Windows.
