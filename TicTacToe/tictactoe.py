def game_grid(matrix_):
    print("---------")
    print("|", *matrix_[0], "|")
    print("|", *matrix_[1], "|")
    print("|", *matrix_[2], "|")
    print("---------")


def win_check(grid):
    col_list = [[j[i] for j in grid] for i in range(3)]
    diagonal_list = [[grid[i][i] for i in range(3)]] + [[grid[i][2 - i] for i in range(3)]]
    matrix = grid + col_list + diagonal_list
    return matrix


def switch_player(move_):
    if move_ % 2 == 0:
        return "X"
    return "O"


def main():
    global running
    matrix = []
    row_list = [[" " for _ in range(i, i + 3)] for i in range(0, 7, 3)]
    game_grid(row_list)
    x_win = ["X", "X", "X"]
    o_win = ["O", "O", "O"]
    move = 0

    while running:
        try:
            row, col = input("Enter the coordinates: ").split()
            row, col = int(row), int(col)
            if 1 <= row <= 3 and 1 <= col <= 3:
                if " " in row_list[row - 1][col - 1]:
                    row_list[row - 1][col - 1] = switch_player(move)
                    game_grid(row_list)
                    move += 1
                    matrix += win_check(row_list)
                    if o_win in matrix:
                        print("O win")
                        running = False
                    elif x_win in matrix:
                        print("X win")
                        running = False
                    elif move == 9:
                        print("Draw")
                        running = False
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")


if __name__ == '__main__':
    running = True
    main()
