def game_grid(matrix_):
    print("---------")
    print("|", *matrix_[0], "|")
    print("|", *matrix_[1], "|")
    print("|", *matrix_[2], "|")
    print("---------")


user = input("Enter cells:")
row_list = [[j for j in user[i:i + 3]] for i in range(0, 7, 3)]
col_list = [[j for j in user[i::3]] for i in range(3)]
diagonal_list = [[row_list[i][i] for i in range(3)]] + [[row_list[i][2 - i] for i in range(3)]]
matrix = row_list + col_list + diagonal_list
game_grid(matrix)

x_win = ["X", "X", "X"]
o_win = ["O", "O", "O"]
count_x = user.count("X")
count_o = user.count("O")

valid = False
while not valid:
    row, col = input("Enter the coordinates: ").split()
    try:
        row, col = int(row), int(col)
        if 1 <= row <= 3 and 1 <= col <= 3:
            if "_" in row_list[row - 1][col - 1]:
                row_list[row - 1][col - 1] = "X"
                game_grid(row_list)
                valid = True
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("You should enter numbers!")
