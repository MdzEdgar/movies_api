import requests

URL = 'http://localhost:8000/api/v1/reviews'
REVIEW = {
    'user_id': 1,
    'movie_id': 1,
    'review': 'Review creada con request',
    'score': 3
}

response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print('Reseña creada de forma exitosa.')
    print(response.json()['id'])
else:
    print(response.content)
