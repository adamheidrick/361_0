from __future__ import print_function, unicode_literals

import os
import time
import json
import urllib.request
import requests

import menus

from termcolor import colored
from pyfiglet import Figlet
from PyInquirer import prompt
from secretkeys import weather_key


class CycleDad:
    def __init__(self):
        self.logoText = Figlet(font='speed')
        self.welcome = menus.welcome
        self.home_menu = menus.home_menu
        self.easy_menu = menus.dad_menu
        self.zip_menu = menus.zip_menu
        self.auto_menu = menus.auto_menu
        self.init = self.main()

    def main(self):
        os.system('clear')
        self.run()
        return 0

    def run(self):
        print("\n")
        print(colored(self.logoText.renderText('CYCLE DAD'), 'cyan'))
        print(self.welcome)
        answers = prompt(self.home_menu, style=menus.style)
        if 'Quit Program' in answers['user_option']:
            self.quit_program()

        elif 'None of that, just give me a dad joke.' in answers['user_option']:
            self.dad_joke()

        else:
            self.parse_answers(answers)

    def parse_answers(self, answers):
        answer = answers['user_option']
        if answer == 'ENTER ZIP':
            self.enter_zip()

        elif answer == 'AUTO ZIP (**NEW FEATURE NOT VPN COMPATIBLE**)':
            self.auto_zip()

        else:
            pass

    def enter_zip(self):
        os.system('clear')
        print(colored(self.logoText.renderText('Enter Zip'), 'cyan'))

        validated = False
        validation = ''

        while validated is not True:
            entered_zip = input(" Enter Your ZIP or type 'q' to go back: ")
            validation = self.validate_zip(entered_zip)
            if validation == 1:
                print(f" Sorry, your zip({entered_zip}) was not correct. Please try again or type 'q' to go back.")

            elif validation == 'quit':
                validated = True
            else:
                validated = True
                print(' ', self.validate_zip(entered_zip))

        if validated is True and validation == 'quit':
            self.go_home()

        else:
            answer = prompt(self.zip_menu, style=menus.style)
            if "Yes, Continue" in answer['user_option']:
                self.results(entered_zip)

            elif 'No, Re-Enter' in answer['user_option']:
                self.enter_zip()

            elif 'Go Back' in answer['user_option']:
                self.go_home()

            else:
                self.quit_program()

    @staticmethod
    def validate_zip(entered_zip):
        if entered_zip.isnumeric() and len(entered_zip) == 5:
            return entered_zip

        elif entered_zip.lower() == 'q':
            return 'quit'

        else:
            return 1

    def auto_zip(self):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Auto Zip'), 'cyan'))
        print(" AUTO ZIP MICROSERVICE. YOUR ZIP IS:")

        ipaddr = urllib.request.urlopen('http://ipify.org').read().decode('utf8')
        ip_api = 'http://ip-api.com/json/'
        req = urllib.request.Request(ip_api + ipaddr)
        response = urllib.request.urlopen(req).read()
        json_response = json.loads(response.decode('utf-8'))
        zip_code = json_response['zip']
        print(colored(' ' + zip_code, 'cyan'))
        # print(colored(' ' + ipaddr + ' ' + zip_code, 'cyan'))
        answers = prompt(self.auto_menu, style=menus.style)

        if 'No, Go Back' in answers['user_option']:
            self.go_home()

        if 'Quit Program' in answers['user_option']:
            self.quit_program()

        if 'Yes, Confirm' in answers['user_option']:
            self.results(zip_code)

    def dad_joke(self, zip_code=None):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Dad Joke'), 'cyan'))
        self.dad_joke_request()
        time.sleep(3)
        answers = prompt(self.easy_menu, style=menus.style)
        if "Go Home" in answers['user_option']:
            self.go_home()
        if "Quit Program" in answers['user_option']:
            self.quit_program()

    @staticmethod
    def dad_joke_request():
        file = open('dad-joke.txt', 'w')
        file.write('dad')
        file.close()

    @staticmethod
    def dad_joke_receive():
        file = open('dad-joke.txt', 'r')
        dad_joke = file.read()
        file.close()
        return dad_joke

    @staticmethod
    def weather_results(zip_code):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q": zip_code}
        headers = {
            "X-RapidAPI-Key": weather_key,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        weather = [data['location']['name'], data['location']['region'], data['current']['condition']['text'],
                   data['current']['temp_f'], data['current']['wind_mph'], data['current']['precip_in']]

        print(weather)
        return weather

    @staticmethod
    def what_to_wear(weather):
        rainy_conditions = ['Rain', 'Shower rain', 'Mist', "Patchy rain possible", "Patchy light drizzle",
                            "Light drizzle", "Patchy light rain", "Light rain", "Moderate rain at times",
                            "Moderate rain", "Heavy rain at times", "Heavy rain"]
        clothes = {'Top': None, 'Bottom': None, 'RainJacket': None}
        if int(weather[-1] > 0) or weather[2] == 'Mist':
            clothes['RainJacket'] = "Wear a rain jacket. It's Raining!"

        if int(weather[3]) <= 60:
            clothes['Top'] = 'Long Sleeve Jersey'
            clothes['Bottom'] = 'Full Length Bib Tights'

        else:
            clothes['Top'] = 'Short Sleeve Jersey'
            clothes['Bottom'] = 'Bib Shorts'

        return clothes

    def results(self, zip_code):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Results'), 'cyan'))

        print(colored("\n RESULTS: \n", 'cyan'))
        print(self.what_to_wear(self.weather_results(zip_code)))

        print(colored("\n DAD JOKE WILL GO HERE \n\n", 'cyan'))
        answers = prompt(self.easy_menu, style=menus.style)
        if 'Quit Program' in answers['user_option']:
            self.quit_program()

        if 'Go Home' in answers['user_option']:
            self.go_home()

    @staticmethod
    def quit_program():
        os.system('clear')
        os.system('exit')

    def go_home(self):
        os.system('clear')
        self.main()


if __name__ == "__main__":
    main = CycleDad()
