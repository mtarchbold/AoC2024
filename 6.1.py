with open('6.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]
  
directions = [[0,-1],[1,0],[0,1],[-1,0]]
direction = [0,-1]

def turn_right():
   global direction
   direction = directions[(directions.index(direction)+1)%4]

def traverse(r,c):
    count = 1
    grid[r][c] = "X"
    while 0 <= r + direction[1] < len(grid) and 0 <= c + direction[0] < len(grid[0]):
        if grid[r + direction[1]][c + direction[0]] == "#":
            turn_right()
            continue
        r += direction[1]
        c += direction[0]
        if grid[r][c] != "X":
            grid[r][c] = "X"
            count += 1
    return count
  
for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == "^":
            r = row
            c = column
print(traverse(r,c))
