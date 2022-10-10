from __future__ import print_function, unicode_literals

import os
import menus
from termcolor import colored
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError

from pyfiglet import Figlet
from PyInquirer import prompt


class CycleDad:
    def __init__(self):
        self.logoText = Figlet(font='speed')
        self.welcome = menus.welcome
        self.home_menu = menus.home_menu
        self.zip_menu = menus.zip_menu
        self.init = self.main()

    def main(self):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('  CYCLE DAD'), 'yellow'))
        print(self.welcome)
        self.run()
        return 0

    def run(self):
        answers = prompt(self.home_menu)
        if 'Quit Program' in answers['user_option']:
            os.system('clear')
            os.system('exit')

        elif 'None of that, just give me a dad joke.' in answers['user_option']:
            self.dad_joke()

        else:
            self.parse_answers(answers)

    def parse_answers(self, answers):
        answer = answers['user_option']
        if answer == 'I want to enter my own.':
            self.enter_zip()

        elif answer == 'I want you to automatically find my zip.':
            pass

        else:
            pass

    def enter_zip(self):
        os.system('clear')
        print(self.logoText.renderText('  ENTER ZIP'))
        answer = prompt(self.zip_menu)
        if 'Go Back' in answer['user_option']:
            os.system('clear')
            self.main()

        if 'Redo' in answer['user_option']:
            self.enter_zip()

    def auto_zip(self):
        os.system('clear')
        print("\n")
        print(self.logoText.renderText('  Auto Zip Generator'))
        print(" AUTO ZIP MICROSERVICE?")
        # TODO: use import socket to get gather IP Address
        # TODO: Find service to convert IP to Zip.
        pass

    def dad_joke(self, zip_code=None):
        os.system('clear')
        print("\n")
        print(self.logoText.renderText('  Dad Joke'))
        print(" DAD JOKE GENERATOR MICROSERVICE")
        # TODO: Find DAD JOKE API

        if zip_code is None:
            # Find zip based off of IP
            pass
        else:
            # API weather app MICROSERVICE
            pass

        # MENU


if __name__ == "__main__":
    main = CycleDad()
