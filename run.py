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
