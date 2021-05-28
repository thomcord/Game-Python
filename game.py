""" Simple game Guess the Number
++++++++++++++++++++++++++++++++
"""

import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it is yours for taking!")

    else:
            print("The current score is {} attempts". format(min(attempts_list)))

def start_game():
    random_number = int(random.ranint(1, 10))
    print("Hello, welcome to the game!")
    player_name = input("What is your name?")
    wanna_play = input("Hi, {}, would you like to play? (Enter Yes/No))" .format(player_name))

    attempts = 0
    show_score ()
    while wanna_play.lower == "yes":
        try:
            guess = input("Pick a number between 1 and 10")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please gues a number within the given range")

            if int(guess) == random_number:
                print("Nice, you got it right!")
            attempts += 1
            attempts_list.append(attempts)
            print("You tried {} times".format(attempts))
            play_again = input("Want to play one more time? (Enter Yes/No")
            
            attempts = 0
            show_score()
            random_number = int(random.randint(1, 10))
            if play_again.lower() == "no":
                print("See you!")
                break
            elif int(guess) > random_number:
                print("It is lower")
                attempts +=1
            elif int(guess) < random_number:
                    print("It is higher")
                    attempts +=1
        except ValueError as err:
                print("Not a valid number, try again")
                print("({})".format(err))
        else:
            print("See you!")
    if __name__ == '_main_':
        start_game()
  
