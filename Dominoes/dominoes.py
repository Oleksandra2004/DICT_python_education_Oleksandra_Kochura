import random


def generate_stock():
    return [[i, j] for j in range(0, 7) for i in range(j, 7)]


def split_dominoes(dominoes):
    num_of_dominoes = 7
    choice = random.sample(dominoes, num_of_dominoes)
    for x in choice:
        dominoes.remove(x)
    return choice


def snake_check(player, cpu):
    player_max = max([[x, y] for x, y in player])
    cpu_max = max([[x, y] for x, y in cpu])
    if player_max > cpu_max:
        status_ = "computer"
        max_domino = player.pop(player.index(player_max))
        return status_, max_domino
    else:
        status_ = "player"
        max_domino = cpu.pop(cpu.index(cpu_max))
        return status_, max_domino


def game_status(status_):
    if status_ == "computer":
        return "Status: Computer is about to make a move. Press Enter to continue..."
    elif status_ == "player":
        return "Status: It's your turn to make a move. Enter your command."


def interface():
    header_count = 70
    print("=" * header_count)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(cpu_dominoes)}\n")
    print(f"{domino_snake}\n")
    print(f"Your pieces:", *[f'{i}:{domino}' for i, domino in enumerate(sorted(player_dominoes), 1)], sep="\n")
    print(game_status(status))


stock_pieces = generate_stock()
player_dominoes, cpu_dominoes = split_dominoes(stock_pieces), split_dominoes(stock_pieces)
status, domino_snake = snake_check(player_dominoes, cpu_dominoes)
interface()