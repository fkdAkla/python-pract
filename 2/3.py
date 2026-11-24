def safeGetNum(s):
    while True:
        try:
            num = int(input(s))
            return num
        except ValueError:
            print("Неверное число")

n1 = safeGetNum("Первое число:")
n2 = safeGetNum("Второе число:")

if n1 > n2:
    start = n2
    end = n1
else:
    start = n1
    end = n2

res = 0
for i in range(start, end+1):
    res += i

print(res)