import random

def play_game():
    options = ['rock', 'paper', 'scissor']

    users_choice = input("Enter your choice: ").lower()

    if users_choice not in options:
        print("Invalid option! Please try again")
        return
    
    computers_choice = random.choice(options)
    print(f"Computer chose: {computers_choice}")
    
    if users_choice == computers_choice:
        print("It's a tie!")
    elif (users_choice == 'rock' and computers_choice == 'scissor') or \
         (users_choice == 'scissor' and computers_choice == 'paper') or \
         (users_choice == 'paper' and computers_choice == 'rock'):
        print("You win!!")
    else:
        print("You lose!!")

play_game()
        
    
         