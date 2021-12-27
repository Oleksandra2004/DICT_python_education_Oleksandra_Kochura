import random


def generate_stock():
    return [[i, j] for j in range(0, 7) for i in range(j, 7)]


def split_dominoes(dominoes):
    num_of_dominoes = 7
    choice = random.sample(dominoes, num_of_dominoes)
    for x in choice:
        dominoes.remove(x)
    return choice


def shuffle_dominoes(dominoes, player, cpu):
    dominoes.clear()
    player.clear()
    cpu.clear()
    dominoes = generate_stock()
    player = split_dominoes(dominoes)
    cpu = split_dominoes(dominoes)
    return dominoes, player, cpu


def pick_first_player(player, cpu):
    player_max = max([[x, y] for x, y in player])
    cpu_max = max([[x, y] for x, y in cpu])
    if player_max > cpu_max:
        status_ = status_set.get(2)
        max_domino = [player.pop(player.index(player_max))]
        return status_, max_domino
    else:
        status_ = status_set.get(1)
        max_domino = [cpu.pop(cpu.index(cpu_max))]
        return status_, max_domino


def game_status(status_):
    if status_ == status_set.get(2):
        return "\nStatus: Computer is about to make a move. Press Enter to continue..."
    elif status_ == status_set.get(1):
        return "\nStatus: It's your turn to make a move. Enter your command."
    elif status_ == status_set.get(3):
        return "\nStatus: The game is over. You won!"
    elif status_ == status_set.get(4):
        return "\nStatus: The game is over. The computer won!"
    elif status_ == status_set.get(5):
        return "\nStatus: The game is over. It's a draw!"


def display_domino_snake():
    if len(domino_snake) > 6:
        left = [str(x) for x in domino_snake[0:3]]
        right = [str(x) for x in
                 domino_snake[:len(domino_snake) - 4:-1]].__reversed__()
        print(f"{''.join(left)}...{''.join(right)}\n")
    else:
        print(f"{''.join(str(x) for x in domino_snake)}\n")


def interface():
    header_count = 70
    print("=" * header_count)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(cpu_dominoes)}\n")
    display_domino_snake()
    print(f"Your pieces:", *[f'{i}:{domino}' for i, domino in
                             enumerate(player_dominoes, 1)], sep="\n")
    print(game_status(status))


def verify_move(choice, dominos):
    side = choice
    choice = abs(choice) - 1
    left_current, right_current = dominos[choice][0], dominos[choice][1]
    left_snake, right_snake = domino_snake[0][0], domino_snake[-1][1]
    if right_current == right_snake and side > 0:
        dominos[choice].reverse()
        return choice
    elif left_current == left_snake and side < 0:
        dominos[choice].reverse()
        return choice
    elif right_current == left_snake and side < 0:
        return choice
    elif left_current == right_snake and side > 0:
        return choice
    else:
        return None


def validate_player(status_, cpu_excludes):
    if status_ == status_set.get(1):
        return input()
    else:
        choice = cpu_rand_choice()
        while choice in cpu_excludes and cpu_dominoes:
            choice = cpu_rand_choice()
        return choice


def cpu_rand_choice():
    return random.randint(-len(cpu_dominoes), len(cpu_dominoes))


def side_of_the_snake(choice, dominos):
    global status
    cpu_choices = set()
    count = 0
    while True:
        try:
            choice = int(choice)
            if abs(choice) <= len(dominos) != 0:
                if choice < 0:
                    domino_snake.insert(0, dominos.pop(verify_move(choice, dominos)))
                    break
                elif choice == 0:
                    if len(stock_pieces) > 0:
                        random.shuffle(stock_pieces)
                        dominos.append(stock_pieces.pop())
                        break
                    else:
                        raise ValueError
                else:
                    domino_snake.append(dominos.pop(verify_move(choice, dominos)))
                    break
            else:
                raise ValueError
        except ValueError:
            if status == status_set.get(1) and count == 0:
                print("Invalid input. Please try again.")
            if count > 0:
                status = status_set.get(5)
                break
            count += 1
            choice = validate_player(status, cpu_choices)
            continue
        except TypeError:
            if status == status_set.get(2):
                cpu_choices.add(choice)
            else:
                print("Illegal move. Please try again.")
            choice = validate_player(status, cpu_choices)
            continue


def player_move():
    side_of_the_snake(input(), player_dominoes)


def cpu_move():
    count = len(cpu_dominoes)
    side_of_the_snake(random.randint(-count, count), cpu_dominoes)


def check_states():
    global status
    if len(player_dominoes) == 0:
        status = status_set.get(3)
        return False
    elif len(cpu_dominoes) == 0:
        status = status_set.get(4)
        return False
    elif domino_snake[0][0] == domino_snake[-1][1]:
        number = domino_snake[0][0]
        numbers = tuple(y for x in domino_snake for y in x if y == number)
        if numbers.count(number) >= 8:
            status = status_set.get(5)
            return False
        else:
            return True
    else:
        return True


status_set = {1: "player", 2: "cpu", 3: "player_win", 4: "computer_win", 5: "draw"}
stock_pieces = generate_stock()
player_dominoes, cpu_dominoes = split_dominoes(stock_pieces), \
                                split_dominoes(stock_pieces)
status, domino_snake = pick_first_player(player_dominoes, cpu_dominoes)


def main():
    global status
    while check_states():
        interface()
        if status == status_set.get(1):
            player_move()
            status = status_set.get(2)
        elif status == status_set.get(2):
            input()
            cpu_move()
            status = status_set.get(1)
    interface()


if __name__ == "__main__":
    main()
