with open('8.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]

def get_harmonics(loc1, loc2, s):
    antinodes = set()

    i=0
    while True:
        next = (loc1[0] - s[0]*i,loc1[1] - s[1]*i)
        if not(0<=next[0]<len(grid) and 0<=next[1]<len(grid[0])):
            break
        antinodes.add(next)
        i += 1
    i=0
    while True:
        next = (loc2[0] + s[0]*i,loc2[1] + s[1]*i)
        if not(0<=next[0]<len(grid) and 0<=next[1]<len(grid[0])):
            break
        antinodes.add(next)
        i += 1

    return antinodes
     
def get_antinodes(locations):
    antinodes = set()
    for  index, location1 in enumerate(locations):
        for i in range(index, len(locations)-1):
            location2 = locations[i+1]
            slope = [location2[0]-location1[0],location2[1]-location1[1]]
            antinodes.update(get_harmonics(location1, location2,slope))
    return antinodes

def count_nodes(rows, columns, antennas):
    antinodes = set()
    for index, key in enumerate(antennas):
        antinodes.update(get_antinodes(antennas[key]))
    antinodes = {node for node in antinodes if 0 <= node[0] < rows and 0 <= node[1] < columns}
    return len(antinodes)    
    
antennas_dict = {}
for row_index, row in enumerate(grid):
    for col_index, col in enumerate(row):
        value = grid[row_index][col_index]
        if value != '.':
             antennas_dict.setdefault(value,[]).append([row_index,col_index])
print(count_nodes(row_index+1,col_index+1,antennas_dict))