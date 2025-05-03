from service.CarService import CarService


class UserInterface:
    def __init__(self, srv:CarService):
        self.__srv = srv

    def run(self):
        while True:
            self.print_menu()
            optiune=input("Dati optiunea: ")
            if optiune=="1":
                self.ui_add_car()
            elif optiune=="2":
                self.show_all()
            elif optiune=="x" or optiune=="X":
                break
            else:
                print("Optiune gresita.")


    def print_menu(self):
        print("Welcome to Car System")
        print("1. Add car")
        print("2. View cars")
        print("x. Exit")

    def ui_add_car(self):
        brand = input("Dati brand: ")
        model = input("Dati model: ")
        fuel = input("Dati fuel: ")
        color = input("Dati color: ")
        cm3 = int(input("Dati cm3: "))
        hp = int(input("Dati hp: "))
        body_type = input("Dati body_type: ")
        self.__srv.add(brand, model, fuel, color, cm3, hp, body_type)
        print("Masina a fost adaugata cu succes.")

    def show_all(self):
        '''
        for i in range (self.__srv.get_size()):
            print(self.__srv.get_all()[i])
        '''
        if  self.__srv.get_size() == 0:
            print("No cars added.\n")
            return
        for elem in self.__srv.get_all():
            print(elem)