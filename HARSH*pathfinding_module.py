straight_path_left = []
straight_path_down = []

diagonal_path_down_left = []
diagonal_path_left = []
diagonal_path_down = []

def pathfind (x_target, y_target) :
    hunter_x, hunter_y = 0, 0

    straight_left = x_target
    straight_down = y_target

    straight_path_left.append(straight_left)
    straight_path_down.append(straight_down)

    if x_target >= 5 and x_target >= y_target :
        diagonal_down_left = y_target
        diaoognal_left = x_target - y_target

        diagonal_path_down_left.append(diagonal_down_left)
        diagonal_path_left.append(diaoognal_left)

    elif x_target >= 5 and x_target <= y_target :
        diagonal_down_left_2 = x_target
        diaognal_down = y_target - x_target

        diagonal_path_down_left.append(diagonal_down_left_2)
        diagonal_path_down.append(diaognal_down)

    elif x_target <= 4 and x_target >= y_target :
        diagonal_down_left_3 = y_target
        diaognal_left_2 = x_target - y_target

        diagonal_path_down_left.append(diagonal_down_left_3)
        diagonal_path_left.append(diaognal_left_2)

    elif x_target <= 4 and x_target <= y_target :
        diagonal_down_left_4 = x_target
        diaognal_down_2 = y_target - x_target

        diagonal_path_down_left.append(diagonal_down_left_4)
        diagonal_path_down.append(diaognal_down_2)
