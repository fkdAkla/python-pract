def safeGetNum(s):
    while True:
        try:
            num = int(input(s))
            if num <= 0 or num > 12:
                raise ValueError
            return num
        except ValueError:
            print("Неверное число")

seasons = ("Зима", "Весна", "Лето", "Осень")

def get_kvartal(month_num):
    return (month_num - 1) // 3 + 1

def get_season(month_num):
    return seasons[(month_num % 12) // 3]

def main():
    n = safeGetNum("Номер месяца:")

    kv = get_kvartal(n)

    season = get_season(n)

    print("Квартал:", kv)
    print("Сезон:", season)

main()