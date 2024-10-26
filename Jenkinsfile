pipeline {
    agent any  // Use any available agent

    stages {
        stage('Pull Code') {
            steps {
                // Pull code from GitHub repository
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'main'
            }
        }

        stage('Install Requirements') {
            steps {
                // Install dependencies from requirements.txt
                bat 'python -m pip install -r C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\requirements.txt'
            }
        }

        stage('Run Backend Servers') {
            parallel {
                stage('Run REST API') {
                    steps {
                        // Start REST API server in a visible cmd window and save the PID
                        bat 'start cmd /k "python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\rest_app.py" & echo !^! > rest_pid.txt'
                    }
                }

                stage('Run Web Server') {
                    steps {
                        // Start Web server in a visible cmd window and save the PID
                        bat 'start cmd /k "python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\web_app.py" & echo !^! > web_pid.txt'
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Kill the command prompts by PID if they exist
                bat 'for /f %p in (rest_pid.txt) do taskkill /F /PID %p'
                bat 'for /f %p in (web_pid.txt) do taskkill /F /PID %p'
            }
        }
    }

    post {
        always {
            // Remove the temporary PID files at the end of the build
            bat 'del rest_pid.txt'
            bat 'del web_pid.txt'
        }
    }
}
