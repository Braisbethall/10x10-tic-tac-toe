import random
import numpy as np


grid = [["-" for i in range(10)] for j in range(10)]
grid_elements = []
for cell in grid:
    grid_elements.extend(cell)
digits = list("0123456789")
total_moves = 100


def print_grid():
    print(" ", *digits)
    row_index = 0
    for row in grid:
        print(row_index, end=" ")
        for element in row:
            print(element, end=" ")
        print()
        row_index += 1


def generate_losing_sets():
    vertical_nums = [grid[i][j] for j in range(10) for i in range(10)]
    vertical_sets = [[x for x in vertical_nums[y:y + 10]] for y in range(0, 100, 10)]
    horizontal_sets = [x for x in grid]
    a = np.array(grid)
    diagonals = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
    diagonals.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
    diagonal_sets = [n.tolist() for n in diagonals]
    return vertical_sets + horizontal_sets + diagonal_sets


def win_check():
    losing_sets = generate_losing_sets()
    x_streak = 0
    o_streak = 0
    for set_ in losing_sets:
        for sign in set_:
            if sign == "X":
                x_streak += 1
                if x_streak == 5:
                    return "0 wins"
            else:
                x_streak = 0
            if sign == "0":
                o_streak += 1
                if o_streak == 5:
                    return "X wins"
            else:
                o_streak = 0


print_grid()
which_move = 2
while total_moves > 0:
    if which_move % 2 == 0:
        coordinates = input("Enter the coordinates through a space: ").split()
        if len(coordinates) != 2 or coordinates[0] not in digits or coordinates[1] not in digits:
            print("You should enter two single digits!")
            continue
        elif grid[int(coordinates[0])][int(coordinates[1])] != "-":
            print("This cell is occupied! Choose another one!")
            continue
    else:
        print("Time to computer make a move:")
        while True:
            coordinates = [random.randint(0, 9), random.randint(0, 9)]
            if grid[coordinates[0]][coordinates[1]] == "-":
                break
    grid[int(coordinates[0])][int(coordinates[1])] = "X" if which_move % 2 == 0 else "0"
    grid_elements[(int(coordinates[0]) * 10) + int(coordinates[1])] = "X" if which_move % 2 == 0 else "0"
    total_moves -= 1
    which_move += 1
    print_grid()
    if win_check():
        print(win_check())
        break
else:
    print("Draw")