pipeline {
    agent any  // Use any available agent

    stages {
        stage('Pull Code') {
            steps {
                // Pull code from GitHub repository
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                bat '"C:\\Users\\shaam\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Backend Servers') {
            parallel {
                stage('Run REST API') {
                    steps {
                        // Run the REST API server in a visible window
                        bat 'start /min  python C:\data\jenkins_home\workspace\devops_project_pipeline\rest_app.py'
                    }
                }

                stage('Run Web Server') {
                    steps {
                        // Run the Web server in a visible window
                        bat 'start /min  python C:\data\jenkins_home\workspace\devops_project_pipeline\web_app.py'
                    }
                }
            }
        }
    }
}
