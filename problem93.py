import itertools
bracket = [
    " {} {} {} ",
    "( {} ){} {} ",
    "( {} {} ){} ",
    " {}( {} ){} ",
    " {}( {} {} )",
    "( {} ){}( {} )",
    "( {}( {} )){} ",
    "(( {} ){} ){} ",
    " {}(( {} ){} )",
    " {}( {}( {} ))",
]
all_combination = []
for i in itertools.permutations("+-*/", 3):
    for config in bracket:
        all_combination.append(config.format(*i).replace(" ", "{}"))
# print(all_combination[:10],len(all_combination))
max_found = 0

for d in range(4, 100):
    for c in range(3, d):
        for b in range(2, c):
            for a in range(1, b):
                ref = [0]*len(all_combination)
                for com in all_combination:
                    for config in itertools.permutations([str(x) for x in [a, b, c, d]]):
                        com.format(*config)
                        try:
                            res = eval(com)
                            if int(res) == res and res > 0:
                                ref[int(res)] = 1
                        except Exception:
                            pass
                if ref[1] != 1:
                    continue
                exit()
                temp = ref[1:].index(0)
                if max_found < temp:
                    max_found = temp
                    print(a, b, c, d, max_found)
