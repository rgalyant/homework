y = int(input("Введите год: " ))
if 1900 < y < 1000000:
    if y % 4 != 0:
        print("Обычный")
        if y % 400 == 0:
            print("Високосный")
    else:
        print("Високосный")
else:
    print("Введеный год не отвечает условиям")



