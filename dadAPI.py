import requests

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
joke = response.json()

print(joke['body'][0]['setup'])
print(joke['body'][0]['punchline'])
