import random

print("Hello! Do you want to play Rock, Paper, Scissors? (yes or no)")
game = ["rock", "paper", "scissors"]
answer = "yes"
while answer.lower != "no":
  answer = input()
  if answer == "yes" or answer == "no":
    break
  print("That was not an option. Try again!")

while answer == "yes":
  print("Pick rock, paper, or scissors")
  option = input()
  if option == "rock":
    rock_opponent = random.choice(game)
    if rock_opponent == "rock": print("Computer chose rock. Tie Game.")
    elif rock_opponent == "paper": print("Computer chose paper. You lose.")
    else: print("Computer chose scissors. You win!")
  elif option == "paper":
    paper_opponent = random.choice(game)
    if paper_opponent == "rock": print("Computer chose rock. You win!")
    elif paper_opponent == "paper": print("Computer chose paper. Tie game.")
    else: print("Computer chose scissors. You lose.")
  elif option == "scissors":
    scissors_opponent = random.choice(game)
    if scissors_opponent == "rock": print("Computer chose rock. You lose.")
    elif scissors_opponent == "paper": print("Computer chose paper. You Win!")
    else: print("Computer chose scissors. Tie game.")
  else: print("That is not an option for the game...")

  print("Do you want to play again? (yes or no)")
  rematch = input()
  if rematch == "no": break

print("Thank you! Goodbye!")
