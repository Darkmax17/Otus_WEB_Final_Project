pipeline {
    agent any
    parameters {
        string(name: 'BROWSER', defaultValue: 'chrome', description: '...')
        booleanParam(name: 'HEADLESS', defaultValue: true, description: '...')
        string(name: 'THREADS', defaultValue: '2', description: '...')
        string(name: 'URL', defaultValue: 'https://www.saucedemo.com', description: '...')
    }
    environment {
        IMAGE_NAME = "saucedemo_tests"
        ALLURE_RESULTS = "${env.WORKSPACE}/allure-results"
    }
    options {
        timeout(time: 30, unit: 'MINUTES')
        ansiColor('xterm')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh "docker build -t ${IMAGE_NAME} ." }
        }
        stage('Test') {
            steps {
                sh "rm -rf ${ALLURE_RESULTS} && mkdir -p ${ALLURE_RESULTS}"
                script {
                    def headlessFlag = params.HEADLESS ? "--headless" : ""
                    sh """
                    docker run --rm \\
                      -v ${ALLURE_RESULTS}:/app/allure-results \\
                      ${IMAGE_NAME} \\
                      --url ${params.URL} \\
                      --browser ${params.BROWSER} \\
                      ${headlessFlag} \\
                      -n ${params.THREADS}
                    """
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'allure-results/**/*.json', allowEmptyArchive: true
                    allure([
                      includeProperties: false,
                      reportBuildPolicy: 'ALWAYS',
                      results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
    post {
        success { echo 'UI tests passed!' }
        failure { echo 'UI tests failed! See Allure Report.' }
    }
}
