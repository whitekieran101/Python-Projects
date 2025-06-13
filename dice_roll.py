"""UNDERSTAND:

Write a function to simulate throwing a cubic dice.  Use your function to
write another function to simulate a gambling game with the following conditions.

1. If the combined rolled values is 12, the gambler gets the highest price of
   10 times the gambled(bet) amount of money
2. If the combined rolled values is 8, the gambler looses the bet
3. If the combined rolled values is 11, the gambler gets 2 times the gambled
   (bet) amount of money
4. Any other combined values, and the gambler must play again upon receiving a message .
   asking to play again.

gambled money = $1000

call function 5 times in main()

inputs: two randomized numbers 1-6
output: result of the two dice roll and the players winnings/losses.


1. create a function that randomly generates an int between 1 and 6
    1.1 - dice_roll = random.randint(1, 6)
2. create a function that simulates a gambling game
    2.1 - call first function twice to determine the dice roll #s
    2.2 - create if statement for combined value of 8
    2.3 - create elif statement for combined value of 11
    2.4 - create elif statement for combined value of 12
    2.5 - create else statement for all other combined values
3. call gambling game function 5 tines in main()
"""

import random

def simulate_dice():
    dice_roll = random.randint(1, 6)
    return dice_roll

def simulate_gambling(money_bet):
    gambling_results = simulate_dice() + simulate_dice()

    if gambling_results == 8:
        return f'Your dice rolls were equal to 8, you lose your bet.'
    elif gambling_results == 11:
        return f'Your dice rolls were equal to 11, you win! Your bet is now = ${money_bet * 2}'
    elif gambling_results == 12:
        return f'Your dice rolls were equal to 12, you win! Your bet is now = ${money_bet * 10}'
    else:
        return f'Your dice rolls were not equal to 8, 11, or 12; Please play again.'


def main():

    money_bet = 1000

    print(simulate_gambling(money_bet))

if __name__ == '__main__':
    main()


