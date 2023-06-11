print('# HARSH FIRST SEARCH pathfinding algorithm #')

while True :

    x_target = int(input('targets x axis >'))
    y_target = int(input('targets y axis >'))

    hunter_x, hunter_y = 0, 0

    print()

    print(f'straight :')

    print(f'left {x_target}')
    print(f'down {y_target}')

    print()

    if x_target >= 5 and x_target >= y_target :

        print(f'diagonally :')

        print(f'diagonally down left {y_target}')
        print(f'left {x_target - y_target}')

        print()

    elif x_target >= 5 and x_target <= y_target :

        print(f'diagonally :')

        print(f'diagonally down left {x_target}')
        print(f'down {y_target - x_target}')

        print()



    elif x_target <= 4 and x_target >= y_target :

        print(f'diagonally :')

        print(f'diagonally down left {y_target}')
        print(f'left {x_target - y_target}')

        print()

    elif x_target <= 4 and x_target <= y_target :

        print('diagonally :')

        print(f'diagonally down left {x_target}')
        print(f'down {y_target - x_target}')

        print()
