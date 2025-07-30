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
        id_person = person.get_id()
        if id_person in self.__people:
            raise ValueError("REPO ERROR in adauga! Person entity NOT UNIQUELEY IDENTIFIED!")
        self.__people.append(person)

    def cauta_by_id(self, id_person):
        if id_person not in self.__people:
            raise ValueError("REPO ERROR in cauta_by_id! ID not found!")
        for pers in self.__people:
            if pers.get_id() == id_person:
                return pers

    def sterge_by_id(self, id_person):
        if id_person not in self.__people:
            raise ValueError("REPO ERROR in sterge_by_id! ID not found!")
        for pers in self.__people:
            if pers.get_id() == id_person:
                self.__people.remove(pers)

    def update(self, person):
        try:
            ValidatePerson(person)()
        except ValueError:
            raise ValueError("REPO ERROR in update! Person entity NOT VALID!")
        id_person = person.get_id()
        if id_person not in self.__people:
            raise ValueError("REPO ERROR in update! Person entity NOT FOUND!")
        for i, pers in enumerate(self.__people):
            if pers.get_id() == id_person:
                self.__people[i] = person


    def get(self):
        return self.__people

    @staticmethod
    def test_adauga():
        invalid_p0 = Person(0, "Gicu Coste123a", 5, "Clujeana", -22)
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(123, "Gicu Costea", "Bordieni", "Clujeana", 22)
        p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        r = Repo()
        try:
            r.adauga(invalid_p0)
        except ValueError as err:
            assert str(err) == "REPO ERROR in adauga! Person entity NOT VALID!"
        r.adauga(p1)
        try:
            r.adauga(p2)
        except ValueError as err:
            assert str(err) == "REPO ERROR in adauga! Person entity NOT UNIQUELEY IDENTIFIED!"
        r.adauga(p3)
        assert r.get()[p1.get_id()] == p1
        assert r.get()[p3.get_id()] == p3

    @staticmethod
    def test_cauta_by_id():
        repo = Repo()
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(1200, "Gicu Costea", "Bordieni", "Clujeana", 22)
        repo.adauga(p1)
        repo.adauga(p2)
        found_p = repo.cauta_by_id(123)
        assert found_p == p1

    @staticmethod
    def test_update():
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(300, "Gicu Costea", "Bordieni", "Clujeana", 22)
        p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        repo = Repo()
        repo.adauga(p1)
        repo.adauga(p2)
        repo.adauga(p3)
        invalid_update_p1 = Person(0, "Gicu Coste123a", 5, "Clujeana", -22)
        invalid_update_p2 = Person(301, "Gigi Costica", "Burdujeni", "Clujului", 27)
        try:
            repo.update(invalid_update_p1)
        except ValueError as err:
            assert str(err) == "REPO ERROR in update! Person entity NOT VALID!"
        try:
            repo.update(invalid_update_p2)
        except ValueError as err:
            assert str(err) == "REPO ERROR in update! Person entity NOT FOUND!"
        update_p1 = Person(300, "Gigi Costica", "Burdujeni", "Clujului", 27)
        repo.update(update_p1)
        new_pers = repo.cauta_by_id(300)
        assert new_pers == update_p1

    @staticmethod
    def test_sterge_by_id():
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        repo = Repo()
        repo.adauga(p1)
        repo.adauga(p3)
        repo.sterge_by_id(123)
        assert len(repo.get()) == 1
    
    @classmethod
    def test(cls):
        cls.test_adauga()
        cls.test_cauta_by_id()
        cls.test_update()
        cls.test_sterge_by_id()
