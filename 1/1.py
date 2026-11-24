s = input()

print(type(s))

try:
    s = int(s)
except ValueError:
    s = s
print(type(s))
s = str(s)
print(type(s))
