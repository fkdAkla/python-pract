n = ""

while True:
    n = input("Введите число:")
    try:
        n = int(n)
        break
    except ValueError:
        print("Это не число")

if n > 0:
    n*=-1

print(n)
