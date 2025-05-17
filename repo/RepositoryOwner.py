from domain.Owner import Owner

class RepositoryOwner:
    def __init__(self, filename):
        self.__filename = filename
        self.__owners = self.__read()

    def __read(self):
        result = []
        try:
            with open(self.__filename, "r") as f:
                lines = f.read().splitlines()
                for line in lines:
                    if line.strip():
                        parts = line.split(",")
                        result.append(Owner(int(parts[0]), parts[1], parts[2], parts[3]))
        except FileNotFoundError:
            pass
        return result

    def __write(self):
        with open(self.__filename, "w") as f:
            for owner in self.__owners:
                f.write(str(owner) + "\n")

    def add(self, owner: Owner):
        self.__owners.append(owner)
        self.__write()

    def delete(self, owner: Owner):
        self.__owners.remove(owner)
        self.__write()

    def get_all(self):
        return self.__owners

    def find_by_id(self, id):
        for owner in self.__owners:
            if owner.get_id() == id:
                return owner
        return None