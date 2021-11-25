user_input = input("Введите N: ")
user_num = int(user_input)

for i in range(1, user_num + 1):
	str_i2 = str(i*i)
	str_i = str(i)
	if (str_i2[-len(str_i):] == str_i):
		print(str_i + '*' + str_i + '=' + str_i2)