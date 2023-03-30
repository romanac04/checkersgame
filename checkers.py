from numpy import random
import numpy as np
def build_board(size):
    board = random.choice(['Empty', 'Red', 'Black'], size=(size, size))
    return board
def get_count(board, item):
        count = 0
        for row in board:
            for cell in row:
                if cell == item:
                    count += 1
        return count
def resize_board(board, new_size):
    board = np.resize(board, (new_size, new_size))
    return board

def pivot_board(board):
    pivoted_board = np.transpose(board)
    return pivoted_board

if __name__ == "__main__":
        print("This file is not intended to be run as a main.")


