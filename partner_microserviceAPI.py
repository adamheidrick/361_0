import requests
import json
import time

source = 'dad-joke.txt'
url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {"#",
           "#"
           }


def main():
    while True:
        time.sleep(1)
        with open(source, 'r') as f:
            value = f.read()
            print('Listening for Request..')

            if value == 'dad':
                message = 'REQUEST RECEIVED '
                print(f"{message} FOR VALUE: {value}")
                f.close()

        with open(source, 'w', encoding="utf-8") as f:
            response = requests.request("GET", url, headers=headers)
            setup, punchline = setup_and_punchline(response)
            f.write(' ' + setup + '\n' + ' ' + punchline)


def setup_and_punchline(response):
    joke = response.json()
    setup = joke['body'][0]['setup']
    punchline = joke['body'][0]['punchline']
    return setup, punchline


if __name__ == "__main__":
    main()
