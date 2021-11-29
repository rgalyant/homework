user_input = int(input('Input number from 3 to 9: '))

if user_input < 3 or user_input > 9:
	print('Not in range')
else:
	string = ""
	for i in range(1, 10):
		string += f'{i}';
		print(f'{string}{string[:-1][::-1]}')

