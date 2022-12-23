# LOG8415E - Final Project
# app.py
# Python file of the Flask app that acts as a Proxy.

import mysql.connector
import pandas as pd
import pymysql
import sshtunnel
import random
import os
import re
import subprocess
from flask import Flask, request
from mysql.connector import Error
from sshtunnel import SSHTunnelForwarder

# Public IPs of nodes and master private IP
# They need to be changed to fit with infrastructure redeploy
nodes = ["54.81.117.88", "54.162.249.104", "100.24.29.166", "54.161.136.42"]
master_private_IP = "10.0.1.13"
localhost = "127.0.0.1" 

# database credentials
db_name = "sakila"
db_user = "benchmark"
db_password = "admin123"

# ssh credentials
ssh_user = "ubuntu"
ssh_key = "/home/ubuntu/.ssh/FinalProject.pem"

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Default route of the Flask app
    
    Returns:
    string: Hello, World text
    """
    return "Hello, World!"

@app.route('/hit', methods = ['POST'])
def hit():
    """Route for the direct hit proxy algorithm
    
    Returns:
    string: sql query
    """
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        hitProxy(query)
        return query

@app.route('/randomNode', methods = ['POST'])
def randomNode():
    """Route for the random proxy algorithm
    
    Returns:
    string: sql query
    """
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        randomProxy(query)
        return query

# Route for the customized algorithm
@app.route('/customized', methods = ['POST'])
def customized():
    """Route for the customized proxy algorithm
    
    Returns:
    string: sql query
    """
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        customizedProxy(query)
        return query


def hitProxy(query):
    """Hit algorithm that calls function to query master node

    Parameters:
    query (string): the sql query
    """
    queryMaster(query)
    return

def queryMaster(query):
    """Function to query master node

    Parameters:
    query (string): the sql query
    """
    try:
        hit_connection = mysql.connector.connect(host=nodes[0],
                                            database=db_name,
                                            user=db_user,
                                            password=db_password)
        if hit_connection.is_connected():
            db_Info = hit_connection.get_server_info()
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
    return

def randomProxy(query):
    """Random algorithm that calls function to query a random slave node

    Parameters:
    query (string): the sql query
    """
    node_index = random.randint(1, 3)
    queryNode(query, node_index)
    return

def queryNode(query, index):
    """Function to query slave node through SSH tunnel

    Parameters:
    query (string): the sql query
    index (int): index of the slave node 
    """
    openSshTunnel(index)
    pymysqlConnect()
    dataframe = pd.read_sql_query(query, connection)
    print(dataframe)
    connection.close()
    tunnel.close()
    return

def openSshTunnel(node_index):
    """Function to open an SSH tunnel

    Parameters:
    node_index (int): index of the slave node 
    """
    global tunnel
    tunnel = SSHTunnelForwarder(
        (nodes[node_index], 22),
        ssh_username = ssh_user,
        ssh_pkey= ssh_key,
        remote_bind_address = (master_private_IP, 3306)
    )

    tunnel.start()
    return

def pymysqlConnect():
    """Function to connect to MySQL master with PyMySQL
    """
    global connection

    connection = pymysql.connect(
        host = localhost,
        user = db_user,
        passwd = db_password,
        db = db_name,
        port = tunnel.local_bind_port
    )
    return

def customizedProxy(query):
    """Customized algorithm that pings every nodes and calls the node with fastest response time

    Parameters:
    query (string): the sql query 
    """
    fastest_node_index = fastestNodePing()
    if fastest_node_index == 0:
        queryMaster(query)
    else:
        queryNode(query, fastest_node_index)
    return

def fastestNodePing():
    """Finds the node with fastest ping response time

    Returns:
    index_min (int): the index of the node with fastest response time
    """
    node_times = []
    
    for node in nodes:
        node_times.append(pingTime(node))

    index_min = node_times.index(min(node_times))
    return index_min

def pingTime(ip_address):
    """Finds the response time of a ping request

    Parameters:
    ip_address (string): the IP address to ping 

    Returns:
    avg_time (int): the average response time of the ping request
    """
    proc = subprocess.Popen(['ping', '-c', '1', ip_address], stdout= subprocess.PIPE)
    out = str(proc.communicate()[0])
    out_regex = re.search('(min\/avg\/max\/mdev = )(.*)(\\\)', out).group(2)
    avg_time = (out_regex.split(" ")[0]).split('/')[1]
    return avg_time