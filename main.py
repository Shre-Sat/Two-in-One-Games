from game_logic.engine import play_stone_paper_scissors, play_dice_roll

def main():
    while True:
        print("\n============================")
        print("      GAME CENTER MENU      ")
        print("============================")
        print("1. Play Stone – Paper – Scissors")
        print("2. Play Dice Roll Game")
        print("3. Exit Program")
        print("----------------------------")
        
        choice = input("Select an option (1-3): ")

        if choice == "1":
            play_stone_paper_scissors()
        elif choice == "2":
            play_dice_roll()
        elif choice == "3":
            print("Exiting... Good luck with your Pre-Mocks!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()