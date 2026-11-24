l = [5, 3, 7, 8, 10, 2.5, 1.7, 23, 102, 43, 201]

z = [x for x in l if not "." in str(x)]

l.remove(min(z))

print(l)