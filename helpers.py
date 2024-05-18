import keyboard
import random

# def get_head(grid:list)->tuple:
#     for l in range(0, len(grid)):
#         for r in range (0, len(grid[l])):
#             if grid[l][r] == 2:
#                 return (l, r)
#     raise ValueError("No head found")

def get_moves(grid:list, pos_head:tuple)->list:
    moves = []
    
    if (pos_head[0] and grid[pos_head[0]-1][pos_head[1]] != 1):
        moves.append('UP')
    if (pos_head[0] < len(grid)-1 and grid[pos_head[0]+1][pos_head[1]] != 1):
        moves.append('DOWN')
    if (pos_head[1] < len(grid[pos_head[0]])-1 and grid[pos_head[0]][pos_head[1]+1] != 1):
        moves.append('RIGHT')
    if (pos_head[1] and grid[pos_head[0]][pos_head[1]-1] != 1):
        moves.append('LEFT')
    
    return moves


def key_pressed()->str:
    if keyboard.is_pressed('left'):
        return "LEFT"
    elif keyboard.is_pressed('right'):
        return "RIGHT"
    elif keyboard.is_pressed('down'):
        return "DOWN"
    elif keyboard.is_pressed('up'):
        return "UP"
    return None

def get_last_move(body_elements:list)->str:
    head, neck = body_elements[-1], body_elements[-2]
    if head[0] - neck[0] == 1 :
        return 1,0
    if head[0] - neck[0] == -1 :
        return -1,0
    if head[1] - neck[1] == 1 :
        return 0,1
    if head[1] - neck[1] == -1 :
        return 0,-1

def get_new_head(move_asked:str, available_moves:list, pos_head:tuple, body_elements:list)->tuple:
    if move_asked not in available_moves:
        last_move = get_last_move(body_elements)
        new_head = pos_head[0] + last_move[0], pos_head[1] + last_move[1]
    elif move_asked == "RIGHT":
        new_head = pos_head[0], pos_head[1]+1
    elif move_asked == "LEFT":
        new_head = pos_head[0], pos_head[1]-1
    elif move_asked == "DOWN":
        new_head = pos_head[0]+1, pos_head[1]
    elif move_asked == "UP":
        new_head = pos_head[0]-1, pos_head[1]
        
    return new_head

def is_in_grid(new_head:tuple, grid:list)->bool:
    if new_head[0] > -1 and new_head[0] < len(grid):
        if new_head[1] > -1 and new_head[1] < len(grid[new_head[0]]):
            return True
    return False

def add_apple(grid:list)->list:
    empty_counter = 0
    for row in grid:
        empty_counter += row.count(0)
    if empty_counter < 1:
        return None, None
    new_apple = random.randint(1, empty_counter)
    
    for row in range(0, len(grid)):
        for elem in range(0, len(grid[row])):
            if not grid[row][elem] == 0:
                continue
            new_apple -=1
            if new_apple == 0:
                pos_apple = (row,elem)
                grid[row][elem] = 'X'
                break
    return grid, pos_apple

def update_score(score, score_label):
    score_label.config(text="Score: {}".format(score))
    score_label.update()

def draw_grid(canvas, grid):
    canvas.delete("all")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x1 = j * 30
            y1 = i * 30
            x2 = x1 + 30
            y2 = y1 + 30
            canvas.create_rectangle(x1, y1, x2, y2)
            if grid[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            elif grid[i][j] == 2:
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            elif grid[i][j] == 'X':
                canvas.create_rectangle(x1, y1, x2, y2, fill="red")
    canvas.update()
