from service.CarService import CarService
from service.OwnerService import OwnerService


class UserInterface:
    def __init__(self, srv_car: CarService, srv_owner: OwnerService):
        self.__srv_car = srv_car
        self.__srv_owner = srv_owner

    def run(self):
        while True:
            self.print_main_menu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.menu_owner()
            elif optiune == "2":
                self.menu_car()
            elif optiune == "x" or optiune == "X":
                break
            else:
                print("Optiune gresita.")

    def print_main_menu(self):
        print("Welcome main menu")
        print("1. Owner menu")
        print("2. Car menu")
        print("x. Leave App")

    # CAR STUFF

    def print_car_menu(self):
        print("Welcome to Car System")
        print("1. Add car")
        print("2. View cars")
        print("3. Delete car")
        print("x. Exit to main menu")

    def menu_car(self):
        while True:
            self.print_car_menu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_add_car()
            elif optiune == "2":
                self.show_all_cars()
            elif optiune == "3":
                self.ui_del_car()
            elif optiune == "x" or optiune == "X":
                break
            else:
                print("Optiune gresita.")

    def ui_add_car(self):
        id = 1
        while self.__srv_car.exist_by_id(id):
            id += 1
        brand = input("Dati brand: ")
        model = input("Dati model: ")
        fuel = input("Dati fuel: ")
        color = input("Dati color: ")
        cm3 = int(input("Dati cm3: "))
        hp = int(input("Dati hp: "))
        body_type = input("Dati body_type: ")
        self.__srv_car.add(id, brand, model, fuel, color, cm3, hp, body_type)
        print("Masina a fost adaugata cu succes.")

    def show_all_cars(self):
        '''
        for i in range (self.__srv_car.get_size()):
            print(self.__srv_car.get_all()[i])
        '''
        if self.__srv_car.get_size() == 0:
            print("No cars added.\n")
            return
        for elem in self.__srv_car.get_all():
            print(elem)

    def ui_del_car(self):
        self.show_all_cars()
        id = int(input("Dati id-ul masinii de sters: "))
        self.__srv_car.remove(id)
        print("Masinia a fost stearsa cu succes!")

    #END CAR STUFF

    # OWNER STUFF
    def print_owner_menu(self):
        print("Welcome to Owner System")
        print("1. Add owner")
        print("2. View owners")
        print("3. Delete owner")
        print("x. Exit to main menu")

    def menu_owner(self):
        while True:
            self.print_owner_menu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_add_owner()
            elif optiune == "2":
                self.show_all_owners()
            elif optiune == "3":
                self.ui_del_owner()
            elif optiune == "x" or optiune == "X":
                break
            else:
                print("Optiune gresita.")

    def ui_add_owner(self):
        id = 1
        while self.__srv_owner.exist_by_id(id):
            id += 1
        name = input("Dati numele ownerului: ")
        surname = input("Dati prenumele ownerului: ")
        phone = input("Dati numarul de telefon: ")
        self.__srv_owner.add_owner(id, name, surname, phone)

    def show_all_owners(self):
        for owner in self.__srv_owner.get_all_owners():
            print(owner)

    def ui_del_owner(self):
        self.show_all_owners()
        id = int(input("Dati id-ul ownerului de sters: "))
        self.__srv_owner.remove_owner(id)
        print("Ownerul a fost sters cu succes!")
