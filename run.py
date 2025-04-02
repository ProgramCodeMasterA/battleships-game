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
                    if self.check_ship_fit(ship_length, row, column, orientation) and not self.ship_overlaps(board, row, column, orientation, ship_length):
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
                else:
                    orientation, row, column = random.choice(["H", "V"]), random.randint(0, 9), random.randint(0, 9)
                    if self.check_ship_fit(ship_length, row, column, orientation) and not self.ship_overlaps(board, row, column, orientation, ship_length):
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
                    row = int(row)# - 1
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
    def count_hit_ships(self, board):
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
