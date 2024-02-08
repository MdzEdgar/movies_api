import requests

URL = 'http://localhost:8000/api/v1/reviews'

response = requests.get(URL)

if response.status_code == 200:
    print('Peticion realizada de forma exitosa')
    print(response.content)
