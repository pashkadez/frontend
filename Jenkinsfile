pipeline {
  agent any
  stages {
    stage('') {
      steps {
        git(poll: true, url: 'https://github.com/Kv-DevOps-094/frontend/', branch: 'develop')
        container(name: '123', shell: 'docker build -t oleksiihead/frontend:3.0') {
          container(name: '234', shell: 'doker push oleksiihead/frontend:3.0')
        }

        kubernetesEngineDeploy(cluster: 'kv094-cluster', clusterName: 'kv094-cluster', location: 'europe-west3', namespace: 'default', projectId: 'main-basis-321206', zone: 'europe-west3-c')
      }
    }

  }
}