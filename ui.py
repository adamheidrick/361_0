from __future__ import print_function, unicode_literals

import os
import time
import json
import urllib.request
import requests
import menus

from requests import get
from termcolor import colored
from pyfiglet import Figlet
from PyInquirer import prompt
from secretkeys import weather_key
from typing import Union


class CycleDad:
    """This is the Cycle Dad class that contains all the logic and methods for the CycleDad program"""
    def __init__(self):
        self.logoText = Figlet(font='speed')
        self.welcome = menus.welcome
        self.home_menu = menus.home_menu
        self.easy_menu = menus.dad_menu
        self.zip_menu = menus.zip_menu
        self.auto_menu = menus.auto_menu
        self.zip_error_menu = menus.dad_menu
        self.rainy_conditions = ['Rain', 'Shower rain', 'Mist', "Patchy rain possible", "Patchy light drizzle",
                                 "Light drizzle", "Patchy light rain", "Light rain", "Moderate rain at times",
                                 "Moderate rain", "Heavy rain at times", "Heavy rain"]
        self.clothes = {'Top': '', 'Bottom': '', 'RainJacket': 'None'}
        self.init = self.main()

    def main(self) -> int:
        """The main function returns 0"""
        os.system('clear')
        self.run()
        return 0

    def run(self) -> None:
        """ The function that runs the program and starts program execution """
        print("\n")
        print(colored(self.logoText.renderText('CYCLE DAD'), 'cyan'))
        print(self.welcome)
        self.navigation_select(prompt(self.home_menu, style=menus.style))

    def enter_zip(self) -> None:
        """ The function to receive entered zip feature """
        os.system('clear')
        print(colored(self.logoText.renderText('Enter Zip'), 'cyan'))
        entered_zip, validated, validation = self.validation_loop()

        if validated is True and validation == 'quit':
            self.go_home()

        self.navigation_select(prompt(self.zip_menu, style=menus.style), entered_zip)

    def validation_loop(self) -> tuple:
        """ The helper function to ask user for zip input"""
        validated = False
        validation = ''
        entered_zip = None
        while validated is not True:
            entered_zip = input(" Enter Your ZIP or type 'q' to go back: ")
            validation = self.validate_zip(entered_zip)
            if not validation:
                print(f" Sorry, your zip({entered_zip}) was not correct. Please try again or type 'q' to go back.")
            elif validation == 'quit':
                validated = True
            else:
                validated = True
                print(' ', self.validate_zip(entered_zip))
        return entered_zip, validated, validation

    @staticmethod
    def validate_zip(entered_zip: str) -> str:
        """ The helper function to validation loop that validates the length of the zip entered """
        if entered_zip.isnumeric() and len(entered_zip) == 5:
            return entered_zip

        elif entered_zip.lower() == 'q':
            return 'quit'

        else:
            return ''

    def auto_zip(self) -> None:
        """ The auto zip function that parses zip code to helper functions"""
        self.print_auto_zip()
        json_response = self.retrieve_zip()
        zip_code, country, city = json_response['postal'], json_response['country_code'], json_response['city']
        print(colored(' ' + zip_code, 'cyan'))
        if self.parse_country(country):
            self.navigation_select(prompt(self.auto_menu, style=menus.style), zip_code)
        else:
            self.navigation_select(prompt(self.auto_menu, style=menus.style), city)

    @staticmethod
    def parse_country(country: str) -> bool:
        """ The country parser that returns true if the country is in the US which drives the conditional branch in
        auto zip to pass zip or city name-- if city is non U.S. This is necessary for the weather API"""
        return country == 'US'

    @staticmethod
    def retrieve_zip() -> dict:
        """ The IP api call function"""
        ipaddr = get('https://api.ipify.org').text
        req = urllib.request.Request(f"https://ipapi.co/{ipaddr}/json/")
        response = urllib.request.urlopen(req).read()
        json_response = json.loads(response.decode('utf-8'))
        return json_response

    def print_auto_zip(self) -> None:
        """ The printing the results of the api call function """
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Auto Zip'), 'cyan'))
        print(" AUTO ZIP MICROSERVICE. YOUR ZIP IS:")

    def zip_error(self, zip_code: str) -> None:
        """ The printing of an error if the weather api fails due to zip or city"""
        os.system('clear')
        print("\n")
        print(colored(f'Error. Either {zip_code} does not exist in the U.S. or it is not a U.S. zip', 'red'))
        self.navigation_select(prompt(self.zip_error_menu, style=menus.style))

    def dad_joke(self, zip_code=None) -> None:
        """ The dad joke screen and dad joke microservice request function """
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Dad Joke'), 'cyan'))
        self.dad_joke_request()
        self.navigation_select(prompt(self.easy_menu, style=menus.style))

    @staticmethod
    def dad_joke_request() -> None:
        """ The dad joke request function for the microservice """
        file = open('dad-joke.txt', 'w')
        file.write('dad')
        file.close()
        time.sleep(3)
        CycleDad.dad_joke_receive()

    @staticmethod
    def dad_joke_receive() -> None:
        """ The dad joke recieve function for the microservice """
        file = open('dad-joke.txt', 'r')
        dad_joke = file.read()
        print(' ' + dad_joke)
        file.close()

    @staticmethod
    def weather_results(zip_code: str, city=None) -> list:
        """ The weather api call. It needs a US zip or if not in the US then a city name """
        parameter = city if city is not None else zip_code
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q": parameter}
        headers = {"X-RapidAPI-Key": weather_key, "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return CycleDad.parse_weather(data, parameter)

    @staticmethod
    def parse_weather(data: dict, parameter: str) -> Union[list, None]:
        """ A weather parsing function that parses the results of the API Call """
        try:
            weather = [data['location']['name'], data['location']['region'], data['current']['condition']['text'],
                       data['current']['temp_f'], data['current']['wind_mph'], data['current']['precip_in']]
            CycleDad.print_weather(weather, parameter)
            return weather

        except KeyError:
            return None

    @staticmethod
    def print_weather(weather: list, parameter: str) -> None:
        """ The print weather function """
        print(f' Weather Data Based on zip: {parameter} \n')
        details = ['City: ', 'State: ', 'Condition: ', 'Temp: ', 'Feels Like: ', 'Perc: ']
        for i in range(len(details)):
            print(' ' + details[i] + str(weather[i]))
        print('\n')

    def what_to_wear(self, weather: list) -> Union[dict, None]:
        """ The clothing recommendation function """
        if self.zip_found(weather):
            if int(weather[-1] > 0) or weather[2] in self.rainy_conditions:
                self.clothes['RainJacket'] = "Wear a rain jacket. It's Raining!"

            if int(weather[3]) <= 60:
                self.clothes['Top'] = 'Long Sleeve Jersey'
                self.clothes['Bottom'] = 'Full Length Bib Tights'

            else:
                self.clothes['Top'] = 'Short Sleeve Jersey'
                self.clothes['Bottom'] = 'Bib Shorts'

            return self.clothes
        return None

    @staticmethod
    def zip_found(weather: list) -> bool:
        """ The zip helper function ensures that the api call does not return an empty list """
        return weather is not None

    def results(self, zip_code: str) -> None:
        """ The results function prints the results and makes calls for data results and a dad joke request """
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Results'), 'cyan'))

        print(colored("\n RESULTS: \n", 'cyan'))
        self.print_results(zip_code)

        print(colored("\n DAD JOKE IN 3 SECONDS: \n", 'cyan'))
        self.dad_joke_request()
        self.navigation_select(prompt(self.easy_menu, style=menus.style))

    def print_results(self, zip_code):
        """ The printing results function """
        results = self.what_to_wear(self.weather_results(zip_code))
        if results is not None:
            self.print_clothes(results)

        else:
            print(colored(f" Zip Error: {zip_code}. City not found. "
                          f"Check you are not using a VPN and try again.", 'red'))

    @staticmethod
    def print_clothes(clothes: dict) -> None:
        """ The printing clothes recommendation function """
        print(' Clothing Recommendation: \n')
        for key, value in clothes.items():
            print(" " + key + ":" + " " + value)

    def navigation_select(self, answers: dict, zip_code=None) -> None:
        """ The navigation menu function for facilitating all CLI menu screens """
        answer = answers['user_option']
        select_home = ['No, Go Back', 'Go Home', 'Go Back']
        select_results = ['Yes, Confirm', 'Yes, Continue']

        if answer in select_home:
            self.go_home()

        if answer == 'Quit Program':
            self.quit_program()

        if answer in select_results:
            self.results(zip_code)

        if answer == "No, Re-Enter":
            self.enter_zip()

        if answer == "None of that, just give me a dad joke.":
            self.dad_joke()

        if answer == 'ENTER ZIP':
            self.enter_zip()

        if answer == 'AUTO ZIP (**NEW FEATURE NOT VPN COMPATIBLE**)':
            self.auto_zip()

    @staticmethod
    def quit_program() -> None:
        """ The quit program function """
        os.system('clear')
        os.system('exit')

    def go_home(self) -> None:
        """ The go home function """
        os.system('clear')
        self.main()


if __name__ == "__main__":
    main = CycleDad()
