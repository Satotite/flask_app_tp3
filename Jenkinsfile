pipeline {
    agent any

    stages {
        stage('Loading') {
            steps {
                git url: 'https://github.com/Satotite/flask_app_tp3', branch: 'main'
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-html selenium
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest tests/test_logiciel.py --html=rapport_unitaires.html
                '''
            }
        }

        stage('Run Functional Tests (Selenium)') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest tests/test_selenium.py --html=rapport_fonctionnel.html
                '''
            }
        }

        stage('Publish Reports') {
            steps {
                archiveArtifacts artifacts: '*.html', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo 'Build terminé avec succès.'
        }
        failure {
            echo 'Le build a échoué.'
        }
    }
}
