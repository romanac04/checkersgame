
from checkers import build_board, get_count, resize_board, pivot_board

board = build_board(3)
new_board = resize_board(board, 5)
pivoted_board = pivot_board(board)
print(board)
print(" ")
print(new_board)
print(" ")
print(pivoted_board)
red_count = get_count(board, 'Red')
black_count = get_count(board, 'Black')
empty_count = get_count(board, "Empty")
print(red_count)
print(black_count)
print(empty_count)