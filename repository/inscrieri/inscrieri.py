from domain.validators.valid_person import *
from domain.validators.valid_event import *

class TabelaInscrieri():
    """
    Aceasta clasa modeleaza o tabela in care fiecare eveniment are o lista de id-uri de participanti
    """
    def __init__(self):
        """
        Initializeaza instanta clasei
        """
        self.__table = {}

    def add_event(self, event_id):
        """
        Adauga in tabela id-ul unui eveniment
        :param event_id: id-ul unui eveniment
        :return: void
        """
        if not event_id in self.__table.keys():
            self.__table[event_id] = []

    def add_participant(self, event_id, person_id):
        """
        Adauga in tabela id-ul persoanei la cheia ce reprezinta id-ul evenimentului
        :param event_id: int
        :param person_id: int
        :return: void
        """
        if event_id in self.__table:
            if not person_id in self.__table[event_id]:
                self.__table[event_id].append(person_id)
        else:
            self.__table[event_id] = []
            self.__table[event_id].append(person_id)

    def del_event(self, event_id):
        """
        Sterge din tabela cheia ce reprezinta id-ul evenimentului si toate elementele de la acea cheie
        :param event_id: int
        :return: void
        """
        if event_id in self.__table:
            del self.__table[event_id]

    def del_participant_from_event(self, event_id, person_id):
        """
        Sterge de la cheia "event_id" din tabela participantul cu id "person_id"
        :param event_id: int
        :param person_id: int
        :return: void
        """
        if event_id in self.__table:
            if person_id in self.__table[event_id]:
                self.__table[event_id].remove(person_id)


    def get_self(self):
        return self.__table

    def get_participants(self, id_event):
        return self.__table[id_event]

    def __len__(self):
        return len(self.__table)

    @staticmethod
    def _test_add_event():
        T = TabelaInscrieri()
        T.add_event(123)
        T.add_event(123)
        T.add_event(155)
        T.add_event(213)
        T.add_event(155)
        assert len(T) == 3
        """
        r = RepoEvent()
        r.adauga(Event(123, 22, 10, 2004, 3, 30, "Facerea I"))
        r.adauga(Event(155, 22, 10, 2005, 3, 30, "Facerea II"))
        r.adauga(Event(213, 22, 10, 2006, 3, 30, "Facerea III"))
        try:
            T.add_event(0, r)
            assert False
        except ValueError as err:
            assert str(err) == "SERVICE ERROR! For TabelaInscrieri entity, In add_event: ID NOT VALID!"
        try:
            T.add_event(["Tractor1", 'Tractor2'], r)
            assert False
        except ValueError as err:
            assert str(err) == "SERVICE ERROR! For TabelaInscrieri entity, In add_event: ID NOT VALID!"
        try:
            T.add_event(5000, r)
            assert False
        except ValueError as err:
            assert str(err) == "SERVICE ERROR! For TabelaInscrieri entity, In add_event: ID NOT FOUND!"
        """

    @staticmethod
    def _test_add_person():
        T = TabelaInscrieri()
        T.add_event(123)
        T.add_event(155)
        T.add_event(155)
        T.add_participant(123, 501)
        T.add_participant(123, 513)
        T.add_participant(123, 501)
        T.add_participant(155, 555)
        T.add_participant(155, 555)
        T.add_participant(155, 555)
        assert len(T.get_participants(123)) == 2
        assert len(T.get_participants(155)) == 1

    @staticmethod
    def _test_del_event():
        T = TabelaInscrieri()
        T.add_event(123)
        T.add_event(155)
        T.add_event(155)
        T.add_event(106)
        T.add_event(107)

        T.del_event(155)
        assert len(T) == 3
        T.del_event(100)
        assert len(T) == 3
        T.del_event(106)
        assert len(T) == 2
        T.del_event(123)
        T.del_event(107)
        assert len(T) == 0

    @staticmethod
    def _test_del_participant_from_event():
        T = TabelaInscrieri()
        T.add_event(123)
        T.add_event(155)
        T.add_participant(107, 555)
        T.add_participant(123, 555)
        T.add_participant(123, 501)

        T.del_participant_from_event(107, 123124)
        T.del_participant_from_event(123, 52323)
        assert len(T.get_participants(123)) == 2
        T.del_participant_from_event(123, 555)
        assert len(T.get_participants(123)) == 1
        T.del_participant_from_event(123,501)
        assert len(T.get_participants(123)) == len(T.get_participants(155)) == 0

    @classmethod
    def test(cls):
        cls._test_add_event()
        cls._test_add_person()
        cls._test_del_event()
        cls._test_del_participant_from_event()
