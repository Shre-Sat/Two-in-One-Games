import random

def play_stone_paper_scissors():
    """Logic for Stone-Paper-Scissors"""
    choices = ["stone", "paper", "scissors"]
    comp = random.choice(choices)
    
    print("\n--- Stone-Paper-Scissors ---")
    user = input("Choose (stone, paper, scissors): ").lower()
    
    if user not in choices:
        print("Invalid choice! Returning to menu...")
        return

    print(f"Computer chose: {comp}")

    if user == comp:
        print("RESULT: It's a tie!")
    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        print("RESULT: You win! 🎉")
    else:
        print("RESULT: Computer wins! 🤖")

def play_dice_roll():
    """Logic for Dice Roll Game"""
    print("\n--- Dice Roll Game ---")
    input("Press Enter to roll the dice...")
    
    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)
    
    print(f"You rolled: {user_roll}")
    print(f"Computer rolled: {comp_roll}")
    
    if user_roll > comp_roll:
        print("RESULT: You win! 🎲")
    elif comp_roll > user_roll:
        print("RESULT: Computer wins!")
    else:
        print("RESULT: It's a draw!")