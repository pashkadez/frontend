#!groovy
pipeline {
    agent any
    environment {
        SERVER_CREDENTIALS = credentials('server-credentials')
    }
    stages {
        stage("Create docker image") {
            steps {
                echo " ========== start building image ========== "
            }
        }
        stage("deploy") {
            steps {
                echo " ========== deploying the app ========== "
                withCredentials([
                    usernamePassword(credentials: 'server-credentials', usernameVariable: USER, passwordVariable: PWD)
                ]) {
                    sh 'some script'
                }
            }
        }
    }
}