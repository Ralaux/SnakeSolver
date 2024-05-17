from helpers import get_moves, key_pressed, get_new_head, is_in_grid, add_apple, update_score, draw_grid
import time
import tkinter as tk 



starting_body = [(7,3), (7,4)]
pos_head = (7,5)
starting_apple = (2,8)
height = 10
width = 10
body_elements = starting_body + [pos_head]
score = 0
eat = False
win = False

grid = []
for i in range(0,height):
    grid.append([])
    for j in range(0,width):
        grid[i].append(0)
        

for pos in starting_body:
    grid[pos[0]][pos[1]] = 1
grid[pos_head[0]][pos_head[1]] = 2
grid[starting_apple[0]][starting_apple[1]] = 'X'

root = tk.Tk()
root.title("Snake Game")
canvas = tk.Canvas(root, width=width*30, height=height*30, borderwidth=0, highlightthickness=0)
canvas.pack()
score_label = tk.Label(root, text="Score: 0")
score_label.pack()


while True:
        
    draw_grid(canvas, grid)
    update_score(score, score_label)
    
    #Get the move asked
    available_moves = get_moves(grid, pos_head)
    time.sleep(0.4)
    move_asked = key_pressed()
    new_head = get_new_head(move_asked, available_moves, pos_head, body_elements)
    
    #Check if the move is legal
    if not is_in_grid(new_head, grid):
        break
    if grid[new_head[0]][new_head[1]] == 1 and new_head != body_elements[0]:
        break
    
    #Check if apple
    if grid[new_head[0]][new_head[1]] == 'X':
        eat = True
    
    #Make the move
    grid[new_head[0]][new_head[1]] = 2
    grid[pos_head[0]][pos_head[1]] = 1
    body_elements.append(new_head)
    pos_head = new_head
    if eat :
        grid = add_apple(grid) #returns none if no empty space -> Win
        eat = False
        score +=1
    else :
        to_remove = body_elements.pop(0)
        if not to_remove == new_head:
            grid[to_remove[0]][to_remove[1]] = 0 
        
    if grid == None:
            win = True
            break
    continue
    

if not win :
    print("LOSER, score =", score)
else :
    score +=100
    print("WINNER, score =", score)


input("Press Enter to continue...")


