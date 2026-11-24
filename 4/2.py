def count_symbols(text, to_count):
    res = {k: 0 for k in to_count}

    for s in text:
        if s in res:
            res[s] += 1
    return res

s = "sksskkkqqqqqooooooo"

to_count = {"q": 0, "o": 0, "p": 0}

res = count_symbols(s, to_count)

if len(res) > 0:
    print("Число определенных символов в предложении:")
    for k, v in res.items():
        print(k+": "+str(v))
else:
    print("Символы для поиска не выбраны")
