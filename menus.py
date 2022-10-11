from PyInquirer import Separator, style_from_dict, Token
from termcolor import colored

new_feature = colored('    (Auto Zip is new and saves time but may not work if VPN in use!', 'green')
auto_zip = colored(' This is new but may not work with VPN!', 'green')

welcome = ' Welcome to Cycle Dad! \n\n This program will give you a clothing recommendation \n' \
                       ' based on your weather so you can plan that epic ride in four easy steps:. \n\n' \
                       ' 1. Select AUTO ZIP or ENTER ZIP from the menu below. \n' \
                       f"{new_feature}\n" \
                       ' 2. Confirm your zip code. \n' \
                       ' 3. See your clothing recommendation results and dress accordingly. \n' \
                       ' 4. Drink water to stay hydrated. \n'


style = style_from_dict({
    Token.Separator: '#9ff436',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#33abab',  # default
    Token.Pointer: '#9ff436 bold',
    Token.Instruction: '#9ff436',  # default
    Token.Answer: '#36f492 bold',
    Token.Question: '',
})

home_menu = [
            {
                'type': 'list',
                'qmark': ' \u2192',
                'message': ' Easy Nav: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ==  How would you like to enter your zip?  =='),
                    {
                        'name': 'AUTO ZIP (**NEW FEATURE NOT VPN COMPATIBLE**)'
                    },
                    {
                        'name': 'ENTER ZIP'
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

zip_menu = [

            {
                'type': 'list',
                'qmark': ' #',
                'message': ' CycleDad: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ======== Is the Zip Code Correct? =========='),
                    {
                        'name': 'Yes, Continue'
                    },
                    {
                        'name': 'No, Re-Enter'
                    },

                    {
                        'name': 'Go Back'
                    },
                    {
                        'name': 'Quit Program'
                    }
                ]
            }
        ]

dad_menu = [
            {
                'type': 'list',
                'qmark': ' #',
                'message': ' Easy Nav: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ======== Go Home, Quit =========='),
                    {
                        'name': 'Go Home'
                    },

                    {
                        'name': 'Quit Program'
                    }
                ]
            }
        ]

auto_menu = [
            {
                'type': 'list',
                'qmark': ' #',
                'message': ' Easy Nav: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ======== Is the Zip Code Correct? =========='),
                    {
                        'name': 'Yes, Confirm'
                    },
                    {
                        'name': 'No, Go Back'
                    },
                    {
                        'name': 'Quit Program'
                    }
                ]
            }
        ]
