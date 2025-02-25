pipeline {
    agent any  // Use any available agent

    stages {
        stage('Pull Code') {
            steps {
                // Pull code from GitHub repository
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'second-part'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install all libraries from requirements.txt
                    bat 'pip install -r prj-requirements.txt'
                }
            }
        }

        stage('Create mySQL_DB') {
            steps {
                script {
                    // Creating DB Schema and table
                    bat 'python mySQL/createDB.py'
                }
            }
        }

        stage('Run Backend Server') {
            steps {
                // Updated path to backend server script
                bat 'start /min /b python App/rest_app.py'
            }
        }

        stage('Run Frontend Server') {
            steps {
                // Updated path to frontend server script
                bat 'start /min /b python App/web_app.py'
            }
        }

        stage('Backend Testing') {
            steps {
                // Updated path to backend_testing.py
                bat 'python "Testing Scripts/backend_testing.py"'
            }
        }

        stage('Frontend Testing') {
            steps {
                // Updated path to frontend_testing.py
                bat 'python "Testing Scripts/frontend_testing.py"'
            }
        }

        stage('Combined Testing') {
            steps {
                // Updated path to combined_testing.py
                bat 'python "Testing Scripts/combined_testing.py"'
            }
        }

        stage('Clean Environment') {
            steps {
                // Updated path to clean_environment.py
                bat 'python "Testing Scripts/clean_environment.py"'
            }
        }
    }

    post {
        failure {
            // Email notification in case of failure
            emailext(
                subject: 'Build Failure Notification',
                body: '${JELLY_SCRIPT,template="html"}',
                to: 'ofrigsp@gmail.com',
                replyTo: '$DEFAULT_REPLYTO',
                mimeType: 'text/html'
            )
        }
    }
}
