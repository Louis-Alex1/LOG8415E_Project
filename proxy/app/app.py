# LOG8415E - Final Project
# flask.py
# Python file of the Flask app that acts as a Proxy.

# import pymysql
# import paramiko
# import pandas as pd
# from paramiko import SSHClient
# from sshtunnel import SSHTunnelForwarder
# from os.path import expanduser
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/hit', methods = ['POST'])
def algo1():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        return

@app.route('/random', methods = ['POST'])
def algo1():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        return

@app.route('/customized', methods = ['POST'])
def algo1():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        return
