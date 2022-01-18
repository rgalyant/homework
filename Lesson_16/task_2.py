class Student:
    __slots__ = ("_name", "_age", "grades")

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.grades = []
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Group:
    __slots__ = ("students")

    def __init__(self):
        self.students = []

    def print(self):
        print("{:15} {:7} {}".format("Имя", "Возраст", "Оценки"))
        print('=' * 15, '=' * 7, '=' * 30)
        for student in self.students:
            print("{:15} {:7} {}"
                .format(student.name, str(student.age), ', '.join([str(grade) for grade in student.grades])))

if __name__ == "__main__":
    from random import randint

    names = [ "Рустам", "Илья", "Андрей", "Владимир", "Алексей", "Евгений", "Иван" ]

    group = Group()
    for name in names:
        student = Student(name, randint(18, 30))
        student.grades = [randint(9, 12) for _ in range(randint(5, 8))]
        group.students.append(student)

    group.print()