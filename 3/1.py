l = ["qqwe", "asdf", "ghjk", "opaiu"]

tofind = input("Строка для поиска её индекса в списке:")

if tofind in l:
    print(l.index(tofind))
else:
    print("Строка отсутствует в списке")