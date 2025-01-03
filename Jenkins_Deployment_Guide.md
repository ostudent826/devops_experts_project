
# Jenkins Deployment on Kubernetes with Helm

This guide provides step-by-step instructions to deploy Jenkins using Helm on Kubernetes, running on Docker Desktop on a Windows PC.

---

## **System Requirements**

### **Operating System**
- Windows 10 or later (64-bit).

### **Hardware**
- **CPU**: Quad-core CPU (Intel i5, Ryzen 5, or better).
- **Memory**: At least 8 GB RAM (minimum 4 GB for Docker Desktop and Kubernetes, plus 4 GB for Jenkins).
- **Disk Space**: Minimum 20 GB free for Docker images, containers, and Helm charts.
- **Networking**: Stable internet connection.

---

## **Tools to Install**

### **1. Docker Desktop**
- Acts as your Kubernetes cluster.
- Download and install Docker Desktop: [Docker Desktop](https://www.docker.com/products/docker-desktop).

#### Enable Kubernetes in Docker Desktop:
1. Open Docker Desktop.
2. Navigate to **Settings** > **Kubernetes**.
3. Check **Enable Kubernetes**.
4. Click **Apply and Restart**.

---

### **2. kubectl (Kubernetes CLI)**
- Required to interact with the Kubernetes cluster.

#### Installation:
```bash
choco install kubernetes-cli
```

#### Verify Installation:
```bash
kubectl version --client
```

#### Configure kubectl:
```bash
kubectl config use-context docker-desktop
```

---

### **3. Helm**
- Simplifies Jenkins deployment on Kubernetes.

#### Installation:
```bash
choco install kubernetes-helm
```

#### Verify Installation:
```bash
helm version
```

#### Add Jenkins Helm Repository:
```bash
helm repo add jenkins https://charts.jenkins.io
helm repo update
```

---

### **4. Git**
- Required for managing source code and Jenkinsfiles.

#### Installation:
```bash
choco install git
```

#### Verify Installation:
```bash
git --version
```

---

### **5. Java (Optional)**
- Needed for custom Jenkins configurations.

#### Installation:
- Download: [AdoptOpenJDK](https://adoptopenjdk.net/).

#### Configure `JAVA_HOME`:
1. Set the environment variable `JAVA_HOME` to the JDK installation path.
2. Add `%JAVA_HOME%\bin` to the `PATH` variable.

---

## **Deploy Jenkins Using Helm**

### Step 1: Create a Namespace
```bash
kubectl create namespace jenkins
```

### Step 2: Install Jenkins Helm Chart
```bash
helm install jenkins jenkins/jenkins --namespace jenkins --set controller.serviceType=LoadBalancer
```

### Step 3: Check Jenkins Deployment Status
```bash
kubectl get pods -n jenkins
```
Ensure the Jenkins pod is in a `Running` state.

### Step 4: Access Jenkins
1. Find the LoadBalancer IP:
   ```bash
   kubectl get service jenkins -n jenkins
   ```
2. Access Jenkins at `http://<LoadBalancer-IP>:8080`.

### Step 5: Retrieve Admin Password
```bash
kubectl exec --namespace jenkins -it <pod-name> -- cat /run/secrets/chart-admin-password
```
Replace `<pod-name>` with the name of the Jenkins pod.

---

## **Optional: Backup Jenkins Data**

### Persistent Volume for Jenkins Home
Ensure the `jenkins-values.yaml` file contains:
```yaml
controller:
  persistence:
    enabled: true
    size: 10Gi
    storageClass: "standard"
```

### Backup Strategy
1. Use volume snapshots (e.g., Velero, AWS EBS).
2. Manually copy `/var/jenkins_home`:
   ```bash
   kubectl cp jenkins/<pod-name>:/var/jenkins_home ./jenkins_backup
   ```

---

## **Monitoring and Logging**

### Monitoring
- Install Prometheus and Grafana for monitoring Jenkins metrics.
- Install the Prometheus plugin in Jenkins to expose metrics.

### Logging
- Forward Jenkins logs to a centralized system (e.g., ELK Stack or Loki).

---

## **Summary Checklist**

| Tool                | Purpose                                        | Command/Link                                                                 |
|---------------------|------------------------------------------------|------------------------------------------------------------------------------|
| Docker Desktop      | Kubernetes and container runtime              | [Docker Desktop](https://www.docker.com/products/docker-desktop)             |
| kubectl             | Manage Kubernetes resources                   | `choco install kubernetes-cli`                                               |
| Helm                | Simplifies Jenkins deployment in Kubernetes   | `choco install kubernetes-helm`                                              |
| Git                 | Version control for Jenkinsfiles and Helm charts | `choco install git`                                                          |
| Java                | Custom Jenkins configurations                 | [AdoptOpenJDK](https://adoptopenjdk.net/)                                    |

---

This setup ensures a modern, scalable, and reliable Jenkins installation. Let me know if you need additional guidance or help!
