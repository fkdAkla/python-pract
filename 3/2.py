l = ["qqwe", "asdf", "ghjk", "ghjk", "opaiu", "opaiu", 1, 5, 3, 5, 7, 3, 3]

t = l.copy()

r = []

for x in t:
    if x not in r:
        r.append(x)
        continue
    l.remove(x)
print(l)