from __future__ import print_function, unicode_literals

import os
from pprint import pprint
from prompt_toolkit.validation import Validator, ValidationError

from pyfiglet import Figlet
from PyInquirer import prompt, Separator


class CycleDad:
    def __init__(self):
        self.logoText = Figlet(font='speed')
        self.welcome = 'Welcome to Cycle Dad!'
        self.home_menu = [
            {
                'type': 'list',
                'qmark': '#',
                'message': ' CycleDad: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ==  How would you like to enter your zip?  =='),
                    {
                        'name': 'I want you to automatically find my zip.'
                    },
                    {
                        'name': 'Woah! I want to enter my own.'
                    },
                    {
                        'name': 'None of that, just give me a dad joke.'
                    },
                    {
                        'name': 'Quit Program'
                    }
                ]
            }

        ]
        self.zip_menu = [
            {
                'type': 'input',
                'name': 'zip',
                'message': 'What is your zip (5 digits): '
            },

            {
                'type': 'list',
                'qmark': '#',
                'message': ' CycleDad: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ==  Is this working?  =='),
                    {
                        'name': 'Continue.'
                    },
                    {
                        'name': 'Go Back.'
                    },
                    {
                        'name': 'None of that, just give me a dad joke.'
                    },
                    {
                        'name': 'Quit Program'
                    }
                ]
            }





        ]


        self.init = self.main()

    def main(self):
        os.system('clear')
        print("\n")
        print(self.logoText.renderText('  CYCLE DAD'))
        self.run()

    def run(self):
        answers = prompt(self.home_menu)
        if 'Quit Program' in answers['user_option']:
            os.system('exit')
        else:
            self.parse_answers(answers)

    def parse_answers(self, answers):
        answer = answers['user_option']
        if answer == 'Woah! I want to enter my own.':
            self.enter_zip()

        elif answer == 'I want you to automatically find my zip.':
            pass

        else:
            pass

    def enter_zip(self):
        print("")
        answer = prompt(self.zip_menu)
        pass



if __name__ == "__main__":
    main = CycleDad()
