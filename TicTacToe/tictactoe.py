def game_grid(matrix_):
    print("---------")
    print("|", *matrix_[0], "|")
    print("|", *matrix_[1], "|")
    print("|", *matrix_[2], "|")
    print("---------")


user = input("Enter cells: ")
row_list = [[j for j in user[i:i+3]] for i in range(0, 7, 3)]
col_list = [[j for j in user[i::3]] for i in range(3)]
diagonal_list = [[row_list[i][i] for i in range(3)]] + [[row_list[i][2 - i] for i in range(3)]]
matrix = row_list + col_list + diagonal_list
game_grid(matrix)

x_win = ["X", "X", "X"]
o_win = ["O", "O", "O"]
count_x = user.count("X")
count_o = user.count("O")

if (o_win in matrix and x_win in matrix) or abs(count_x - count_o) > 1:
    print("Impossible")
elif o_win in matrix:
    print("X win")
elif x_win in matrix:
    print("O win")
elif "_" in user:
    print("Game not finished")
else:
    print("Draw")
