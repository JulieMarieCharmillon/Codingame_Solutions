########################################## BINGO GAME ##########################################
from random import randint

## BINGO INITIALISATION
def bingo(n):
    """Create a random grid for the bingo game

    Args:
        n (int): the grid size (ie: if n=3 the grid is 3x3)

    Returns:
        list: the list of n*n elements representing the lines and colums of the bingo card
    """
    serie = []
    a,b = 1,5
    if n%2!=0: #impair
        for i in range(n**2):
            if i == round((n**2)/2):
                serie.append("0")
            else:
                serie.append(str(randint(a,b)))
                a += 5
                b += 5
    else:
        for i in range(n**2):
            l_i = [(list(range(n**2)))[a:a+n] for a in range(0, n**2, n)]
            
            li_diag = [[l_i[i][i] for i in range(1,n-1)], [l_i[x][y] for x,y in enumerate(range(n-1,-1,-1))][1:-1]]
            
            if i in li_diag[0] or i in li_diag[1]:
                serie.append("0")
            else:
                serie.append(str(randint(a,b)))
                a += 5
                b += 5
    return " ".join(serie)

# Creating a game not completely random: here we have at least the first line of the player's card matching the bingo card
def complete_win(n):
    """Create a random list of n**2-n element

    Args:
        n (int):the grid size (ie: if n=3 the grid is 3x3)

    Returns:
        list: return a list to be added to the n first element of the bingo card to ensure the match.
    """
    
    l = (bingo(n)).split(" ")
    for i in range(n):
        l.pop(0)
    return l

n=3
card = bingo(n)
card_list = card.split(" ")
win_results = card.split(" ")
win_list = (win_results[0:n])
win_list.extend(complete_win(n))

#win_list = bingo(n) ##Run this line instead of the previous 6 to get a full random game !

# Tests: you can run these to verify the two list
# print(card_list)
# print(win_list)

## BINGO results:
card_lines = [tuple(card_list[i:i+n]) for i in range(0, len(win_list), n)]
win_lines = [tuple(win_list[i:i+n]) for i in range(0, len(win_list), n)]

card_columns = [[(card_lines[y][i]) for y in range(n)] for i in range(n)]
win_columns = [[(win_lines[y][i]) for y in range(n)] for i in range(n)]

card_diag = [[(card_lines[i][i]) for i in range(n)], [(card_lines[x][y]) for x,y in enumerate(range(n-1,-1,-1))]]
win_diag = [[(win_lines[i][i]) for i in range(n)], [(win_lines[x][y]) for x,y in enumerate(range(n-1,-1,-1))]]


def compare_by_type(a,b,tp): 
    """Compare the lines/columns/diagonals of the cards

    Args:
        a (list): bingo list
        b (list): player list 
        tp (comments): lines/columns/diagonals

    Returns:
        tuples: lines/columns/diag, 0 if not matches
    """
    c_list = [tuple(l) for l in a] + [tuple(l) for l in b]
    bingo_number = len(c_list) - len(set(c_list))
    return (tp, bingo_number) 

def game():
    """Compares and counts the number of matches 
    """
    all = []
    all.append(compare_by_type(card_lines, win_lines, "lines"))
    all.append(compare_by_type(card_columns, win_columns, "columns"))
    all.append(compare_by_type(card_diag, win_diag, "diagonals"))
    br = 0
    sentence = f"BINGO! You've got"
    turn=0
    for tup in all:
        br += tup[1]
        if tup[1] !=0:
            turn += 1
            sentence = sentence + f" {'and ' if turn > 2 else ''}{tup[1]} {tup[0]}" #{',' if turn > 1 else ''}
    print(sentence) if br != 0 else "You loose"
    
game()
