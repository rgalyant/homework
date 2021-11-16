y = int(input("Введите год:" ))
if y % 4 != 0:
    print("Обычный")
    if y % 400 == 0:
        print("Високосный")
        print("Обычный")
else:
    print("Високосный")