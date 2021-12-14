inp = "В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте. (25)"

filter_out = ",.?!()[]:;"

inp = inp.lower()

for char in filter_out:
    inp = inp.replace(char, " ")

inp = inp.split(" ")

counter = {}
for word in inp:
    if word == "":
        continue
    if word not in counter:
        counter[word] = 0
    counter[word] += 1

for word in counter:
    print(f"Слово {word!r} встретилось столько раз: {counter[word]}")