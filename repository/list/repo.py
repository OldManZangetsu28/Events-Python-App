from domain.validators.valid_person import *

class Repo():
    """
    Clasa ce modeleaza persistenta in memeoria RAM a entitatilor de tip Persoana
    Vechi si neutilizat in program.
    !!!NU SE RECOMANDA UTILIZAREA LUI!!!
    """
    def __init__(self):
        self.__people = []

    def adauga(self, person):
        try:
            ValidatePerson(person)()
        except ValueError:
            raise ValueError("REPO ERROR in adauga! Person entity NOT VALID!")
        if person in self.__people:
            raise ValueError("REPO ERROR in adauga! Person entity NOT UNIQUELEY IDENTIFIED!")
        self.__people.append(person)

    def cauta_by_id(self, id_person):
        for pers in self.__people:
            if pers.get_id() == id_person:
                return pers
        raise ValueError("REPO ERROR in cauta_by_id! ID not found!")

    def sterge_by_id(self, id_person):
        for pers in self.__people:
            if pers.get_id() == id_person:
                self.__people.remove(pers)
                return None
        raise ValueError("REPO ERROR in sterge_by_id! ID not found!")

    def update(self, person):
        try:
            ValidatePerson(person)()
        except ValueError:
            raise ValueError("REPO ERROR in update! Person entity NOT VALID!")
        id_person = person.get_id()
        for i, pers in enumerate(self.__people):
            if pers.get_id() == id_person:
                self.__people[i] = person
                return None
        raise ValueError("REPO ERROR in update! Person entity NOT FOUND!")


    def get(self):
        return self.__people
