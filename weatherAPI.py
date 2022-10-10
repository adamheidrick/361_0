import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "85603"}

headers = {
    "X-RapidAPI-Key": "27c0ac8818msh2ca32d6adfc0fb1p1d0a96jsn4c228f1a6b2a",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
weather = response.json()
print(weather)
