pipeline {
    agent any  // Use any available agent

    stages {
        stage('Pull Code') {
            steps {
                // Pull code from GitHub repository
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'main'
            }
        }

      //  stage('Run Backend Server') {
         //   steps {
                // Skip running rest_app.py in this stage by commenting out the command
                // bat 'start /min cmd.exe /K "python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\rest_app.py"'
        //    }
      //  }

        //stage('Run Frontend Server') {
           // steps {
                // Skip running web_app.py in this stage by commenting out the command
                // bat 'start /min cmd.exe /K "python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\web_app.py"'
           // }
      //  }

        stage('Backend Testing') {
            steps {
                // Run backend_testing.py and wait for it to finish
                bat 'python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\backend_testing.py'
            }
        }

        stage('Frontend Testing') {
            steps {
                // Run frontend_testing.py and wait for it to finish
                bat 'python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\frontend_testing.py'
            }
        }

        stage('Combined Testing') {
            steps {
                // Run combined_testing.py and wait for it to finish
                bat 'python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\combined_testing.py'
            }
        }

        stage('Clean Environment') {
            steps {
                // Run clean_environment.py at the end to perform cleanup
                bat 'python C:\\data\\jenkins_home\\workspace\\devops_project_pipeline\\clean_environment.py'
            }
        }
    }
}
