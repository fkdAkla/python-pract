l = ["qqwe", "asdf", "ghjk", "ghjk", "opaiu", "opaiu", 1, 5, 3, 5, 7, 3, 3, 3]

reps = {}

for x in l:
    reps[x] = reps.get(x) or 0
    reps[x] += 1
print(reps)