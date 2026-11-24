import string

alf = string.ascii_lowercase

pmin = alf.find("m")
pmax = alf.find("z")

def count(text):
    res = 0
    for s in text:
        if alf.find(s) == -1:
            print("Присутствуют неразрешенные символы")
            return
        i = alf.find(s)
        if i >= pmin and i <= pmax:
            res += 1
    return res

print(count("mnoooaaazz"))