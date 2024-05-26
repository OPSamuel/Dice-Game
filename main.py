import random
import time
tries = 0


#Try number 1

def logo():
    print("\nROLLING DICE GAME")
    print("   _______")
    print("  /\ o o o\ ")
    print(" /o \ o o o\_______")
    print("<    >------>   o /|")
    print(" \ o/  o   /_____/o|")
    print("  \/______/     |oo|")
    print("        |   o   |o/")
    print("        |_______|/")
while tries != 1:
    logo()
    print("\nROLL A PAIR TO WIN!")

    input("\nPress enter to roll first dice: ")

    dice1 = random.randint(1,6)
    print("Dice value is", dice1)

    input("\nPress enter to roll second dice: ")

    dice2 = random.randint(1,6)
    print("Dice value is", dice2)

    if dice1 == dice2:
        print("\nCongratulations you rolled a PAIR!")
    else:
        print("\nNot a PAIR - try again!")

    playagain = input("\nWould you like to play again (Yes/No):\n").lower()

    if playagain == "yes":
        pass
    else:
        tries = tries + 1

print("\n**** Program Closing in 5 Seconds ****")
time.sleep(5)
exit(0)
