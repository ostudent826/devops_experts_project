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
                        // Run the REST API server in a visible window and log output
                        bat 'start New Text Document.bat'
                    }
                }

                stage('Run Web Server') {
                    steps {
                        // Run the Web server in a visible window and log output
                        bat 'start python web_app.py >> web_server_log.txt 2>&1'
                    }
                }
            }
        }
    }
}
