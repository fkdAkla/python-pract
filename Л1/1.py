
def main():
    count = int(input("Число людей:"))

    if count <= 0:
        print("Число людей должно быть положит.")
        return

    res = 0
    for i in range(count):
        res += int(input("Возраст человека №"+str(i+1)+": "))

    print(res/count)
main()