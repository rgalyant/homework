with open("task-1.txt", "wt", encoding="utf-8") as file:
    while True:
        inp = input()
        if len(inp) == 0: break
        file.write(inp + "\n")