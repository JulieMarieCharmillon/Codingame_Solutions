
w = int(input())
h = int(input())
LINES = []

for i in range(h):
    line = input()
    l = [ch for ch in line]
    LINES.append(l)
    

for y in range(h):
    for x in range(w):
        character = LINES[y][x]
        if character == '.':
            neighbours = []
            if y-1 >=0 and x-1 >=0: ## Cette succession de if n'est pas élégante du tout !!! -> TROUVER UN AUTRE ALGORITHME PLUS EFFICACE ET PLUS ELEGANT !!!!
                neighbours.append(LINES[y-1][x-1])
            if y+1 <=h-1 and x+1 <=w-1:
                neighbours.append(LINES[y+1][x+1])
            if y-1 >=0 and x+1 <=w-1:
                neighbours.append(LINES[y-1][x+1])
            if y+1 <=h-1 and x-1 >=0:
                neighbours.append(LINES[y+1][x-1])
            
            if x+1 <=w-1:
                neighbours.append(LINES[y][x+1])
            if x-1 >=0:
                neighbours.append(LINES[y][x-1])
            if y+1 <=h-1:
                neighbours.append(LINES[y+1][x])
            if y-1 >=0:
                neighbours.append(LINES[y-1][x])
            if neighbours.count("x") != 0:
                LINES[y][x] = str(neighbours.count("x"))
        
for y in range(h):
    for x in range(w):
        character = LINES[y][x]
        if character == 'x':
            LINES[y][x] = "."


for line in LINES:
    print("".join(line))


#### AUTRES (morceaux de) SOLUTIONS :
# for row in range(h):
#     count_row = []
#     for col in range(w):
#         if grid[row][col] == 'x':
#             count_row.append('.')
#             continue

#         mines = 0
#         for x, y in [(-1,0), (1,0), (0,-1), (0,1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
#             if (0 <= (row + x) < h) and (0 <= (col + y) < w):
#                 if grid[row + x][col + y] == 'x':
#                     mines += 1
#         count_row.append(str(mines) if mines > 0 else '.')
#     print("".join(count_row))