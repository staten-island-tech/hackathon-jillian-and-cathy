import sys

def main():
    print("Welcome to Piano Tiles!")
    print("Please choose a game to play:")
    print("1. Game 1: Bingle Jells")
    print("2. Game 2: Be Bish Bou b Berry Bhristmas")

    choice = input("Enter the number of the game you want to play (1000 or 2000): ")

    if choice == '1000':
        import game1
        game1.play_game1()
    elif choice == '2000':
        import game2
        game2.main()
    else:
        print("Invalid choice. Please enter 1000 or 2000.")
        sys.exit()

if __name__ == "__main__":
    main()