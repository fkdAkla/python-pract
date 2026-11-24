def safeGetNum(s):
    while True:
        try:
            num = int(input(s))
            if num <= 0 or num > 12:
                raise ValueError
            return num
        except ValueError:
            print("Неверное число")

n = safeGetNum("Номер месяца:")

seasons = ("Зима", "Весна", "Лето", "Осень")

kv = (n - 1) // 3 + 1

season = seasons[(n % 12) // 3]

print("Квартал:", kv)
print("Сезон:", season)