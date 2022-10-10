from PyInquirer import Separator

welcome = ' Welcome to Cycle Dad! \n\n This program will give you a clothing recommendation \n' \
                       ' based on your weather so you can plan that epic ride. \n' \
                       ' You can input your own zip code or it can be automatically generated. \n' \
                       ' Or . . . you can just have a dad joke if you want. Cheers. \n'

home_menu = [
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
                'qmark': '#',
                'name': 'zip',
                'message': 'What is your zip (5 digits): '
            },

            {
                'type': 'list',
                'qmark': '#',
                'message': ' CycleDad: ',
                'name': 'user_option',
                'choices': [
                    Separator('\n ======== Confirm, Redo, GoBack, DadJoke, Quit =========='),
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
