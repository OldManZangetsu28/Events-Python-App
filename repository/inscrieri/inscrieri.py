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
