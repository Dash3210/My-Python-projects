# Cho_Hin game 
import random, sys

Japanese_Numbers = {1: 'Ichi', 2: 'Ni', 3: 'San',
                    4: 'Shi',  5: 'Go', 6: 'Roku'}

print('Cho-Han Game of odd or even, simple guess the total game.')

purse = 5000
win = 0
loss = 0
while True:
    #How mch does the player want to bet?
    print('You have', purse, 'mon, How much do you want to bet?(OR (q)uit)')
    while True:
        bet = input('>').lower()
        if bet.startswith('q'):
            print('Thanks for playing:)')
            sys.exit()
        elif not bet.isdecimal or bet == '':
            print('Please enter a valid response')
        elif int(bet) > purse:
            print('You\'re for that kind of bet')
        else:
            #valid bet
            bet = int(bet)
            break

    Dice_1 = random.randint(1, 6)
    Dice_2 = random.randint(1, 6)

    Roll_Even = (Dice_2 + Dice_1)%2 == 0

    if Roll_Even:
        Answer_Bet = 'CHO'
    else:
        Answer_Bet = 'HAN'
    #A cheat because I always want to win!
    if Answer_Bet == 'CHO':
        print('Dealer makin\' game sounds and bams the cup of dice and asks you: "CHO" OR "HAN"')
    elif Answer_Bet == 'HAN':
        print('Dealer making game sounds and bams the cup of dice and asks you: "CHO" OR "HAN"')
    
    while True:
        Bet_2 = input('>').upper()
        if Bet_2 != 'CHO' and Bet_2 != 'HAN':
            print('Enter valid response: "CHO" OR "HAN"')
            continue
        else:
            break #valid response

    print('Dealer reveals the dice')
    print(Japanese_Numbers[Dice_1], '-', Japanese_Numbers[Dice_2])
    print(Dice_1, '-', Dice_2)
    
    #Determining if player won or lost
    Player_Won = Answer_Bet == Bet_2
    if Player_Won:
        purse = purse + bet - (bet//10)
        print('You\'ve won \nHouse collects 10 percent so your purse has', purse, 'mon')
        win += 1
    else:
        purse -= bet
        print('You\'ve LOST!!!')
        loss += 1

    #Punishment
    if (win > 4 and loss == 0) or (loss > 0 and loss * 5 <= win and purse >= 50_000) or (purse >= 500_000):
        print('House thinks you\'re cheating, we\'re kicking you out and taking away all your mon.')
        sys.exit()

    if purse == 0:
        print('You\'re Broke MF leave')
        sys.exit()
