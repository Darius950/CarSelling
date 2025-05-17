from domain.Owner import Owner
from repo.RepositoryOwner import RepositoryOwner


class OwnerService:
    def __init__(self, repo: RepositoryOwner):
        self.__repo = repo

    def add_owner(self, id, name, surname, phone):
        if self.__repo.find_by_id(id) is not None:
            print("Proprietar cu acest ID deja există.")
            return
        owner = Owner(id, name, surname, phone)
        self.__repo.add(owner)

    def remove_owner(self, id):
        owner = self.__repo.find_by_id(id)
        if owner:
            self.__repo.delete(owner)

    def exist_by_id(self, id):
        for elem in self.get_all_owners():
            if elem.get_id() == id:
                return True
        return False

    def get_all_owners(self):
        return self.__repo.get_all()