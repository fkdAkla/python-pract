def stb(s:str):
    return s.lower() in ("true", "1")

employed = stb(input("employed:"))
vacation = stb(input("vacation:"))

print(employed and not vacation)