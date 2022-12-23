import requests

url1 = 'http://127.0.0.1:5000/hit'
url2 = 'http://127.0.0.1:5000/random'
url3 = 'http://127.0.0.1:5000/customized'
query = {'query': 'SHOW FULL TABLES;'}

x = requests.post(url1, data = query)
y = requests.post(url2, data = query)
z = requests.post(url3, data = query)