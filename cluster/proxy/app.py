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

# Configuration credentials
nodes = ["54.81.117.88", "54.162.249.104", "100.24.29.166", "54.161.136.42"]
master_private_IP = "10.0.1.13"
db_name = "sakila"
db_user = "benchmark"
db_password= "admin123"

ssh_user = "ubuntu"
ssh_key = "/home/ubuntu/.ssh/FinalProject.pem"
localhost = "127.0.0.1" 

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
        randomProxy(query)
        return query

# Route for the customized algorithm
@app.route('/customized', methods = ['POST'])
def customized():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        return query


def hitProxy(query):
    try:
        hit_connection = mysql.connector.connect(host=nodes[0],
                                            database=db_name,
                                            user=db_user,
                                            password=db_password)
        if hit_connection.is_connected():
            db_Info = hit_connection.get_server_info()
            print("db info :", db_Info)
            cursor = hit_connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("records are : ", records)
    except Error as e:
        print("Error")
    finally:
        if hit_connection.is_connected():
            cursor.close()
            hit_connection.close()
            print("closed")
    return

def randomProxy(query):
    node_index = 1
    openSshTunnel(node_index)
    pymysqlConnect()
    dataframe = pd.read_sql_query(query, connection)
    print(dataframe.head())
    connection.close()
    tunnel.close()
    return

def openSshTunnel(node_index):

    sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    global tunnel
    tunnel = SSHTunnelForwarder(
        (nodes[node_index], 22),
        ssh_username = ssh_user,
        ssh_password = ssh_key,
        remote_bind_address = (master_private_IP, 3306)
    )

    tunnel.start()
    return

def pymysqlConnect():

    global connection

    connection = pymysql.connect(
        host = nodes[0],
        user = db_user,
        passwd = db_password,
        db = db_name,
        port = tunnel.local_bind_port
    )
    return