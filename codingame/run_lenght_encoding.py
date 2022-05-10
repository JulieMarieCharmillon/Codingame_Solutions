digits = input()

d = {"1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", 
"7":"Seven", "8":"Eight", "9":"Nine", "0":"Zero"}

s=[]
for index,chiffre in enumerate(digits):
    
    if chiffre == digits[index-1]:
        pass
    else: 
        count = 1
        for c in digits[index+1:]:
            if chiffre == c:
                count += 1
            else:
                break
        if count >1:
            s.append(f"{d.get(str(count))} {d.get(chiffre)}s")
        else:
            s.append(d.get(chiffre))
        

print(" ".join(s))


###################### 'Correction' from condingame ##########################
# from itertools import groupby

# s=groupby(input())

# r = []

# D=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
# P=['Zeros','Ones','Twos','Threes','Fours','Fives','Sixes','Sevens','Eights','Nines']

# for d,c in s:
#     d=int(d)
#     n = len(list(c))
#     if n == 1:
#         r.append(D[d])
#     else:
#         r.append(D[n])
#         r.append(P[d])

# print(*r)


