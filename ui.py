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
        self.run()
        return 0

    def run(self):
        print("\n")
        print(colored(self.logoText.renderText('CYCLE DAD'), 'cyan'))
        print(self.welcome)
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
                self.results()

            elif 'No, Re-Enter' in answer['user_option']:
                self.enter_zip()

            elif 'Go Back' in answer['user_option']:
                self.go_home()

            else:
                self.quit_program()

    @staticmethod
    def validate_zip(entered_zip):
        if entered_zip.isnumeric() and len(entered_zip) == 7:
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
        print(colored(' ZIPCODE', 'cyan'))
        # TODO: use import socket to get gather IP Address
        # TODO: Find service to convert IP to Zip.
        answers = prompt(self.auto_menu, style=menus.style)

        if 'No, Go Back' in answers['user_option']:
            self.go_home()

        if 'Quit Program' in answers['user_option']:
            self.quit_program()

        if 'Yes, Confirm' in answers['user_option']:
            self.results()

    def dad_joke(self, zip_code=None):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Dad Joke'), 'cyan'))
        print(" DAD JOKE GENERATOR MICROSERVICE\n DAD JOKE WILL GO HERE\n")
        answers = prompt(self.easy_menu, style=menus.style)
        if "Go Home" in answers['user_option']:
            self.go_home()
        if "Quit Program" in answers['user_option']:
            self.quit_program()

    def results(self):
        os.system('clear')
        print("\n")
        print(colored(self.logoText.renderText('Results'), 'cyan'))
        print(colored("\n RESULTS WILL GO HERE \n", 'cyan'))
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
