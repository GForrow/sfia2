pipeline{

    agent any

    stages {

        stage('Pull Images') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/pull_images.sh'
            }
            
        }

        stage('Build Stack') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_stack.sh'
            }
            
        }

        stage('Update Stack') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/update_stack.sh'
            }
            
        }

    }

}