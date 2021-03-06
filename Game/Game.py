import random

wins = {"rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["rock", "scissors"]
}


def get_user_choice():
    print("Hello! You`re playing: Rock-paper-scissors-lizard-spock")
    while True:
        user_input = input("Choose your gesture (rock paper scissors lizard spock)?\n")
        if user_input in wins:
            print("Player`s choice:", user_input)
            return user_input
        else:
            print("Invalid input.")


def play_again():
    while True:
        choice = input("Repeat (Y/N)?")
        if choice == "y":
            game()
            continue
        elif choice == "n":
            break
        else:
            print("Invalid input")



def game():
    computer = random.choice(list(wins.keys()))
    user = get_user_choice()
    print("Computer`s choice:", computer)
    if computer in wins[user]:
        print("Player win!")
    elif user in wins[computer]:
        print("Computer wins")
    else:
        print("Tie.")

if __name__ == '__main__':
    while True:
        game()
        if not play_again():
            break