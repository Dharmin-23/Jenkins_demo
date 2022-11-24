

pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Dharmin-23/Jenkins_demo'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x function.py"
                sh "python3 function.py"
            }
        }
     stage('Test Code1') {
            steps {
                sh "chmod u+x Test1.py"
                sh "python3 Test1.py"
            }
        }
        
    stage('Test Codef') {
            steps {
                sh "chmod u+x Testf.py"
                sh "python3 Testf.py"
            }
        }
    } 
}
