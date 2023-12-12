import random

print("Welcome to the game!")

player_select = input("Enter 'rock', 'scissors' or 'paper':")
choice = ["rock", "scissors", "paper"]
print(player_select)

computer_select = random.choice(choice)
print(computer_select)

if player_select not in choice:
    print("Error value")
    exit()

if player_select == computer_select:
    print("Draw!")
    print("Thanks for the game!")

if ((player_select == "rock" and computer_select == "scissors") or
    (player_select == "paper" and computer_select == "rock") or
        (player_select == "scissors" and computer_select == "paper")):
    print("Congratulations!You win!")
    print("Thanks for the game!")

elif ((player_select == "rock" and computer_select == "paper") or
      (player_select == "paper" and computer_select == "scissors") or
      (player_select == "scissors" and computer_select == "rock")):
    print("The computer wins!")
    print("Thanks for the game!")
