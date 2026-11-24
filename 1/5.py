def safeGetNum(text):
    n = ""
    while True:
        n = input(text)
        try:
            n = int(n)
            break
        except ValueError:
            print("Это не число")
    return n

a = safeGetNum("Первый множитель:")
b = safeGetNum("Второй множитель:")
print("Произведение:", a*b)