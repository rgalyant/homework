class Buffer:
    def __init__(self):
        self.__length = 0
        self.__array = [ None ] * 5

    def add(self, *a):
        for n in a:
            self.__array[self.__length] = n
            self.__length += 1

            if self.__length == 5:
                print("Sum of five:", sum(self.__array))
                self.__length = 0

    def get_current_part(self):
        return self.__array[:self.__length]

if __name__ == "__main__":
    from random import randint
    random_data = [ randint(0, 50) for _ in range(50) ]
    print("Input data:", ", ".join([ str(n) for n in random_data ]))
    print("Input sums:", ", ".join([ str(sum(random_data[i * 5 : i * 5 + 5])) for i in range(10) ]))

    buffer = Buffer()

    print("Current input: ", random_data[0])
    buffer.add(random_data[0])

    print("Current input: ", *random_data[1:4])
    buffer.add(*random_data[1:4])

    print("Current input: ", *random_data[4:14])
    buffer.add(*random_data[4:14])

    print("Current state: ", buffer.get_current_part())

    print("Current input: ", *random_data[14:])
    buffer.add(*random_data[14:])