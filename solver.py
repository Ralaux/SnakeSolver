def my_move(grid, pos_head, pos_apple, available_moves, last_move)->str:
    print(pos_head, pos_apple)
    if pos_apple[0] > pos_head[0] and "DOWN" in available_moves:
        if last_move == "UP" and pos_head[1] != 0:
            rtn = "RIGHT"
        elif last_move == "UP" :
            rtn = "LEFT"
        else :
            rtn = "DOWN"
    elif pos_apple[0] < pos_head[0] and "UP" in available_moves:
        if last_move == "DOWN" and pos_head[1] != 0:
            rtn = "RIGHT"
        elif last_move == "DOWN" :
            rtn = "LEFT"
        else :
            rtn = "UP"
    elif pos_apple[1] < pos_head[1] and "LEFT" in available_moves:
        if last_move == "RIGHT" and pos_head[0] != 0:
            rtn = "UP"
        elif last_move == "RIGHT" :
            rtn = "DOWN"
        else :
            rtn = "LEFT"
    elif pos_apple[1] > pos_head[1] and "RIGHT" in available_moves:
        if last_move == "LEFT" and pos_head[0] != 0:
            rtn = "UP"
        elif last_move == "LEFT" :
            rtn = "DOWN"
        else :
            rtn = "RIGHT"
    else :
        rtn = available_moves[0]
    print(rtn)
    return rtn

def move_180():
    return "UP"