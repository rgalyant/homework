from random import randint

random_number = randint(1, 100)
user_number = 0
user_guesses = 0

while user_number != random_number:
    user_input = input("Введите число от 1 до 100: ")
    user_guesses += 1

    if not user_input.isnumeric():
        print("Неправельный ввод")
    else:
        user_number = int(user_input)
        if user_number < 1 or user_number > 100:
            print("Число вне диапазона")

        if user_number < random_number:
            print("Ваше число меньше")
        elif user_number > random_number:
            print("Ваше число больше")

print(f"Вы победили! Ваш номер: {random_number} Попыток: {user_guesses}")