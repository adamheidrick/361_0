from PyInquirer import Separator, style_from_dict, Token

welcome = ' Welcome to Cycle Dad! \n\n This program will give you a clothing recommendation \n' \
                       ' based on your weather so you can plan that epic ride. \n' \
                       ' You can input your own zip code or it can be automatically generated. \n' \
                       ' Or . . . you can just have a dad joke if you want. Cheers. \n'

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

home_menu = [
            {
                'type': 'list',
                'qmark': ' #',
                'message': ' CycleDad: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ==  How would you like to enter your zip?  =='),
                    {
                        'name': 'I want you to automatically find my zip.'
                    },
                    {
                        'name': 'I want to enter my own.'
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
                'type': 'input',
                'qmark': ' #',
                'name': 'zip',
                'message': 'What is your zip (5 digits): '
            },

            {
                'type': 'list',
                'qmark': ' #',
                'message': ' CycleDad: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ======== Continue, Redo, GoBack, DadJoke, Quit =========='),
                    {
                        'name': 'Continue.'
                    },
                    {
                        'name': 'Redo.'
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

dad_menu = [
            {
                'type': 'list',
                'qmark': ' #',
                'message': ' Easy Nav: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ======== Go Home, Quit =========='),
                    {
                        'name': 'Go Home.'
                    },

                    {
                        'name': 'Quit Program.'
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
