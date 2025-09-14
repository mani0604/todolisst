import random

choices = ["rock", "paper", "scissors"]

player = input("Enter rock, paper or scissors: ").lower()
computer = random.choice(choices)

print("You chose:", player)
print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") \
     or (player == "paper" and computer == "rock") \
     or (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
