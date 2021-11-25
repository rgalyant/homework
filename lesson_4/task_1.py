user_input = input("Введите натуральное число: ")

nums = [0] * 10
double_num = False

for character in user_input:
	if character in '0123456789':
		index = int(character)
		nums[index] += 1
		double_num = nums[index] > 1
	if double_num:
		break

print('Да.' if double_num else 'Нет.')