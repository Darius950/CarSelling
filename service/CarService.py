from domain.Car import Car
from repo.RepositoryCar import RepositoryCar


class CarService:
    def __init__(self, repo:RepositoryCar):
        self.__repo = repo

    def add(self, id:int, brand:str, model:str, fuel:str,
            color:str, cm3:int, hp:int, body_type:str):
        car = Car(id, brand, model, fuel, color, cm3, hp, body_type)
        self.__repo.add(car)
        """
        Adauga o masina in repository. Cu ajutorul atributelor masinii creeam o masina 
        si o adaugam in repository.
        """
    def remove(self, id:int):
        if self.exist_by_id(id):
            self.__repo.delete(self.find_by_id(id))

    def find_by_id(self, id:int):
        if self.exist_by_id(id):
            for elem in self.get_all():
                if elem.get_id() == id:
                    return elem
        print("Masina nu exista.")

    def exist_by_id(self, id):
        for elem in self.get_all():
            if elem.get_id() == id:
                return True
        return False

    def get_size(self):
        return self.__repo.get_size()

    def get_all(self):
        return self.__repo.get_all()