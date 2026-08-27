# Import the Game class from game.py
from game import Game


# Main function of the application
def main():

    # Create a Game object
    game = Game()

    # Start the game
    game.start()


# This ensures main() runs only when
# this file is executed directly
if __name__ == "__main__":
    main()