pipeline {
    agent any

    parameters {
        choice(name: 'browser', choices: ['chromium', 'firefox'])
        choice(name: 'suite', choices: ['smoke', 'regression'])
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                echo 'setup Stage done!'

                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                pytest -m "%suite%" --browser_name "%browser%" --html=AutoJenkinsreport.html
                """
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: '.',
                    reportFiles: 'AutoJenkinsreport.html',
                    reportName: 'Playwright Test Report'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'AutoJenkinsreport.html'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
