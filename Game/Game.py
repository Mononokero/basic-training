import random

wins = {"rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["rock", "scissors"]
}

def get_user_choise():
    print("Hello! You`re playing: Rock-paper-scissors-lizard-spock")
    while True:
        user_input = input("Your choice (rock paper scissors lizard spock)?\n")
        if user_input in wins:
            #print("Correct input")
            return user_input
        else:
            print("Invalid input.")


def play_again():
    choice = input("Repeat (Y/N)?")
    try:
        return choice.lower() == 'y'
    except (AttributeError, TypeError, IndexError):
        return False

def game():
    computer_choice = random.choice(list(wins.keys()))
    user_choice = get_user_choise()
    print("Computer choise:", computer_choice)
    if computer_choice in wins[user_choice]:
        print("You win!")
    elif user_choice in wins[computer_choice]:
        print("Computer wins")
    else:
        print("Tie.")

if __name__ == '__main__':
    while True:
        game()
        if not play_again():
            break