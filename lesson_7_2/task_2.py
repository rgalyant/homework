students = (
  ("Иван", 18, 7.1, "Киев"),
  ("Светлана", 20, 8.2, "Киев"),
  ("Дмитрий", 19, 5.1, "Фастов"),
  ("Николай", 18, 7.0, "Одесса"),
  ("Стас", 18, 6.7, "Киев"),
  ("Илона", 20, 9.9, "Жмерынка"),
  ("Надя", 21, 8.6, "Маякы")
)

average = sum([mark for name, age, mark, city in students]) / len(students)
good_ones = []
for name, age, mark, city in students:
    if mark >= average:
        good_ones.append(name)
print("Ученики", ", ".join(good_ones), "в этом семестре хорошо учатся!")