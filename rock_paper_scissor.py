import random

game = ["rock", "paper", "scissor"]

wanna_play = input("Do you wanna play?('yes' or 'no') ").lower()

while True:
    if wanna_play == 'yes':
        user = input(f"\nChoose {game} or 'q' to quit\nyour turn : ").lower()

        # 1. Check for quit immediately
        if user == 'q':
            break
            
        # 2. Validate input before computer moves
        if user not in game:
            print("Invalid choice")
            continue  # Skips the rest of the loop and asks again

        computer = random.choice(game)
        print(f"computer turn : {computer}")
        
        # 3. Game Logic
        if user == computer:
            print("Tie")
        elif (user == "rock" and computer == "paper"):
            print("Computer Win")
        elif (user == "paper" and computer == "scissor"):
            print("Computer Win")
        elif (user == "scissor" and computer == "rock"):
            print("Computer Win")
        else:
            print("User Win")

    else:
        break

print("Have a great day!")