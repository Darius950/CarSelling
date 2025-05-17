from domain.Car import Car
from repo.RepositoryCar import RepositoryCar
from repo.RepositoryOwner import RepositoryOwner
from service.CarService import CarService
from service.OwnerService import OwnerService
from ui.UserInterface import UserInterface



if __name__ == '__main__':
    car_repo = RepositoryCar("Cars")
    car_service = CarService(car_repo)

    owner_repo = RepositoryOwner("Owners")
    owner_service = OwnerService(owner_repo)

    ui = UserInterface(car_service, owner_service)
    ui.run()