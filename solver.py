def my_move(grid, pos_head, pos_apple, available_moves, last_move)->str:
    print(pos_head, pos_apple)
    if len(available_moves) == 1:
        return available_moves[0]
    
    grid = clean3(grid)

    print("grid:")
    for l in grid:
        print(l)

    new_g = grid
    new_g = find_islands(new_g)

    print("grid with islands:")
    for l in new_g:
        print(l)
    
    if pos_apple[0] > pos_head[0] and "DOWN" in available_moves:
        if last_move == "UP" and pos_head[1] != 0:
            if new_g[pos_head[0]][pos_head[1]+1] != 3:
                return "RIGHT"
        if last_move == "UP" and pos_head[1] != len(grid[pos_head[0]])-1:
            if new_g[pos_head[0]][pos_head[1]-1] != 3:
                return "LEFT"
        else :
            if new_g[pos_head[0]+1][pos_head[1]] != 3:
                return "DOWN"
    if pos_apple[0] < pos_head[0] and "UP" in available_moves:
        if last_move == "DOWN" and pos_head[1] != 0:
            if new_g[pos_head[0]][pos_head[1]+1] != 3:
                return "RIGHT"
        if last_move == "DOWN" and pos_head[1] != len(grid[pos_head[0]])-1:
            if new_g[pos_head[0]][pos_head[1]-1] != 3:
                return "LEFT"
        else :
            if new_g[pos_head[0]-1][pos_head[1]] != 3:
                return "UP"
    if pos_apple[1] < pos_head[1] and "LEFT" in available_moves:
        if last_move == "RIGHT" and pos_head[0] != 0:
            if new_g[pos_head[0]-1][pos_head[1]] != 3:
                return "UP"
        if last_move == "RIGHT" and pos_head[0] != len(grid):
            if new_g[pos_head[0]+1][pos_head[1]] != 3:
                return "DOWN"
        else :
            if new_g[pos_head[0]][pos_head[1]-1] != 3:
                return "LEFT"
    if pos_apple[1] > pos_head[1] and "RIGHT" in available_moves:
        if last_move == "LEFT" and pos_head[0] != 0:
            if new_g[pos_head[0]-1][pos_head[1]] != 3:
                return "UP"
        if last_move == "LEFT" and pos_head[0] != len(grid):
            if new_g[pos_head[0]+1][pos_head[1]] != 3:
                return "DOWN"
        else :
            if new_g[pos_head[0]][pos_head[1]+1] != 3:
                return "RIGHT"
    
    print("NO ENCOURAGING 0 AROUND")

    if "DOWN" in available_moves:
        if last_move == "UP" and pos_head[1] != 0:
            if new_g[pos_head[0]][pos_head[1]+1] != 3:
                return "RIGHT"
        if last_move == "UP" and pos_head[1] != len(grid[pos_head[0]])-1:
            if new_g[pos_head[0]][pos_head[1]-1] != 3:
                return "LEFT"
        else :
            if new_g[pos_head[0]+1][pos_head[1]] != 3:
                return "DOWN"
    if "UP" in available_moves:
        if last_move == "DOWN" and pos_head[1] != 0:
            if new_g[pos_head[0]][pos_head[1]+1] != 3:
                return "RIGHT"
        if last_move == "DOWN" and pos_head[1] != len(grid[pos_head[0]])-1:
            if new_g[pos_head[0]][pos_head[1]-1] != 3:
                return "LEFT"
        else :
            if new_g[pos_head[0]-1][pos_head[1]] != 3:
                return "UP"
    if "LEFT" in available_moves:
        if last_move == "RIGHT" and pos_head[0] != 0:
            if new_g[pos_head[0]-1][pos_head[1]] != 3:
                return "UP"
        if last_move == "RIGHT" and pos_head[0] != len(grid):
            if new_g[pos_head[0]+1][pos_head[1]] != 3:
                return "DOWN"
        else :
            if new_g[pos_head[0]][pos_head[1]-1] != 3:
                return "LEFT"
    if "RIGHT" in available_moves:
        if last_move == "LEFT" and pos_head[0] != 0:
            if new_g[pos_head[0]-1][pos_head[1]] != 3:
                return "UP"
        if last_move == "LEFT" and pos_head[0] != len(grid):
            if new_g[pos_head[0]+1][pos_head[1]] != 3:
                return "DOWN"
        else :
            if new_g[pos_head[0]][pos_head[1]+1] != 3:
                return "RIGHT"


    print("REALLY NO 0")
    return available_moves[0]

def check_islands_on_move(available_moves, grid, pos_head):
    moves = []
    for move in available_moves:
        if move == "RIGHT":
            moves.append(("RIGHT", grid[pos_head[0]][pos_head[1]+1]))
        if move == "LEFT":
            moves.append(("LEFT", grid[pos_head[0]][pos_head[1]-1]))
        if move == "DOWN":
            moves.append(("DOWN", grid[pos_head[0]+1][pos_head[1]]))
        if move == "UP":
            moves.append(("UP", grid[pos_head[0]-1][pos_head[1]]))
    return moves


def find_islands(new_g):
    for y in range(0, len(new_g)-1):
        if 1 not in new_g[y]:
            continue
        for x in range(0, len(new_g[y])-1):
            if (new_g[y][x] in [1,2]  
                and new_g[y +1][x] in [1,2] 
                and new_g[y][x+1] in [1, 2]
                and new_g[y+1][x+1] == 0):
                new_g = island_marking(new_g, y+1, x+1)

    return new_g


def island_marking(new_g, y, x):
    island_elem = [(y, x)]
    try :
        for i in range(y, len(new_g)):
            # We are on the island
            foundIsland = False
            for j in range(x, len(new_g[i])):
                # if we reach the end of the line without encountering snake, no island there
                if (new_g[i][j] == 0
                    and j == len(new_g[j])-1):
                    return new_g
                
                # Each 0 is marked as an island spot is equals to 0 and on island
                if (new_g[i][j] == 0):
                    foundIsland = True
                    island_elem.append((i, j))

                # if elem is 1 or 2, search if it's a corner (2 can't be a corner of interest in our case, bur algorithm will be easier to be reused)
                elif (new_g[i][j] in [1,2] 
                    and new_g[i-1][j] in [1,2]
                    and new_g[i][j-1] in [1,2]):
                    raise  # Raise is used to break out both for loops

                # If we find a snake, mark the following elem as non-island. Will reset when going to the next line
                elif (new_g[i][j] in [1, 2] and not foundIsland):
                    raise
                
                elif (new_g[i][j] in [1, 2]):
                    break

                # Happends when we hit something else than a snake after saying we are not in the island, and no corner have been found.
                # Go to next line.
                else :
                    break

    except :
        for elem in island_elem:
            new_g[elem[0]][elem[1]] = 3
        return new_g
    
    return new_g

def clean3(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 3:
                grid[i][j] = 0
    return grid