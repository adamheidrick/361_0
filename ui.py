import os
from pyfiglet import Figlet
from PyInquirer import prompt

logoText = Figlet(font='speed')
welcome = 'Welcome to Cycle Dad!'

questions = [
    {
        'type': 'list',
        'name': 'user_option',
        'message': 'Welcome to Cycle Dad!',
        'choices': ["Get My Zip", "Enter My Zip"]
    }

]


def main():
    print(logoText.renderText('CYCLE DAD'))


if __name__ == "__main__":
    main()
