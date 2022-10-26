import time
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)


def main():
    request = 'random-int-request.txt'
    returned_data = 'random-int-receive.txt'
    returned_value = None
    is_running = True
    my_array = ['dog', 'cat', 'mouse', 'elephant', 'zebra']

    while is_running:
        run = int(input("Enter 1 to run program or 2 to quit: "))
        if run == 1:
            with open(request, 'w') as f:
                f.write(str(len(my_array)))
                f.close()
                time.sleep(5)

            with open(returned_data, 'r') as f:
                value = f.read()

            if value.isnumeric():
                with open(returned_data, 'r') as f:
                    message = 'Successful Microservice. Your Random Number is: '
                    returned_value = f.read()
                    print(f'{message}')
                    print(f'{Back.GREEN}{returned_value:_^20}')
                    f.close()

            else:
                comment = 'Failure: Make sure your requested number is converted to a string.'
                print(f'{comment:!^20}')

        elif run == 2:
            is_running = False
            print('End of Program')

        else:
            print('Unknown Command. Please try again.')


if __name__ == "__main__":
    main()
