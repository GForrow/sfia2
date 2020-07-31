pipeline{

    agent any

    stages {

        stage('Build and Push') {
            
            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'
            }
            
        }

        stage('Build Stack') {
            
            steps {
                sh './scripts/build_stack.sh'
            }
            
        }

        stage('Update Stack') {
            
            steps {
                sh './scripts/update_stack.sh'
            }
            
        }

    }

}