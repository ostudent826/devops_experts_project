pipeline {
    agent any  // Use any available agent

    stages {
        stage('Pull Code') {
            steps {
                // Pull code from GitHub repository
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'main'
            }
        }

        stage('Run Backend Servers') {
            parallel {
                stage('Run REST API') {
                    steps {
                        // Run the REST API server in a minimized window
                        bat 'start /min "C:\Users\shaam\AppData\Local\Programs\Python\Python312\python.exe" rest_app.py'
                    }
                }

                stage('Run Web Server') {
                    steps {
                        // Run the Web server in a minimized window
                        bat 'start /min "C:\Users\shaam\AppData\Local\Programs\Python\Python312\python.exe" web_app.py'
                    }
                }
            }
        }

        stage('Delay') {
            steps {
                // Add a delay of 10 seconds
                script {
                    sleep 10
                }
            }
        }

        stage('Run Cleanup Script') {
            steps {
                // Run the cleanup script at the end
                bat '"C:\Users\shaam\AppData\Local\Programs\Python\Python312\python.exe" clean_environment.py'
            }
        }
    }
}
