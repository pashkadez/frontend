from flask import render_template, redirect, url_for, Flask
from app import app
import requests
import json

HOST = '127.0.0.1'
PORT = '5000'


@app.route('/', methods=['GET'])
@app.route('/issues/', methods=['GET'])
def getIssues():
    request = requests.get(f'http://{HOST}:{PORT}/issues/')
    request_data = json.loads(request.content)
    return render_template('index.html', title='Kv-DevOps-094', request_data=request_data)


@app.route('/issues/by-id/<int:id>', methods=['GET'])
def getIssueById(id=None):
    request = requests.get(f'http://{HOST}:{PORT}/issues/by-id/{id}')
    request_data = json.loads(request.content)
    return render_template('issue_by_id.html', title='Kv-DevOps-094', request_data=request_data)


@app.route('/labels/', methods=['GET'])
def getLabels():
    request = requests.get(f'http://{HOST}:{PORT}/labels/')
    request_data = json.loads(request.content)
    return render_template('labels.html', title='Kv-DevOps-094', request_data=request_data)


@app.route('/issues/by-label/<label>', methods=['GET'])
def getIssuesByLabel(label):
    request = requests.get(f'http://{HOST}:{PORT}/issues/by-label/{label}')
    request_data = json.loads(request.content)
    return render_template('issues_by_label.html', request_data=request_data, bug='bug', duplicate='duplicate')
#    return render_template('bug.html', request_data=request_data)


@app.route('/states/', methods=['GET'])
def getStates():
    request = requests.get(f'http://{HOST}:{PORT}/states/')
    request_data = json.loads(request.content)
    return render_template('states.html', title='Kv-DevOps-094', request_data=request_data)


@app.route('/actions/', methods=['GET'])
def getActions():
    request = requests.get(f'http://{HOST}:{PORT}/actions/')
    request_data = json.loads(request.content)
    return render_template('actions.html', title='Kv-DevOps-094', request_data=request_data)


@app.route('/users/', methods=['GET'])
def getUsers():
    request = requests.get(f'http://{HOST}:{PORT}/users/')
    request_data = json.loads(request.content)
    return render_template('users.html', title='Kv-DevOps-094', request_data=request_data)
