import random

valid_input = True

while valid_input:
    cpu_choice = random.choice(["r", "p", "s"])
    player_choice = input("Enter r for Rock, p for Paper or s for Scissors: ")
    player_choice = player_choice.lower()

    if not(player_choice == "r" or player_choice == "p" or player_choice == "s"):
        print("Invalid Input, Please try again.")
    else:
        valid_input = False
        print(f"player ({player_choice}) : CPU ({cpu_choice})")

    if cpu_choice == player_choice:
        print("It's a tie.")
        valid_input = True
    elif cpu_choice == 'r' and player_choice == 's':
        print('CPU wins!')
    elif cpu_choice == 'p' and player_choice == 'r':
        print("CPU Wins!")
    elif cpu_choice == 's' and player_choice == 'p':
        print("CPU wins")
    elif player_choice == 'r' and cpu_choice == 's':
        print("You Win!")
    elif player_choice == 'p' and cpu_choice == 'r':
        print("You Win!")
    elif player_choice == 's' and cpu_choice == 'p':
        print("You Win!")
