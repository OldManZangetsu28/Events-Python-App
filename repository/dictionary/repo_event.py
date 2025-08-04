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
