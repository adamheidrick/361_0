# reads prng service text, if run, then generates random number and writes it to the .txt
from colorama import init
from colorama import Fore, Back, Style
import random
import time
source = 'random-int-request.txt'
destination = 'random-int-receive.txt'

init(autoreset=True)


def main():
    while True:
        time.sleep(1)
        with open(source, 'r') as f:
            value = f.read()
            print('Listening for Request..')

        if value.isnumeric():
            message = 'REQUEST RECEIVED '
            print(f"{Back.GREEN}{message} FOR VALUE: {value}")
            value = int(value)
            with open(destination, 'w') as f:
                randy = str(random.randint(0, value))
                print(f'Writing Random Number to { destination }: ')
                print(f'The random number generated from range 0 -> {value} is the following: ')
                print(f'{Back.GREEN}{randy:_^20}')
                f.write(randy)

            with open(source, 'w') as f:
                f.write('')
                f.close()

        f.close()


if __name__ == "__main__":
    main()

