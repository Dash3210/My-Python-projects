#Quick Quiz game
import threading, random, sys

def get_equation():#Generating random equation/numbers
    a, b = random.randint(10, 99), random.randint(10, 99)
    return a, b, a + b


def get_input(prompt, timeout):#Time boom, Answer in specific secs or lose
    user_input = [None]
    def input_W_timeout():
        user_input[0] = input(prompt)
    input_thread = threading.Thread(target=input_W_timeout)
    input_thread.start()#Starting clock
    input_thread.join(timeout)

    if input_thread.is_alive():# If thread still alive after timer then...
        print('\nBOOM')
        return 0
    else:
        return user_input[0]

money = 100
while True:# Main game loop
    a, b, c = get_equation()
    Structure = 'What is the answer of ' + str(a) + ' + ' + str(b) + '\n>'
    print('Money=', money)
    response = get_input(Structure, 5) # You have 5 secs to answer
    if response != 0:# If got response
        if response == str(c):
            print('good')
            money += 10
        else:# If response is wrong
            print('Wrong!! The answer was ', c)
            money -= 11
    else:# If timeout is true
        print('Timeout!! The answer was ', c)
        money -= 12

    if money >= 11:
        Decision = input('Do you want to continue(press enter to continue or N to leave)?\n>')
        if Decision.upper() == 'N':
            sys.exit()
    else:#Negative money not possible
        print('You\'ve lost most of your money, you can\'t afford to lose more GTFO')
        sys.exit()