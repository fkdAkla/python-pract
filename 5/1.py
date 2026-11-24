import json

res = {"students": [], "total_average_grade": 0}

try:
    
    with open("students.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
        
        s:dict
        total_avg = 0
        total_count = 0

        for s in data:
            if type(s) != dict:
                print("[1]Неверный тип данных")
                raise TypeError
            
            name = s.get("name")
            grades = s.get("grades")
            avg = 0

            if not name or not grades:
                print("Отсутствует ключ grades или name")
                raise KeyError
            if type(name) != str or type(grades) != list:
                print("[2]Неверный тип данных")
                raise TypeError

            
            if len(grades) == 0:
                print("У " + name + " нет оценок, пропускаем")
                continue

            for n in grades:
                if type(n) != int:
                    print("[3]Неверный тип данных")
                    raise TypeError
                avg += n
            
            avg /= len(grades)

            total_avg += avg
            total_count += 1
            list.append(res["students"], {"name": name, "average_grade": avg})


        if total_count == 0:
            print("Список учеников пуст")
        else:
            total_avg /= total_count
            res["total_average_grade"] = total_avg

except FileNotFoundError:
    print("Файл students.json не найден")
except json.JSONDecodeError:
    print("Ошибка чтения JSON")

if len(res["students"]) != 0:
    with open("report.json", "w+", encoding="utf-8") as f:
        f.write(json.dumps(res))