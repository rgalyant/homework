def update_hero(hero=None, power=None, alive=None, speed=None, X=None, Y=None):
    data = {}

    with open("hero.ini", "rt", encoding="utf-8") as ini:
        while True:
            line = ini.readline()[:-1]
            if not line: break
            if len(line) == 0 or line[0] == ";" or "=" not in line: continue
            [key, value] = line.split("=", 1)
            data[key] = value
        
    if hero:  data["hero"] = hero
    if power: data["power"] = power
    if alive: data["alive"] = alive
    if speed: data["speed"] = speed
    if X:     data["X"] = X
    if Y:     data["Y"] = Y

    with open("hero.ini", "wt", encoding="utf-8") as ini:
        for key in data:
            ini.write(f"{key}={data[key]!s}\n")

if __name__ == "__main__":
    update_hero(hero="Hulk", power=450, Y=2.3)