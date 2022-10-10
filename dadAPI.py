import requests

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
    "X-RapidAPI-Key": "27c0ac8818msh2ca32d6adfc0fb1p1d0a96jsn4c228f1a6b2a",
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
joke = response.json()

print(joke['body'][0]['setup'])
print(joke['body'][0]['punchline'])