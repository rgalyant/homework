is_ok = False
user_input_words = []

while not is_ok:
    user_input = input("Введите 2 слова: ")
    word_pos = 0
    for index in range(len(user_input)):
        if user_input[index] == ' ':
            if user_input[word_pos:index] != '':
                user_input_words.append(user_input[word_pos:index])
            word_pos = index + 1

    if user_input[word_pos:] != '':
        user_input_words.append(user_input[word_pos:])

    print(user_input_words)

    if len(user_input_words) == 2:
        is_ok = True

result = ''
for word in user_input_words:
    for index in range(len(word)):
        char = word[-index - 1]
        result += char.lower() if index > 0 else char.upper()
    result += ' '
print(result[:-1])