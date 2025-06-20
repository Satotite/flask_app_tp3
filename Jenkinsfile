pipeline {
  agent any

  environment {
    DISPLAY = ':99' 
  }

  stages {
    stage('Clone du projet') {
      steps {
        git 'https://github.com/Satotite/flask_app_tp3.git'
      }
    }

    stage('Installer les dépendances') {
      steps {
        sh '''
          python3 -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
          pip install pytest pytest-html selenium
        '''
      }
    }

    stage('Lancer les tests unitaires') {
      steps {
        sh '''
          source venv/bin/activate
          pytest tests/test_logiciel.py --html=rapport_unitaires.html
        '''
      }
    }

    stage('Lancer Selenium (headless)') {
      steps {
        sh '''
          sudo apt-get update
          sudo apt-get install -y firefox xvfb
          Xvfb :99 -screen 0 1920x1080x24 &
          export DISPLAY=:99
          source venv/bin/activate
          pytest tests/test_selenium.py --html=rapport_fonctionnel.html
        '''
      }
    }

    stage('Archiver les rapports') {
      steps {
        archiveArtifacts artifacts: '*.html', allowEmptyArchive: true
      }
    }
  }

  post {
    always {
      echo 'Pipeline terminé !'
    }
    success {
      echo ' Tous les tests sont passés !'
    }
    failure {
      echo ' Un test a échoué.'
    }
  }
}
