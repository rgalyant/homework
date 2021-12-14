inp = """
Стоишь на берегу и чувствуешь соленый запах ветра, что веет с моря, и веришь,
что свободен ты и жизнь лишь началась, и губы жжет подруги поцелуй, пропитанный слезой!
"""

filter_out = "!\"#$%&'()*+,\n -./:;<=>?@[\]^_`{|}~"

inp = inp.lower().split()

most_often = ("", 0)
counter = {}
for word in inp:
    word = word.strip(filter_out)
    if word == "" or word.isnumeric():
        continue
    if word not in counter:
        counter[word] = 0
    counter[word] += 1

    if counter[word] >= most_often[1]:
        most_often = (word, counter[word])

print(f"Слово {most_often[0]!r} встретилось столько раз: {most_often[1]}")