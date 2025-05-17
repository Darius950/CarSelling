class Owner:
    def __init__(self, id, name, surname, phone):
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__phone = phone

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_phone(self, phone):
        self.__phone = phone

    def __str__(self):
        return f"{self.__id},{self.__name},{self.__surname},{self.__phone}"

    def __eq__(self, other):
        return self.__id == other.__id