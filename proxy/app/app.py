# LOG8415E - Final Project
# flask.py
# Python file of the Flask app that acts as a Proxy.

import mysql.connector
import pandas as pd
import pymysql
import logging
import sshtunnel
from flask import Flask, request
from mysql.connector import Error
from sshtunnel import SSHTunnelForwarder

# IP of master node
master_IP = "54.166.246.82"

app = Flask(__name__)

# Default route
@app.route("/")
def hello_world():
    return "Hello, World!"

# Route for the direct hit algorithm
@app.route('/hit', methods = ['POST'])
def hit():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        hitProxy(query)
        return query

# Route for the random algorithm
@app.route('/random', methods = ['POST'])
def random():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        return

# Route for the customized algorithm
@app.route('/customized', methods = ['POST'])
def customized():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        return


def hitProxy(query):
    try:
        connection = mysql.connector.connect(host=master_IP,
                             database="sakila",
                             user="benchmark",
                             password="admin123")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("db info :", db_Info)
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("records are : ", records)
    except Error as e:
        print("Error")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("closed")
    return