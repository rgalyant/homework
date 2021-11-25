user_input_string = input('Введите строку: ')
user_input_char = input('Введите символ: ')

last_pos = -1

is_first_run = True
was_char_found = False

while last_pos >= 0 or is_first_run:
	is_first_run = False
	last_pos = user_input_string.find(user_input_char, last_pos + 1)
	if last_pos == -1:
		if not was_char_found:
			print('Символ не найден.')
	else:
		was_char_found = True
		print('Найден символ в позиции ', last_pos)