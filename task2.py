import random

def get_user_choice():
    choice = input("Rock, Paper, or Scissors? ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return 0
    elif user == "rock" and computer == "scissors":
        return 1
    elif user == "scissors" and computer == "paper":
        return 1
    elif user == "paper" and computer == "rock":
        return 1
    else:
        return -1

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"Computer chose: {computer}")
        result = determine_winner(user, computer)
        print("You Win!" if result==1 else "You Lose!" if result==-1 else "It's a Tie!")
        
        if result==1:
            user_score += 1
        elif result==-1:
            computer_score += 1
        
        print(f"Score: You {user_score} - Computer {computer_score}")
        
        if input("Play again? (y/n): ").lower() != "y":
            break

play_game()