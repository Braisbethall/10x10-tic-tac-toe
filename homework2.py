import random
import numpy as np


grid = [["-" for i in range(10)] for j in range(10)]
grid_elements = []
for cell in grid:
    grid_elements.extend(cell)
digits = list("1234567890")
total_moves = 100


def print_grid():
    print(f"""  0 1 2 3 4 5 6 7 8 9
0 {grid[0][0]} {grid[0][1]} {grid[0][2]} {grid[0][3]} {grid[0][4]} {grid[0][5]} {grid[0][6]} {grid[0][7]}\
 {grid[0][8]} {grid[0][9]}
1 {grid[1][0]} {grid[1][1]} {grid[1][2]} {grid[1][3]} {grid[1][4]} {grid[1][5]} {grid[1][6]} {grid[1][7]}\
 {grid[1][8]} {grid[1][9]}
2 {grid[2][0]} {grid[2][1]} {grid[2][2]} {grid[2][3]} {grid[2][4]} {grid[2][5]} {grid[2][6]} {grid[2][7]}\
 {grid[2][8]} {grid[2][9]}
3 {grid[3][0]} {grid[3][1]} {grid[3][2]} {grid[3][3]} {grid[3][4]} {grid[3][5]} {grid[3][6]} {grid[3][7]}\
 {grid[3][8]} {grid[3][9]}
4 {grid[4][0]} {grid[4][1]} {grid[4][2]} {grid[4][3]} {grid[4][4]} {grid[4][5]} {grid[4][6]} {grid[4][7]}\
 {grid[4][8]} {grid[4][9]}
5 {grid[5][0]} {grid[5][1]} {grid[5][2]} {grid[5][3]} {grid[5][4]} {grid[5][5]} {grid[5][6]} {grid[5][7]}\
 {grid[5][8]} {grid[5][9]}
6 {grid[6][0]} {grid[6][1]} {grid[6][2]} {grid[6][3]} {grid[6][4]} {grid[6][5]} {grid[6][6]} {grid[6][7]}\
 {grid[6][8]} {grid[6][9]}
7 {grid[7][0]} {grid[7][1]} {grid[7][2]} {grid[7][3]} {grid[7][4]} {grid[7][5]} {grid[7][6]} {grid[7][7]}\
 {grid[7][8]} {grid[7][9]}
8 {grid[8][0]} {grid[8][1]} {grid[8][2]} {grid[8][3]} {grid[8][4]} {grid[8][5]} {grid[8][6]} {grid[8][7]}\
 {grid[8][8]} {grid[8][9]}
9 {grid[9][0]} {grid[9][1]} {grid[9][2]} {grid[9][3]} {grid[9][4]} {grid[9][5]} {grid[9][6]} {grid[9][7]}\
 {grid[9][8]} {grid[9][9]}""")


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
    print(generate_losing_sets())
    if win_check():
        print(win_check())
        break
else:
    print("Draw")
