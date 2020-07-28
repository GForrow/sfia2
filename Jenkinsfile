pipeline{

    agent any

    stages {

        stage('Pull Images') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/pull_images.sh'
            }
            
        }

    }

}