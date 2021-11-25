user_input = input("Введите натуральное число: ")

double_char = False

for i in range(1, len(user_input)):
	if user_input[i] == user_input[i - 1]:
		double_char = True
		break

print('Да.' if double_char else 'Нет.')