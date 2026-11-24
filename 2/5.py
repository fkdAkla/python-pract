
k = 0
c = 0
while True:
    try:
        n = int(input("Введите оценку:"))
        if n == -1: break
        if n < 0: raise ValueError
        k += n
        c += 1
    except ValueError:
        print("Неверная оценка")

res = k / (c or 1)

if res >= 90:
    print("A")
elif res >= 80:
    print("B")
elif res >= 70:
    print("C")
elif res >= 60:
    print("D")
else:
    print("F")
