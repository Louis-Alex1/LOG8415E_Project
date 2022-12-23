# LOG8415E - Final Project
# request.py
# Python file of that does requests through the Flask proxy. 

import requests

# urls of the 3 different proxy algorithms
url1 = 'http://127.0.0.1:5000/hit'
url2 = 'http://127.0.0.1:5000/randomNode'
url3 = 'http://127.0.0.1:5000/customized'

query = {'query': 'SHOW FULL TABLES;'}

# Request to the 3 differents algorithms
x = requests.post(url1, data = query)
y = requests.post(url2, data = query)
z = requests.post(url3, data = query)