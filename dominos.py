import random

game = True
status = None
full_set = []

def shuffle(set):
    
    for x in range(7):
        for y in range(7):
            if [y, x] not in set:
                set.append([x,y])
                y += 1

    stock = (random.sample(set, 14))
    set = pop(stock, set)

    computer = random.sample(set, 7)
    set = pop(computer, set)

    player = random.sample(set, 7)
    set = pop(player, set)

    return stock, computer, player


def pop(set_1, set_2):
    for n in set_1:
        if n in set_2:
            set_2.remove(n)

    return(set_2)

def get_snake(set):
    snake = []

    for n in set:
        if n[0] == n[1]:
            if len(snake) == 0:
                snake.append(n)
            elif n > snake[0]:
                snake[0] = n
    return snake

def check_move(move):

    valid = True
    if len(move) == 1 and move != 0 or len(move) > 2:
        valid = False

    direction = move[0]
    piece = move[1]
    try:
        piece = int(piece)
    except:
        print('Invalid input. Please try again.')
        continue

    if piece < 0 or piece > len(player):
        print('Invalid input. Please try again.')
        continue

    if direction not in ['+', '-']:
        print('Invalid input. Please try again.')
        continue

while game is True:

    while status is None:
        stock, computer, player = shuffle(full_set)

        c_snake = get_snake(computer)
        p_snake = get_snake(player)

        if c_snake > p_snake:
            snake = c_snake
            computer.remove(snake[0])
            status = 'player'
        elif p_snake > c_snake:
            snake = p_snake
            player.remove(snake[0])
            status = 'computer'

    print(70 * '=')
    print(f'Stock size: {len(stock)}')
    print(f'Computer pieces: {len(computer)}\n')
    print(snake)
    print()
    print('Your pieces:')

    i = 1
    for n in player:
        print(f'{i}:{n}')
        i += 1

   
    if status == "player":
        move = None
        while status is "player":
            move = input("\nStatus: It's your turn to make a move. Enter your command.")

            if check_move(move) is False:
                print('Invalid input. Please try again.')
                continue

            else:
                if direction == '+':
                    piece = player.pop(piece - 1)
                    snake.append(piece)
                    print(snake)
                else:
                    piece = player.pop(piece - 1)
                    snake.insert(0, piece)
                    print(snake)

                i = 1
                for n in player:
                    print(f'{i}:{n}')
                    i += 1

                status = 'computer'
                game = 'off'
                
  

    else:
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        game = 'off'

