
def safeGetNum(text):
    n = ""
    while True:
        n = input(text)
        try:
            n = int(n)
            if n >= 0:
                break
            else:
                print("Число не может быть отрицательным")
        except ValueError:
            print("Это не число")
        
    return n

cap = safeGetNum("Вместимость автобуса:")
on = safeGetNum("Заполненность автобуса:")
wait = safeGetNum("Число ожидающих посадку:")

print("Число оставшихся пассажиров:", max(0, wait-(cap-on)))
