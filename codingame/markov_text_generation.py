t = """stop there once was a girl named dorothy stop dorothy had a dog named toto stop dorothy lived with her aunt and uncle with her dog named toto stop she was a girl of who dreamed of traveling stop"""
d = 2 # depth
l = 10 # output 'lenght' ie: nombre de MOT (pas de caractère)
s = "dorothy was a" # the output starts with and count for the lenght

words = t.split(" ")
d_gram = [" ".join(words[i:i+d]) for i in range(len(words)-d)]

s_list = s.split(" ")

d_n_gram = {}

for i in range(len(words)-d):
    if not (d_gram[i] in d_n_gram.keys()):
        d_n_gram[d_gram[i]] = [words[i+d]]
    else:
        d_n_gram[d_gram[i]].append(words[i+d])

random_seed=0
def pick_option_index(num_of_options):
    global random_seed 
    random_seed += 7
    return random_seed % num_of_options

output = s_list
for i in range(l-len(s_list)):
    to_add = d_n_gram.get(" ".join(output[-d:]))
    opt = pick_option_index(len(to_add))
    output.append(to_add[opt])
print(" ".join(output))


print(d_n_gram)
# options = d_gram.count(" ".join(s_list[-d:]))

# def get_start_index():
#     option_index_list = []
#     for i in range(len(d_gram)):
#         if d_gram[i] == " ".join(s_list[-d:]):
#             option_index_list.append(i)
#     option_index = pick_option_index(options)
#     start = option_index_list[option_index]
#     return start

# start = get_start_index()+d
# print(c " ".join(words[start:start+l]))

