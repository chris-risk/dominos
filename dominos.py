import random

def pop(set_1, set_2):
    for n in set_1:
        if n in set_2:
            set_2.remove(n)

    return(set_2)

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

def get_snake(set):
    snake = []

    for n in set:
        if n[0] == n[1]:
            if len(snake) == 0:
                snake.append(n)
            elif n > snake[0]:
                snake[0] = n
    return snake

status = None
full_set = []

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
print(snake[0])
print()
print('Your pieces:')

i = 1
for n in player:
    print(f'{i}:{n}')
    i += 1

if status == "player":
    print("\nStatus: It's your turn to make a move. Enter your command.")
else:
    print("\nStatus: Computer is about to make a move. Press Enter to continue...")