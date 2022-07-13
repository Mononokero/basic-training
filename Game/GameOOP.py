import random

class Player:

    def get_player_choice(self):
        user_input = input("Choose your gesture (rock paper scissors lizard spock)? \n>>> ")
        return user_input


class Computer:
    def __init__(self):
        self.choices = ["rock", "scissors", "lizard", "paper", "spock"]

    def get_random_choice(self):
        return random.choice(self.choices)


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.wins = {"rock": ["scissors", "lizard"],
                     "paper": ["rock", "spock"],
                     "scissors": ["paper", "lizard"],
                     "lizard": ["spock", "paper"],
                     "spock": ["rock", "scissors"]}

    def __check_input(self, choice):
        if choice in self.wins:
            return True
        return False

    def __check_win_condition(self, choice1, choice2):
        if choice2 in self.wins[choice1]:
            return True
        return False

    def play(self):
        print(
            "Hello! You`re playing: Rock-paper-scissors-lizard-spock.\n")
        player_input = self.player.get_player_choice()
        while True:
            if self.__check_input(player_input):
                break
            else:
                print("Invalid input. Please choose your gesture (rock paper scissors lizard spock)?\n")
                player_input = self.player.get_player_choice()

        print("Player`s choice:", player_input)

        computer_input = self.computer.get_random_choice()
        print("Computer`s choice:", computer_input)

        if self.__check_win_condition(player_input, computer_input):
            print("Player wins!")
        elif self.__check_win_condition(computer_input, player_input):
            print("Computer wins")
        else:
            print("Tie.")




def run():
    player = Player()
    computer = Computer()
    game = Game(player, computer)

    while True:
        choice = input("Let's play? (Y/N)?\n >>> ")
        if choice == "y":
            game.play()
        elif choice == "n":
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    run()