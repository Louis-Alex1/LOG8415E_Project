import requests

url = 'http://127.0.0.1:5000/random'
query1 = {'query': 'SHOW FULL TABLES;'}

x = requests.post(url, data = query1)

print(x.text)