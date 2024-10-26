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
                        // Run the REST API server in a visible command prompt window
                        bat 'start cmd /k "python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\rest_app.py"'
                    }
                }

                stage('Run Web Server') {
                    steps {
                        // Run the Web server in a visible command prompt window
                        bat 'start cmd /k "python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\web_app.py"'
                    }
                }
            }
        }
    }
}
