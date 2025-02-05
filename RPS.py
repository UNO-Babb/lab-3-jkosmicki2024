#RPS.py
#Name:Jacob Kosmicki
#Date: 2/5/2025
#Assignment: RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  import random

import random

def main():
    playagain = "Y"
    wins = 0
    ties = 0
    losses = 0

    while playagain == "Y":
        computer = random.choice(["R", "P", "S"])
        player = input("Choose one (R, P, S): ").upper()

        if computer == "R":
            print("Computer picked rock")
        elif computer == "P":
            print("Computer picked paper")
        elif computer == "S":
            print("Computer picked scissors")

        if player == computer:
            print("Tie")
            ties += 1
        elif player == "R" and computer == "S":
            print("You win")
            wins += 1
        elif player == "R" and computer == "P":
            print("You lose")
            losses += 1
        elif player == "P" and computer == "R":
            print("You win")
            wins += 1
        elif player == "P" and computer == "S":
            print("You lose")
            losses += 1
        elif player == "S" and computer == "P":
            print("You win")
            wins += 1
        elif player == "S" and computer == "R":
            print("You lose")
            losses += 1

        playagain = input("Play again? (Y/N): ").upper()

    # Print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties, "\t", losses)

if __name__ == '__main__':
    main()

