w, h = [int(i) for i in input("w,h").split()]
# n = int(input("n"))  # maximum number of turns before game over.

x0, y0 = [int(i) for i in input().split()]
bomb_dir = input()

chart_y = [y for y in range(h)]
chart = [(x, chart_y) for x in range(w)]

while len(chart) != 1:
    if "L" in bomb_dir: # x0 est donc plus GRAND que bomb_dir on peut donc retirer les listes avec un indice plus grand que xO:
        for i in range(w):
            if chart[-1][0]>=x0: #ici on compare le dernier élément de la ligne x (pas avec l'indice car celui-ci augmente et en enlevant l'élé
                chart.pop(-1)
    elif "R" in bomb_dir: 
        for i in range(w):
            if chart[0][0]<= x0:
                chart.pop(0)


    if "U" in bomb_dir: # yO est donc plus grand que bomb_dir on retire tout ce qui est plus grand:
        for i in range(len(chart_y)):
            if chart_y[i]>=y0:
                chart_y.pop(-1)
    elif "D" in bomb_dir:
        for i in range(len(chart_y)):
            if chart_y[i]<=y0:
                chart_y.pop(0)

    x0 = chart[(len(chart)//2)][0]
    y0 = chart_y[(len(chart_y)//2)]


    print(chart)
    print(f"xO={x0}, y0={y0}, len(chart)={len(chart)}, len(chart_y)={len(chart_y)}")
