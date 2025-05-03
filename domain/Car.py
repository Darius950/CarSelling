class Car:
    def __init__(self,id ,brand, model, fuel, color, cm3, hp, body_type):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__fuel = fuel
        self.__color = color
        self.__cm3 = cm3
        self.__hp = hp
        self.__body_type = body_type

    def get_id(self):
        return self.__id

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_fuel(self):
        return self.__fuel

    def get_color(self):
        return self.__color

    def get_cm3(self):
        return self.__cm3

    def get_hp(self):
        return self.__hp

    def get_body_type(self):
        return self.__body_type

    def set_id(self, new_id):
        self.__id = new_id

    def set_brand(self,brand):
        self.__brand = brand

    def set_model(self,model):
        self.__model = model

    def set_fuel(self,fuel):
        self.__fuel = fuel

    def set_color(self,color):
        self.__color = color

    def set_cm3(self,cm3):
        self.__cm3 = cm3

    def set_hp(self,hp):
        self.__hp = hp

    def set_body_type(self,body_type):
        self.__body_type = body_type

    def __str__(self):
        return (f"{self.__id},{self.__brand}, {self.__model}, {self.__fuel},"
                f" {self.__color}, {self.__cm3}, {self.__hp}, {self.__body_type}")

    def __eq__(self,other):
        return (self.__brand==other.__brand and self.__model==other.model
                and self.__fuel==other.__fuel and self.__color==other.__color
                and self.__cm3==other.__cm3 and self.__hp==other.__hp
                and self.__body_type==other.__body_type)