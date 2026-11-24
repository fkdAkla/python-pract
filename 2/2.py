operation = ""
validOps = ("+", "-", "*", "/")

while True:
    operation = input("operation:")
    if not operation in validOps:
        print("Невалидная операция")
        continue
    break

def safeGetNum(s, excl = False):
    while True:
        try:
            num = int(input(s))
            if (excl and num == 0 and operation == "/"):
                print("На 0 делить нельзя")
            else:
                return num
        except ValueError:
            print("Неверное число")

def action(s, a, b):
    match s:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a/b
        
value_1 = safeGetNum("value_1:")
value_2 = safeGetNum("value_2:", True)

print(action(operation, value_1, value_2))