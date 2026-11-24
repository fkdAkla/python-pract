def analyze_color(hex_code: str) -> str:

    if len(hex_code) != 6:
        raise ValueError("Цветовой код должен состоять из 6 символов")

    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)

    if r == g == b:
        if r == 0:
            return "черный"
        elif r == 255:
            return "белый"
        else:
            return "серый"

    channels = {
        "красный": r,
        "зеленый": g,
        "синий": b
    }
    dominant_color = max(channels, key=channels.get)
    return f"ближе к {dominant_color[:-2]}ому"

print("a0351f ->", analyze_color("a0351f"))
print("10e540 ->", analyze_color("10e540"))
print("2244ff ->", analyze_color("2244ff"))
print("808080 ->", analyze_color("808080"))
print("000000 ->", analyze_color("000000"))
print("ffffff ->", analyze_color("ffffff"))