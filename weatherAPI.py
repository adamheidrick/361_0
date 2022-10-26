import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "85603"}

headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
weather = response.json()
print(weather)
