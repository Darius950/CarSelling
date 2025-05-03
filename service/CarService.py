from domain.Car import Car
from repo.Repository import Repository


class CarService:
    def __init__(self, repo:Repository):
        self.__repo = repo

    def add(self, brand:str, model:str, fuel:str,
            color:str, cm3:int, hp:int, body_type:str):
        car = Car(brand, model, fuel, color, cm3, hp, body_type)
        self.__repo.add(car)
        """
        Adauga o masina in repository. Cu ajutorul atributelor masinii creeam o masina 
        si o adaugam in repository.
        """

    def get_size(self):
        return self.__repo.get_size()

    def get_all(self):
        return self.__repo.get_all()