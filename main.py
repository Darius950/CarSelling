from domain.Car import Car
from repo.Repository import Repository
from service.CarService import CarService
from ui.UserInterface import UserInterface

if __name__ == '__main__':
    repo = Repository("Cars")
    srv = CarService(repo)
    ui = UserInterface(srv)

    ui.run()