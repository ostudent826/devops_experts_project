
# Project Requirements for Windows Users

This document outlines all the resources and tools required to run the code in this project on Windows.

---

## **1. Chocolatey**
- **Purpose**: For managing all dependencies like Python, Git, MySQL, Docker, Kubernetes, Helm, and Java.

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

## **2. Install All Dependencies Using Chocolatey**

### **One-Click Installation Command**
This command installs all required tools in one go:
```cmd
choco install python git mysql docker-engine kubernetes-cli kubernetes-helm temurin17 -y
```

### **Explanation**
- This command installs:
  - **Python 3.11+** (with pip included).
  - **Git** for version control.
  - **MySQL** database.
  - **Docker Engine** (without Docker Desktop).
  - **kubectl** for Kubernetes CLI.
  - **Helm** for Kubernetes management.
  - **Temurin OpenJDK 17** for Java.

### **Verify Installation**
After installation, verify each tool using:
```cmd
python --version
pip --version
git --version
mysql --version
docker --version
kubectl version --client
helm version
java --version
```

---

## **3. Docker Engine with Kubernetes**
- **Purpose**: To use Docker as a container runtime on your local machine, with Kubernetes for orchestration.

### **Installation Using Chocolatey**
```cmd
choco install docker-engine -y
```

### **Start and Enable Docker Service**
After installation, start Docker and enable it to start on boot:
```cmd
net start com.docker.service
sc config com.docker.service start= auto
```

### **Verify Installation**
```cmd
docker version
```

### **Install kubectl via Chocolatey**
```cmd
choco install kubernetes-cli -y
```

### **Configure kubectl to Use Docker Engine**
```cmd
kubectl config set-context docker
kubectl config use-context docker
```

### **Test Docker Installation**
Pull and run a test container:
```cmd
docker pull hello-world
docker run hello-world
```

---

## **4. MySQL Configuration**
- **Purpose**: To provide a database for the application.

### **Steps:**
1. Start the MySQL service:
   ```cmd
   net start mysql
   ```
2. Secure MySQL installation:
   ```cmd
   mysql_secure_installation
   ```
3. Set up the database with the required credentials:
   - Root username: `root`
   - Root password: `123456`
   - Alternatively, use:
     - Username: `admin`
     - Password: `123456`
4. Verify MySQL is running on port `3306`:
   ```cmd
   mysqladmin -u root -p status
   ```

---

## **5. Checklist for Windows Users**
- [ ] Install Chocolatey for package management.
- [ ] Install all dependencies with one command using Chocolatey.
- [ ] Start and enable Docker Engine.
- [ ] Configure kubectl to use Docker Engine.
- [ ] Set up and secure MySQL on port `3306`.
- [ ] Verify all installations with version checks.

---

## **6. Java Installation (OpenJDK 17)**
- **Purpose**: Required for Jenkins and other Java-based applications.

### **Version Requirement**
- **OpenJDK 17.0.13** or newer (Temurin distribution).

### **Installation Using Chocolatey**
```cmd
choco install temurin17 -y
```

### **Verify Installation**
```cmd
java --version
```
Example Output:
```
openjdk 17.0.13 2024-10-15
OpenJDK Runtime Environment Temurin-17.0.13+11 (build 17.0.13+11)
OpenJDK 64-Bit Server VM Temurin-17.0.13+11 (build 17.0.13+11, mixed mode, sharing)
```

---

## **Why This Version Is Better**
- **Unified Installation**: One command installs all tools via Chocolatey.
- **Consistent Version Control**: Ensures the latest version of each tool.
- **Reduced Complexity**: Merges steps for a cleaner and more maintainable setup.

---

This document ensures you have all the tools and dependencies needed to run the project successfully on Windows.
