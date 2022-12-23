import requests

url = 'http://127.0.0.1:5000/hit'
query1 = {'query': 'SELECT * FROM NAME;'}
query2 = {'query': 'SELECT * FROM PERSON;'}

x = requests.post(url, data = query1)
y = requests.post(url, data = query2)

print(x.text)
print(y.text)