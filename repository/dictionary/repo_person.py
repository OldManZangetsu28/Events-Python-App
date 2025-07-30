from repository.dictionary.repo_event import *
class RepoPerson():
    """
    Clasa ce modeleaza persistenta in memeoria RAM a entitatilor de tip Persoana
    """
    def __init__(self, T_inscrieri = None):
        self.__people = {}
        if T_inscrieri == None:
            self.__inscrieri = None
        else:
            self.__inscrieri = T_inscrieri

    def adauga(self, person):
        try:
            ValidatePerson(person)()
        except ValueError:
            raise ValueError("REPO ERROR in adauga! Person entity NOT VALID!")
        id_person = person.get_id()
        if id_person in self.__people:
            raise ValueError("REPO ERROR in adauga! Person entity NOT UNIQUELEY IDENTIFIED!")
        self.__people[id_person] = person

    def cauta_by_id(self, id_person):
        if id_person not in self.__people:
            raise ValueError("REPO ERROR in cauta_by_id! ID not found!")
        return self.__people[id_person]

    def sterge_by_id(self, id_person):
        if id_person not in self.__people:
            raise ValueError("REPO ERROR in sterge_by_id! ID not found!")
        del self.__people[id_person]
        if self.__inscrieri != None:
            for key in self.__inscrieri.get_self():
                if id_person in self.__inscrieri.get_self()[key]:
                    self.__inscrieri.del_participant_from_event(key, id_person)

    def update(self, person):
        try:
            ValidatePerson(person)()
        except ValueError:
            raise ValueError("REPO ERROR in update! Person entity NOT VALID!")
        id_person = person.get_id()
        if id_person not in self.__people:
            raise ValueError("REPO ERROR in update! Person entity NOT FOUND!")
        self.__people[id_person] = person


    def get_self(self):
        return self.__people

    def get(self, id_person):
        """
        Getter al unui singur item al repo-ului
        (Spre deosebire de get_self, care este un getter al intregului repo)
        :param id_person: id-ul unei persone
        :return: persoana cu id-ul dat
        """
        return self.__people[id_person]

    @staticmethod
    def _test_adauga():
        invalid_p0 = Person(0, "Gicu Coste123a", 5, "Clujeana", -22)
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(123, "Gicu Costea", "Bordieni", "Clujeana", 22)
        p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        r = RepoPerson()
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
        assert r.get_self()[p1.get_id()] == p1
        assert r.get_self()[p3.get_id()] == p3

    @staticmethod
    def _test_cauta_by_id():
        repo = RepoPerson()
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(1200, "Gicu Costea", "Bordieni", "Clujeana", 22)
        repo.adauga(p1)
        repo.adauga(p2)
        found_p = repo.cauta_by_id(123)
        assert found_p == p1

    @staticmethod
    def _test_update():
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(300, "Gicu Costea", "Bordieni", "Clujeana", 22)
        p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        repo = RepoPerson()
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
    def _test_sterge_by_id():
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        repo = RepoPerson()
        repo.adauga(p1)
        repo.adauga(p3)
        repo.sterge_by_id(123)
        assert len(repo.get_self()) == 1
        repo.sterge_by_id(12463)
        assert len(repo.get_self()) == 0
    @classmethod
    def test(cls):
        cls._test_adauga()
        cls._test_cauta_by_id()
        cls._test_update()
        cls._test_sterge_by_id()
