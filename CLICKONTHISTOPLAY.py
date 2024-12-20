import sys

def main():
    print("Welcome to Piano Tiles!")
    print("Please choose a game to play:")
    print("1. Game 1: Jingle Bells")
    print("2. Game 2: We Wish You a Merry Christmas")

    choice = input("Enter the number of the game you want to play (1 or 2): ")

    if choice == '1':
        import game1
        game1.play_game1()
    elif choice == '2':
        import game2
        game2.main()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit()

if __name__ == "__main__":
    main()