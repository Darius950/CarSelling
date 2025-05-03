from domain.Car import Car

'''
CRUD
Create
Read
Update
Delete
'''


class Repository:
    def __init__(self, filename):
        self.__filename = filename
        self.__repo = self.__read()

    def __read(self):
        result = []
        with open(self.__filename, "r") as f:
            file = f.read()
        lines = file.split("\n")
        if len(lines) > 1:
            for line in lines:
                if len(line) > 2:
                    line = line.split(',')
                    result.append(Car(int(line[0]), line[1], line[2],
                                      line[3], line[4], int(line[5]), int(line[6]), line[7]))
        return result

    def __write(self):
        with open(self.__filename, "w") as f:
            for car in self.__repo:
                f.write(f"{car}\n")

    def add(self, car: Car):
        """"
        Adauga o masina in lista.
        """
        self.__repo.append(car)
        self.__write()

    def delete(self, car: Car):
        self.__repo.remove(car)
        self.__write()

    def get_size(self):
        return len(self.__repo)

    def get_all(self):
        return self.__repo
