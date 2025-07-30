from repository.inscrieri.validator_inscrieri import *
class RepoEvent():
    """
    Clasa ce modeleaza persistenta in memeoria RAM a entitatilor de tip Eveniment
    """
    def __init__(self, T_inscrieri=None):
        if T_inscrieri == None:
            self.__inscrieri = None
        else:
            self.__inscrieri = T_inscrieri
        self.__events = {}

    def adauga(self, event):
        try:
            ValidateEvent(event)()
        except ValueError:
            raise ValueError("REPO ERROR in adauga! Event entity NOT VALID!")
        id_event = event.get_id()
        if id_event in self.__events:
            raise ValueError("REPO ERROR in adauga! Event entity NOT UNIQUELEY IDENTIFIED!")
        self.__events[id_event] = event
        if self.__inscrieri != None: self.__inscrieri.add_event(id_event)


    def cauta_by_id(self, id_event):
        if id_event not in self.__events:
            raise ValueError("REPO ERROR in cauta_by_id! ID not found!")
        return self.__events[id_event]

    def sterge_by_id(self, id_event):
        if id_event not in self.__events:
            raise ValueError("REPO ERROR in sterge_by_id! ID not found!")
        del self.__events[id_event]
        if self.__inscrieri != None: self.__inscrieri.del_event(id_event)

    def update(self, event):
        try:
            ValidateEvent(event)()
        except ValueError:
            raise ValueError("REPO ERROR in update! Event entity NOT VALID!")
        id_event = event.get_id()
        if id_event not in self.__events:
            raise ValueError("REPO ERROR in update! Event entity NOT FOUND!")
        self.__events[id_event] = event

    def get_self(self):
        return self.__events

    def get(self, id_event):
        """
        Getter al unui singur item al repo-ului
        (Spre deosebire de get_self, care este un getter al intregului repo)
        :param id_event: id-ul unei persone
        :return: persoana cu id-ul dat
        """
        return self.__events[id_event]

    @staticmethod
    def _test_adauga():
        invalid_p0 = Event(0, "Gicu Coste123a", 5, "Clujeana", -22)
        p1 = Event(123, 22, 10, 2004, 3, 30, "Facerea")
        p2 = Event(12111, 22, 1, 2004, 2, 0, "Existenta")
        p3 = Event(1233, 22, 12, 2004, 1, 20, "Distrugerea")
        r = RepoEvent()
        try:
            r.adauga(invalid_p0)
        except ValueError as err:
            assert str(err) == "REPO ERROR in adauga! Event entity NOT VALID!"
        r.adauga(p1)
        try:
            r.adauga(p2)
        except ValueError as err:
            assert str(err) == "REPO ERROR in adauga! Event entity NOT UNIQUELEY IDENTIFIED!"
        r.adauga(p3)
        assert r.get_self()[p1.get_id()] == p1
        assert r.get_self()[p3.get_id()] == p3

    @staticmethod
    def _test_cauta_by_id():
        repo = RepoEvent()
        p1 = Event(123, 22, 10, 2004, 3, 30, "Facerea")
        p2 = Event(12111, 22, 1, 2004, 2, 0, "Existenta")
        p3 = Event(1233, 22, 12, 2004, 1, 20, "Distrugerea")
        repo.adauga(p1)
        repo.adauga(p2)
        found_p = repo.cauta_by_id(123)
        assert found_p == p1

    @staticmethod
    def _test_update():
        p1 = Event(123, 22, 10, 2004, 3, 30, "Facerea")
        p2 = Event(12111, 22, 1, 2004, 2, 0, "Existenta")
        p3 = Event(1233, 22, 12, 2004, 1, 20, "Distrugerea")
        repo = RepoEvent()
        repo.adauga(p1)
        repo.adauga(p2)
        repo.adauga(p3)
        invalid_update_p1 = Event(0, "Gicu Coste123a", 5, "Clujeana", -22)
        invalid_update_p2 = Event(124001, 22, 1, 2004, 2, 0, "Existenta")
        try:
            repo.update(invalid_update_p1)
        except ValueError as err:
            assert str(err) == "REPO ERROR in update! Event entity NOT VALID!"
        try:
            repo.update(invalid_update_p2)
        except ValueError as err:
            assert str(err) == "REPO ERROR in update! Event entity NOT FOUND!"
        update_p1 = Event(123, 1, 11, 2000, 3, 30, "Geneza")
        repo.update(update_p1)
        new_pers = repo.cauta_by_id(123)
        assert new_pers == update_p1

    @staticmethod
    def _test_sterge_by_id():
        p1 = Event(123, 22, 10, 2004, 3, 30, "Facerea")
        p3 = Event(1233, 22, 12, 2004, 1, 20, "Distrugerea")
        repo = RepoEvent()
        repo.adauga(p1)
        repo.adauga(p3)
        repo.sterge_by_id(123)
        assert len(repo.get_self()) == 1
    @classmethod
    def test(cls):
        cls._test_adauga()
        cls._test_cauta_by_id()
        cls._test_update()
        cls._test_sterge_by_id()
