n = int(input())

family_liste = []

for i in range(n):
    inputs = input().split()
    name = inputs[0]
    parent = inputs[1]
    birth = int(inputs[2])
    death = inputs[3]
    religion = inputs[4]
    gender = inputs[5]
    
    family_liste.append(inputs)

family_liste.sort(key= lambda el: el[2])
di_family = {}

for enfant in family_liste:
    for parent in family_liste:
        if enfant[1] == parent[0]:
            if parent[0] in di_family.keys():
                di_family.get(parent[0]).append(enfant)
            else:
                di_family[parent[0]]=[enfant]
        else:
            di_family[enfant[0]]=[]
        

def dfs(d:list, graph:dict, start):
    
    couleur = {s: 'vert' for s in graph} # couleur des sommets
    couleur[start[0]] = 'orange' # on passe la racine à orange
    Q= [start[0]] #premier element de la pile
    succession = [start]
    while Q: 
        u = Q[-1] # on prend le dernier élément ...
        # On cherche les enfants non parcourus:
        R = [y for y in graph[u] if couleur[y[0]] == 'vert'] 
        R.sort(key= lambda el: el[2]) # ordonne les siblings par date de naissance
        R.sort(key=lambda el: el[5], reverse=True) # ordonne les siblings par genre
        if R:
            v=R[0][0] # on prend le premier sommet   #pour succession on choisi le plus vieux
            couleur[v] = "orange" #on passe le sommet à orange
            Q.append(v) # on empile le sommet découvert
            succession.append(R[0])
        else:
            Q.pop() # on dépile par la tête 
            couleur[u]='rouge' #le sommet est fermé
    return succession


# OUTPUT :
succession = dfs(family_liste,di_family,family_liste[0])
FINAL = []
for human in succession:
    if human[3] == "-" and human[4] == "Anglican":
        FINAL.append(human[0])
print("\n".join(FINAL))

