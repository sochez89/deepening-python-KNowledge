import random
from random import choice

print("Select from the options below")
print("------OPTIONS--------")
print("select  'R' for rock" )
print(" Select 'P' for paper")
print(" Select 'S' for scissors")
print(" Select 'Q' to quit")
possible_actions = ['R', 'P', 'S']

while True:
    possible_actions = ['R', 'P', 'S']
    CPU = random.choice(possible_actions)
    Player = (input("Your option: ")).upper()
    if ( (Player == 'R' and CPU == 'R')|(Player == 'P' and CPU == 'P') | (Player == 'S' and CPU == 'S')):
        print(f"It's a tie! Both players selected {Player}. ")
    elif Player == "R":
        if CPU =="scissors":
            print("Player won! Rock smashes scissors! ")
            break
        else:
            print("CPU won! Paper covers rock.")
            break
    elif Player =='P':
        if CPU == 'R':
            print("Player won! Paper covers rock! ")
            break
        else:
            print("CPU won! Scissors cuts paper.")
            break
    elif Player == 'S':
        if CPU == 'P':
            print("Player won! Scissors cuts paper! ")
            break
        else:
            print(" CPU won! Rock smashes scissors.")
            break
    elif Player == 'Q':
        print("Game over!")
        break
    elif Player != possible_actions:
        print(" Error! Select Appropriate Option")
        print("------OPTIONS--------")
        print("select  'R' for rock" )
        print(" Select 'P' for paper")
        print(" Select 'S' for scissors")
        print(" Select 'Q' to quit")