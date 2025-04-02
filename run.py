import os
import random

# configure BattleshipGame Class object
class BattleshipGame:
    def __init__(self):
        self.LENGTH_OF_SHIPS = [2, 3, 3, 4, 5]
        self.PLAYER_BOARD = [[" "] * 10 for _ in range(10)]
        self.COMPUTER_BOARD = [[" "] * 10 for _ in range(10)]
        self.PLAYER_GUESS_BOARD = [[" "] * 10 for _ in range(10)]
        self.COMPUTER_GUESS_BOARD = [[" "] * 10 for _ in range(10)]
        self.LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

    # print current state of current player's board
    def print_board(self, board):
        print("  A|B|C|D|E|F|G|H|I|J")
        print("---------------------")
        row_number = 0
        for row in board:
            print('{}|{}'.format(row_number, '|'.join(row)))
            row_number += 1

    # Check that ship placement is not out of range of game board
    def check_ship_fits(self, SHIP_LENGTH, row, column, orientation):
        if orientation == "H":
            return column + SHIP_LENGTH <= 10
        else:
            return row + SHIP_LENGTH <= 10

    def ship_overlaps(self, board, row, column, orientation, ship_length):
        if orientation == "H":
            return any(board[row][i] == "X" for i in range(column, column + ship_length))
        else:
            return any(board[i][column] == "X" for i in range(row, row + ship_length))


    # Place each player's ships on their boards
    def place_ships(self, board):
        for ship_length in self.LENGTH_OF_SHIPS:
            while True:
                if board == self.COMPUTER_BOARD:
                    orientation, row, column = random.choice(["H", "V"]), random.randint(0, 9), random.randint(0, 9)
                    if self.check_ship_fits(ship_length, row, column, orientation) and not self.ship_overlaps(board, row, column, orientation, ship_length):
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
                else:
                    orientation, row, column = random.choice(["H", "V"]), random.randint(0, 9), random.randint(0, 9)
                    if self.check_ship_fits(ship_length, row, column, orientation) and not self.ship_overlaps(board, row, column, orientation, ship_length):
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break

    # Ensure only valid input is entered
    def user_input(self, place_ship):
        while True:
            try:
                row = input("Enter the row 0-9 of the ship: ")
                if row in '0123456789':
                    row = int(row)
                    break
            except ValueError:
                print('Sorry invalid input, please enter a valid letter between 0-9')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHIJ':
                    column = self.LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Sorry invalid input, please enter a valid letter between A-J')
        return row, column

    # Track how many hits the opponent has
    def count_ship_hits(self, board):
        return sum(row.count("X") for row in board)

    # Initiate turn for Player or Computer
    def turn(self, board):
        if board == self.PLAYER_GUESS_BOARD:
            row, column = self.user_input(True)
            if board[row][column] == "-":
                self.turn(board)
            elif board[row][column] == "X":
                self.turn(board)
            # Display message whether target is a Hit or a Miss
            elif self.COMPUTER_BOARD[row][column] == "X":
                print("Player lands Hit!")
                board[row][column] = "X"
            else:
                print("Player Misses")
                board[row][column] = "-"
        else:
            row, column = random.randint(0, 9), random.randint(0, 9)
            if board[row][column] == "-":
                self.turn(board)
            elif board[row][column] == "X":
                self.turn(board)
            # Display message whether target is a Hit or a Miss
            elif self.PLAYER_BOARD[row][column] == "X":
                print("Computer lands Hit!")
                board[row][column] = "X"
            else:
                print("Player Misses")
                board[row][column] = "-"

    def play_game(self, player_name):
        # Display current hits and misses on the player's and computer's boards
        self.place_ships(self.COMPUTER_BOARD)
        self.place_ships(self.PLAYER_BOARD)

        while True:
            # Start Player's turn
            while True:
                print("\n", player_name, "'s turn")
                print('\nPlayers view of Computer Board:')
                self.print_board(self.PLAYER_GUESS_BOARD)
                self.turn(self.PLAYER_GUESS_BOARD)
                break
            if self.count_ship_hits(self.PLAYER_GUESS_BOARD) == 17:
                print("\nCongratulations, you won the game!")
                break

            # Start the Computer's turn
            while True:
                self.turn(self.COMPUTER_GUESS_BOARD)
                break
            print("\nComputers view of ", player_name, " Board:")
            self.print_board(self.COMPUTER_GUESS_BOARD)
            if self.count_ship_hits(self.COMPUTER_GUESS_BOARD) == 17:
                print("\nSorry, the computer won this game")
                break

# Clear current OS terminal output
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_instructions():
    print('''
    The aim of this game is to take out your opponents battleships by entering a selected square on
    the board you think the opponents ships are hiding to win before the opponent eliminates all of
    your ships

    Enter a valid row number between 0-9 and a valid column letter between A-J on your turn then the
    computer enters a random row number and column number for its turn until the a winner is deciceded

    If you wish to exit the program simply close the terminal or hold down the Shift key while pressing C
    ''')
    print("\n")

def main():
    print("Welcome to the Battleships Game program\n")

    # Display game instructions
    game_instructions()

    # Enter a valid player name
    while True:
        player_name = str(input("Please enter your player name with a minimum length of 3 characters: "))

        if len(player_name) < 3:
            print("Sorry invlaid player name, please try again\n")
        else:
            break

    # Continue program until user decides to end the program
    while True:
        # Create an instance of the BattleshipGame class and start the game
        game = BattleshipGame()
        game.play_game(player_name)

        # Clear previous terminal output
        clear_terminal()

        # Check if the user would like to play again
        replay = input("\nEnter 'yes' or 'Y' to play again, otherwise this program will end: ").upper()
        if replay == "YES" or replay == "Y":
            reiterate = input("\nDo you wish to read instructions again?, enter 'yes' or 'Y': ").upper()

            # Reiterate instructions to user
            if reiterate == "YES" or reiterate == "Y":
                game_instructions()

        else:
            # Display goodbye message
            print("Thanks for playing ", player_name, "Goodbye")
            break

# Initiate main program
if __name__ == "__main__":
    main()
