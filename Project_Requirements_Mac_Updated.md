
# Project Requirements for Mac Users

This document outlines all the resources and tools required to run the code in this project on macOS.

---

## **1. Python**

### **Version Requirement**
- **Python 3.11** or newer.

### **Installation**
1. Install Python via Homebrew:
   ```bash
   brew install python
   ```
2. Verify the installation:
   ```bash
   python3 --version
   ```

---

## **2. pip**
- Ensure pip is installed and available.

### **Verify Installation**
1. Check if pip is installed:
   ```bash
   pip3 --version
   ```
2. If pip is not installed, use:
   ```bash
   python3 -m ensurepip --upgrade
   ```

---

## **3. Homebrew**
- **Purpose**: For managing additional tools like Git, kubectl, and Helm.

### **Installation**
1. Open the terminal.
2. Run the following command to install Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Verify installation:
   ```bash
   brew --version
   ```

---

## **4. Git**
- **Purpose**: For managing source code and version control.

### **Installation**
1. Install Git via Homebrew:
   ```bash
   brew install git
   ```
2. Verify installation:
   ```bash
   git --version
   ```

---

## **5. MySQL**
- **Purpose**: To provide a database for the application.

### **Installation**
1. Install MySQL via Homebrew:
   ```bash
   brew install mysql
   ```
2. Start the MySQL service:
   ```bash
   brew services start mysql
   ```
3. Secure MySQL installation:
   ```bash
   mysql_secure_installation
   ```
4. Set up the database with the required credentials:
   - Root username: `root`
   - Root password: `123456`
   - Alternatively, use:
     - Username: `admin`
     - Password: `123456`
5. Verify MySQL is running on port `3306`:
   ```bash
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
   ```bash
   kubectl version --client
   kubectl get nodes
   ```

---

## **7. Helm**
- Simplifies Kubernetes application management.

### **Installation**
1. Install Helm via Homebrew:
   ```bash
   brew install helm
   ```
2. Verify installation:
   ```bash
   helm version
   ```

---

## **Checklist for Mac Users**
- [ ] Install Python 3.11 and ensure it is added to PATH. Python is required for the project, but dependencies will be handled by Jenkins.
- [ ] Install pip and verify it is available.
- [ ] Install Homebrew for package management.
- [ ] Install Git for version control via Homebrew.
- [ ] Install MySQL and configure it to run on port `3306` with the appropriate credentials.
- [ ] Install Docker Desktop and enable Kubernetes.
- [ ] Install kubectl for Kubernetes CLI via Homebrew.
  ```bash
  brew install kubectl
  ```
- [ ] Install Helm for Kubernetes application management via Homebrew.
  ```bash
  brew install helm
  ```

---

This document ensures you have all the tools and dependencies needed to run the project successfully on macOS.
