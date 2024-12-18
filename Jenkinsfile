pipeline {
    agent any  // Use any available agent

    stages {
        stage('Pull Code') {
            steps {
                // Pull code from GitHub repository
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'second-part'
            }
        }

        stage('Run Backend Server') {
            steps {
                bat 'start /min /b python rest_app.py'
            }
        }

        stage('Run Frontend Server') {
            steps {
                bat 'start /min /b python web_app.py'
            }
        }

        stage('Backend Testing') {
            steps {
                // Run backend_testing.py and wait for it to finish
                bat 'python backend_testing.py'
            }
        }

        stage('Frontend Testing') {
            steps {
                // Intentional error to test email notification
                bat 'python frontend_testing.py'
            }
        }
		
		stage('Combined Testing') {
            steps {
                // Run combined_testing.py and wait for it to finish
                bat 'python combined_testing.py'
            }
        }

        stage('Clean Environment') {
            steps {
                // Run clean_environment.py at the end to perform cleanup
                bat 'python clean_environment.py'
            }
        }
    }

    post {
        failure {
            emailext(
                subject: 'omo',
                body: '${JELLY_SCRIPT,template="html"}',
                to: 'ofrigsp@gmailcom',
                replyTo: '$DEFAULT_REPLYTO',
                mimeType: 'text/html'
            )
        }
    }
}
