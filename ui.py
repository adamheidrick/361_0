from __future__ import print_function, unicode_literals

import os
import menus

from termcolor import colored
from pyfiglet import Figlet
from PyInquirer import prompt


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
        print("\n")
        print(colored(self.logoText.renderText('CYCLE DAD'), 'cyan'))
        print(self.welcome)
        self.run()
        return 0

    def run(self):
        answers = prompt(self.home_menu, style=menus.style)
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
            self.auto_zip()

        else:
            pass

    def enter_zip(self):
        os.system('clear')
        print(colored(self.logoText.renderText('Enter Zip'), 'cyan'))
        answer = prompt(self.zip_menu, style=menus.style)
        if 'Go Back' in answer['user_option']:
            os.system('clear')
            self.main()

        if 'Redo' in answer['user_option']:
            self.enter_zip()

        if "Continue." in answer['user_option']:
            self.results()

    def auto_zip(self):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Auto Zip'), 'cyan'))
        print(" AUTO ZIP MICROSERVICE. YOUR ZIP IS:")
        print(colored(' ZIPCODE', 'green'))
        # TODO: use import socket to get gather IP Address
        # TODO: Find service to convert IP to Zip.
        answers = prompt(self.auto_menu, style=menus.style)
        pass

    def dad_joke(self, zip_code=None):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Dad Joke'), 'cyan'))
        print(" DAD JOKE GENERATOR MICROSERVICE\n DAD JOKE WILL GO HERE\n")
        answers = prompt(self.easy_menu, style=menus.style)

        if zip_code is None:
            # Find zip based off of IP
            pass
        else:
            # API weather app MICROSERVICE
            pass

    def results(self):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Results'), 'cyan'))
        answers = prompt(self.easy_menu, style=menus.style)

        pass


if __name__ == "__main__":
    main = CycleDad()
