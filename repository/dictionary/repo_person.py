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
