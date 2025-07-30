from repository.fisiere.filerepo_person import *

class Service():
    """
    Clasa ce modeleaza functionalitatile de business ale aplicatiei
    """
    def __init__(self, repo_events = None, repo_people = None, inscrieri = None):
        """
        Initializeaza o instanta a clasei.
        Putem initializa instanta fara sa folosim vreun parametru
            ex: S = Service()
        :param repo_events: instanta a clasei RepoEvent
        :param repo_people: instanta a clasei RepoPerson
        :param inscrieri:  instanta a clasei TabelaInscriere
        """
        if [repo_events, repo_people, inscrieri] == [None] * 3 : repo_events, repo_people, inscrieri = None, None, None
        self.__repo_events = repo_events
        self.__repo_people = repo_people
        self.__inscrieri = inscrieri


    @staticmethod
    def _cmp_dates(zi1, luna1, an1, zi2, luna2, an2):
        """
        Compara doua date calendaristice: (zi1, luna1, an1) si (zi2, luna2, an2)
        Functie deja testata altundeva
        :params: numere intregi strict pozitive
        :return: 1, daca data caldendaristica (zi1, luna1, an1) > (zi2, luna2, an2) (s-a intamplat dupa)
                 0, daca data caldendaristica (zi1, luna1, an1) == (zi2, luna2, an2) (sunt aceeasi data)
                 -1, daca data caldendaristica (zi1, luna1, an1) < (zi2, luna2, an2) (s-a intamplat inainte)
        """
        date1 = (zi1, luna1, an1)
        date2 = (zi2, luna2, an2)
        if date1[2] == date2[2] and date1[1] == date2[1] and date1[0] == date2[0]:
            return 0
        elif date1[2] > date2[2]:
            return 1
        elif date1[2] == date2[2] and date1[1] > date2[1]:
            return 1
        elif date1[2] == date2[2] and date1[1] == date2[1] and date1[0] > date2[0]:
            return 1
        else:
            return -1


    @staticmethod
    def my_sorted(iterable, key=None, reverse=None, algorithm=None):
        """
        Replacement for the "sorted()" built-in
        Uses selection sort
        :param iterable: iterable and subscriptable type
        :param key: Tuple made out of key functions
        :param reverse: Tuple made out of booleans
        :return: the sorted iterable
        """
        if key == None: key = lambda x:x
        if reverse == None: reverse = False
        if algorithm == None: algorithm = "SelectionSort"
        if str(type(key)) == "<class 'function'>":
            keys = []
            keys.append(key)
            key = tuple(keys)
        if str(type(reverse)) == "<class 'bool'>":
            revs = []
            revs.append(reverse)
            reverse = tuple(revs)
        if len(key) < len(reverse):
            reverse = list(reverse)
            while len(key) < len(reverse): reverse.append(False)
            reverse = tuple(reverse)
        if algorithm == "SelectionSort":
            n = len(iterable)
            for i in range(n-1):
                for j in range(i+1, n):
                    cond = True
                    for k,none in enumerate(key):
                        partial_cond = key[k](iterable[j]) < key[k](iterable[i])
                        if reverse[k] == True: partial_cond = not partial_cond
                        cond = cond and partial_cond
                    if cond:
                        iterable[i], iterable[j] = iterable[j], iterable[i]
        elif algorithm in ["ShakeSort", "CocktailSort", "CocktailShakerSort", "BidirectionalBubbleSort"]:
            right = len(iterable)
            left = 0
            while right > left:
                swapped_at = left
                i = left
                while i < right - 1:
                    cond = True
                    for k,none in enumerate(key):
                        partial_cond = key[k](iterable[i+1]) < key[k](iterable[i])
                        if reverse[k] == True: partial_cond = not partial_cond
                        cond = cond and partial_cond
                    if cond:
                        iterable[i], iterable[i+1] = iterable[i+1], iterable[i]
                        swapped_at = i+1
                    i += 1
                right = swapped_at

                if left == right: break

                swapped_at = right
                i = right - 1
                while i > left:
                    i -= 1
                    cond = True
                    for k,none in enumerate(key):
                        partial_cond = key[k](iterable[i+1]) < key[k](iterable[i])
                        if reverse[k] == True: partial_cond = not partial_cond
                        cond = cond and partial_cond
                    if cond:
                        iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
                        swapped_at = i + 1
                left = swapped_at

        return iterable


    @staticmethod
    def calc_minutes(eveniment):
        return 60 * eveniment.get_timp()["ore"] + eveniment.get_timp()["min"]


    def rap_laborator12(self):
        """

        :return: lista de evenimete sortate crescator dupa descriere si descrescator dupa timp
        """
        repo_list = []
        for key in self.__repo_events.get_self():
            repo_list.append(self.__repo_events.get(key))

        return self.my_sorted(repo_list, key= (lambda x: x.get_desc(), lambda x: self.calc_minutes(x)), reverse= (False, True) )


    def rap1(self, person):
        """
        :param person: instanta valida a clasei Persoana()
        :return: (type: list), Lista de evenimente la care participă o persoană ordonat alfabetic după descriere, după dată
        """
        try:
            ValidatePerson(person)()
        except ValueError:
            raise ValueError("SERVICE ERROR! In rap1, Given entity not a valid instance of Person class!")
        try:
            if person != self.__repo_people.get(person.get_id()):
                raise ValueError("SERVICE ERROR! In rap1, Given Person instance not found in repository!")
        except KeyError:
            raise ValueError("SERVICE ERROR! In rap1, Given Person instance not found in repository!")

        event_list = []
        for key in self.__inscrieri.get_self():
            if person.get_id() in self.__inscrieri.get_self()[key]:
                event_list.append(self.__repo_events.cauta_by_id(key))

        #mai trebuie sortata lista
        n = len(event_list)
        for i in range(n-1):
            for j in range(i+1, n):
                d1 = event_list[j].get_data()["zi"], event_list[j].get_data()["luna"], event_list[j].get_data()["an"]
                d2 = event_list[i].get_data()["zi"], event_list[i].get_data()["luna"], event_list[i].get_data()["an"]
                if event_list[j].get_desc() < event_list[i].get_desc() or (event_list[j].get_desc() == event_list[i].get_desc()
                   and Service._cmp_dates(d1[0], d1[1], d1[2], d2[0], d2[1], d2[2]) <= 0):
                    event_list[i], event_list[j] = event_list[j], event_list[i]

        return event_list


    def rap2(self):
        """
        Functia returneaza lista cu persoanele care au avut cele mai multe participari la evenimente
        (toate persoanele din lista au acelasi numar de participari, care este numarul maxim)
        :return: lista cu persoanele care au avut cele mai multe participari la evenimente
        """
        participant_ids = {}

        for key in self.__inscrieri.get_self():
            for id_person in self.__inscrieri.get_self()[key]:
                if not id_person in participant_ids:
                    participant_ids[id_person] = 1
                else:
                    participant_ids[id_person] += 1

        participant_ids = self.my_sorted(list(participant_ids.items()), key= lambda x:x[1], reverse=True)
        participants = []

        for i,p in enumerate(participant_ids):
            if p[1] == participant_ids[0][1]:
                participants.append(p)
            else: break
        del(participant_ids)

        for i, p in enumerate(participants): participants[i] = p[0]

        for i,p in enumerate(participants):
            participants[i] = self.__repo_people.cauta_by_id(p)

        return participants


    def rap3(self):
        """
        Functia returneaza o lista in care se afla top 20% evenimente cu cei mai multi participanti (descriere, număr participanți)
        :return: (type: list) ale carei elemente sunt {"descriere": event.get_desc(), "participanti": nr}
                    event.get_desc() - type "str"
                    nr - type "int" pozitiv
        """
        event_list = []
        for key in self.__inscrieri.get_self():
            num_participants = len(self.__inscrieri.get_self()[key])
            event_list.append((key, num_participants))

        event_list = self.my_sorted(event_list, key= lambda x:x[1], reverse=True, algorithm="ShakeSort")

        L = len(event_list) // 5
        if L == 0 and len(event_list) > 0: L += 1
        top20pcent = event_list[:L]
        for i, ev in enumerate(top20pcent):
            top20pcent[i] = {"descriere": self.__repo_events.cauta_by_id(ev[0]).get_desc(), "participanti": ev[1]}

        return top20pcent


    def rap4(self):
        """
        :return: (type: int), Nr maxim de evenimente care au acelasi numar de persoane inscrise
        """
        event_list = []
        for key in self.__inscrieri.get_self():
            num_participants = len(self.__inscrieri.get_self()[key])
            event_list.append(num_participants)

        if event_list == [] : return 0
        event_list = sorted(event_list)

        len_max, len_seq = 0, 0
        for i in range(0, len(event_list) - 1):
            if event_list[i] == event_list[i + 1]:
                len_seq += 1
                if len_seq > len_max: len_max = len_seq
            else: len_seq = 0
        len_max += 1
        return len_max


    def stringify_repo_events(self):
        """
        :return: (type: string) toate evenimentele din repo stilizate intr-un string printabil
        """
        buffer = ""
        for key in self.__repo_events.get_self():
            buffer += str(self.__repo_events.get(key)) + '\n'
        return buffer


    def stringify_repo_people(self):
        """
        :return: (type: string) toate persoanele din repo stilizate intr-un string printabil
        """
        buffer = ""
        for key in self.__repo_people.get_self():
            buffer += str(self.__repo_people.get(key)) + '\n'
        return buffer


    def stringify_repo_events_recursive(self, l):
        """
        :param l: lista formata din id-urile evenimentelor din repository
        :return: (type: string) toate evenimentele din repo stilizate intr-un string printabil
        """
        if len(l) == 0:
            return ""
        x = str(self.__repo_events.get(l[0])) + "\n"
        return x + self.stringify_repo_events_recursive(l[1:])

    def stringify_repo_people_recursive(self, l):
        """
        :param l: lista formata din id-urile persoanelor din repository
        :return: (type: string) toate persoanele din repo stilizate intr-un string printabil
        """
        if len(l) == 0:
            return ""
        x = str(self.__repo_people.get(l[0])) + "\n"
        return x + self.stringify_repo_people_recursive(l[1:])

    def stringify_TabelaInscrieri(self):
        """
        :return: (type: string) tabela de inscrieri sub forma de string, stilizata pentru printare

        Complexitate: O(n * M) = Omega(n * m)
            n = numarul de chei din tabela de inscrieri
            M = numarul MAXIM de elemente pe care il are tabela de inscrieri la o anumita cheie
            m = numarul MINIM de elemente pe care il are tabela de inscrieri la o anumita cheie
            BestCase:    Theta(n * m)
            WorstCase:   Theta(n * M)
            AverageCase: Theta(n * (M+m)/2)
                Justificare:
                AC = Theta( n*m/(M-m) + n*(m+1)/(M-m) + n*(m+2)/(M-m) + ... + n*(m+M-m)/(M-m) ) =
                   = Theta( (n/(M-m)) * (m + m+1 + m+2 + ... + m+M-m) ) = (inmultitorul este suma lui Gauss)
                   = Theta( (n/(M-m)) * ((M-m)*m + (M-m)*(M-m+1)/2) ) = (numitorul deinmultitului anuleaza factorul comun al inmultitorului)
                   = Theta( n * (m + (M-m+1)/2) )
                   = Theta( n * (M+m+1)/2 )
                   = Theta( n * (M+m)/2 )
        """
        buffer = ""
        for key in self.__inscrieri.get_self():
            buffer += str(self.__repo_events.get(key)) + "\n"
            T = "          "
            for pers_id in self.__inscrieri.get_participants(key):
                buffer += T + str(self.__repo_people.get(pers_id)) + "\n"
            buffer += "\n"
        buffer.strip()
        buffer += "\n"
        return buffer


    def stringify_TabelaInscrieri_simplified(self):
        """
        :return: (type: string) versiune simplificata de tabela de inscrieri stilizata pentru printare
        """
        buffer = ""
        for key in self.__inscrieri.get_self():
            buffer += self.__repo_events.get(key).get_desc() + ": "
            for pers_id in self.__inscrieri.get_participants(key):
                buffer += str(self.__repo_people.get(pers_id).get_id()) + " " + self.__repo_people.get(pers_id).get_nume() + ", "
            buffer = buffer.strip(", ")
            buffer += "\n"
        return buffer


    @staticmethod
    def _test_rap1():
        r_people = RepoPerson()
        r_events = RepoEvent()
        inscrieri = TabelaInscrieri()
        S = Service(r_events, r_people, inscrieri)
        r_people.adauga(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20))
        r_people.adauga(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9))
        r_people.adauga(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22))
        r_people.adauga(Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50))
        r_people.adauga(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2))
        r_events.adauga(Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului"))
        r_events.adauga(Event(9213, 22, 9, 2001, 10, 55, "Zilele Zalaului"))
        r_events.adauga(Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"))
        inscrieri.add_participant(9871, 123)
        inscrieri.add_participant(9871, 12463)
        inscrieri.add_participant(9871, 6351)
        inscrieri.add_participant(9213, 6351)
        inscrieri.add_participant(9871, 463)
        inscrieri.add_participant(5555, 463)
        inscrieri.add_participant(5555, 46351)
        inscrieri.add_participant(5555, 6351)
        try:
            S.rap1(Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"))
            assert False
        except ValueError as err:
            assert str(err) == "SERVICE ERROR! In rap1, Given entity not a valid instance of Person class!"
        try:
            S.rap1(Person(123000, "Tudor BigHead", "Rareseni", "Ferdinand", 20))
            assert False
        except ValueError as err:
            assert str(err) == "SERVICE ERROR! In rap1, Given Person instance not found in repository!"
        try:
            S.rap1(Person(120, "Tudor SmallHead", "Rareseni", "Ferdinand", 20))
            assert False
        except ValueError as err:
            assert str(err) == "SERVICE ERROR! In rap1, Given Person instance not found in repository!"
        assert (S.rap1(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)) ==
                S.rap1(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)) )

        assert (S.rap1(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22)) ==
                [Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"),
                 Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului")])
        assert (S.rap1(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)) ==
                [Event(5555, 29, 2, 2024, 2, 10, "Campionatiul Comunal de Quiddich"),
                 Event(9213, 22, 9, 2001, 10, 55, "Zilele Zalaului"),
                 Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului")])

    @staticmethod
    def _test_rap2():
        r_people = RepoPerson()
        r_events = RepoEvent()
        inscrieri = TabelaInscrieri()
        S = Service(r_events, r_people, inscrieri)
        r_people.adauga(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20))
        r_people.adauga(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9))
        r_people.adauga(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22))
        r_people.adauga(Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50))
        r_people.adauga(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2))
        r_events.adauga(Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului"))
        r_events.adauga(Event(9213, 22, 9, 2001, 10, 55, "Batalia cu Aizen si Istvan"))
        r_events.adauga(Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"))
        assert S.rap2() == []

        inscrieri.add_participant(9871, 123)
        inscrieri.add_participant(9871, 12463)
        inscrieri.add_participant(9871, 6351)
        inscrieri.add_participant(9213, 6351)
        inscrieri.add_participant(9871, 463)
        inscrieri.add_participant(5555, 463)
        inscrieri.add_participant(5555, 46351)
        inscrieri.add_participant(5555, 6351)
        assert S.rap2() == [Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)]

        inscrieri.add_participant(9213, 463)
        assert (S.rap2() == [Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2),
                            Person(463, "Gilgamesh", "Uruk", "Gloriei", 22)]
                                                            or
                S.rap2() == [Person(463, "Gilgamesh", "Uruk", "Gloriei", 22),
                             Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)])


    @staticmethod
    def _test_rap3():
        inscrieri = TabelaInscrieri()
        r_people = RepoPerson()
        r_events = RepoEvent(inscrieri)

        S = Service(r_events, r_people, inscrieri)
        r_people.adauga(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20))
        r_people.adauga(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9))
        r_people.adauga(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22))
        r_people.adauga(Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50))
        r_people.adauga(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2))
        assert S.rap3() == []

        r_events.adauga(Event(1011, 22, 9, 2027, 3, 45, "Zilele Zalaului"))
        r_events.adauga(Event(2012, 22, 9, 2001, 10, 55, "Batalia cu Aizen si Istvan"))
        r_events.adauga(Event(3013, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"))
        rap3 = S.rap3()
        ev1 = {"descriere": "Zilele Zalaului", "participanti": 0}
        ev2 = {"descriere": "Batalia cu Aizen si Istvan", "participanti": 0}
        ev3 = {"descriere": "Campionatul Comunal de Quiddich", "participanti": 0}
        assert ev1 in rap3 or ev2 in rap3 or ev3 in rap3


        inscrieri.add_participant(1011, 123)
        inscrieri.add_participant(1011, 12463)
        inscrieri.add_participant(1011, 6351)
        inscrieri.add_participant(2012, 6351)
        inscrieri.add_participant(1011, 463)
        inscrieri.add_participant(3013, 463)
        inscrieri.add_participant(3013, 46351)
        inscrieri.add_participant(3013, 6351)
        assert S.rap3() == [{"descriere": "Zilele Zalaului", "participanti": 4}]

        r_events.adauga(Event(4014, 22, 9, 2027, 13, 00, "Gabi Mircea vs Kurt Cobain"))
        r_events.adauga(Event(5015, 22, 9, 2001, 2, 55, "Seara de Filme Hermes"))
        r_events.adauga(Event(6016, 29, 2, 2024, 2, 10, "Vizita la Malul Marii"))
        r_events.adauga(Event(7017, 22, 9, 2027, 3, 45, "Parada Tractoarelor din Municipiul Carei"))
        r_events.adauga(Event(8018, 22, 9, 2001, 10, 55, "Concursul Ursului"))
        r_events.adauga(Event(9019, 29, 2, 2024, 2, 10, "Vanatoarea de Dinozauri Cluj"))
        r_events.adauga(Event(108810, 24, 11, 2027, 0, 0, "Ziua in care Vancea termina la timp"))
        r_events.adauga(Event(118811, 22, 3, 2025, 0, 3, "Tudor si fata cu parul roz din blocul meu FAC DRAGOSTE"))
        r_events.adauga(Event(128812, 29, 2, 2024, 2, 10, "Campionatul de prins ganduri necurate"))
        inscrieri.add_participant(4014, 123)
        inscrieri.add_participant(4014, 12463)
        inscrieri.add_participant(4014, 6351)
        inscrieri.add_participant(4014, 46351)
        inscrieri.add_participant(7017, 6351)
        inscrieri.add_participant(7017, 463)
        inscrieri.add_participant(7017, 12463)
        inscrieri.add_participant(7017, 46351)
        top_ev1 = {"descriere": "Gabi Mircea vs Kurt Cobain", "participanti": 4}
        top_ev2 = {"descriere": "Parada Tractoarelor din Municipiul Carei", "participanti": 4}
        top_ev3 = {'descriere': 'Zilele Zalaului', 'participanti': 4}
        l = S.rap3()
        assert (top_ev1 in l and top_ev2 in l) or (top_ev1 in l and top_ev3 in l) or (top_ev2 in l and top_ev3 in l)


    @staticmethod
    def _test_rap4():
        inscrieri = TabelaInscrieri()
        r_people = RepoPerson()
        r_events = RepoEvent(inscrieri)
        S = Service(r_events, r_people, inscrieri)
        r_people.adauga(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20))
        r_people.adauga(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9))
        r_people.adauga(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22))
        r_people.adauga(Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50))
        r_people.adauga(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2))
        assert S.rap4() == 0

        r_events.adauga(Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului"))
        r_events.adauga(Event(9213, 22, 9, 2001, 10, 55, "Zilele Zalaului"))
        r_events.adauga(Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"))
        assert S.rap4() == 3

        inscrieri.add_participant(9871, 123)
        inscrieri.add_participant(9871, 12463)
        inscrieri.add_participant(9871, 6351)
        inscrieri.add_participant(9213, 6351)
        inscrieri.add_participant(5555, 463)
        inscrieri.add_participant(5555, 46351)
        inscrieri.add_participant(5555, 6351)
        assert S.rap4() == 2

        inscrieri.add_participant(9871, 463)
        assert S.rap4() == 1

        r_events.adauga(Event(4014, 22, 9, 2027, 13, 00, "Gabi Mircea vs Kurt Cobain"))
        r_events.adauga(Event(5015, 22, 9, 2001, 2, 55, "Seara de Filme Hermes"))
        r_events.adauga(Event(6016, 29, 2, 2024, 2, 10, "Vizita la Malul Marii"))
        r_events.adauga(Event(7017, 22, 9, 2027, 3, 45, "Parada Tractoarelor din Municipiul Carei"))
        r_events.adauga(Event(8018, 22, 9, 2001, 10, 55, "Concursul Ursului"))
        r_events.adauga(Event(9019, 29, 2, 2024, 2, 10, "Vanatoarea de Dinozauri Cluj"))
        r_events.adauga(Event(108810, 24, 11, 2027, 0, 0, "Ziua in care Vancea termina la timp"))
        r_events.adauga(Event(118811, 22, 3, 2025, 0, 3, "Tudor si fata cu parul roz din blocul meu FAC DRAGOSTE"))
        r_events.adauga(Event(128812, 29, 2, 2024, 2, 10, "Campionatul de prins ganduri necurate"))
        assert  S.rap4() == 9


    @staticmethod
    def _test_stringify_repo_events():
        inscrieri = TabelaInscrieri()
        r_people = RepoPerson()
        r_events = RepoEvent(inscrieri)
        S = Service(r_events, r_people, inscrieri)
        ev1 = Event(4014, 22, 9, 2027, 13, 00, "Gabi Mircea vs Kurt Cobain")
        ev2 = Event(5015, 22, 9, 2001, 2, 55, "Seara de Filme Hermes")
        r_events.adauga(ev1)
        r_events.adauga(ev2)
        assert S.stringify_repo_events_recursive(list(r_events.get_self().keys())) == S.stringify_repo_events() == str(ev1) + "\n" + str(ev2) + "\n"


    @staticmethod
    def _test_stringify_repo_people():
        inscrieri = TabelaInscrieri()
        r_people = RepoPerson()
        r_events = RepoEvent(inscrieri)
        S = Service(r_events, r_people, inscrieri)
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        p3 = Person(463, "Gilgamesh", "Uruk", "Gloriei", 22)
        r_people.adauga(p1)
        r_people.adauga(p2)
        r_people.adauga(p3)
        assert S.stringify_repo_people_recursive(list(r_people.get_self().keys())) == S.stringify_repo_people() == str(p1) + "\n" + str(p2) + "\n" + str(p3) + "\n"


    @staticmethod
    def _test_stringify_TabelaInscrieri_simplified():
        inscrieri = TabelaInscrieri()
        r_people = RepoPerson()
        r_events = RepoEvent(inscrieri)
        S = Service(r_events, r_people, inscrieri)
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        p3 = Person(463, "Gilgamesh", "Uruk", "Gloriei", 22)
        p4 = Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50)
        p5 = Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)
        ev1 = Event(9871, 22, 9, 2027, 13, 00, "Gabi Mircea vs Kurt Cobain")
        ev2 = Event(9213, 22, 9, 2001, 2, 55, "Seara de Filme Hermes")
        ev3 = Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich")
        r_people.adauga(p1)
        r_people.adauga(p2)
        r_people.adauga(p3)
        r_people.adauga(p4)
        r_people.adauga(p5)
        r_events.adauga(ev1)
        r_events.adauga(ev2)
        r_events.adauga(ev3)
        inscrieri.add_participant(9871, 123)
        inscrieri.add_participant(9871, 12463)
        inscrieri.add_participant(9213, 6351)

        T = "          "
        assert (S.stringify_TabelaInscrieri_simplified() ==
                ev1.get_desc() + ": " + p1.get_nume() + ", " + p2.get_nume() + "\n" + ev2.get_desc() + ": " + p3.get_nume() + "\n" + ev3.get_desc() + ": " + '\n')


    @classmethod
    def test(cls):
        cls._test_rap1()
        cls._test_rap2()
        cls._test_rap3()
        cls._test_rap4()
        cls._test_stringify_repo_events()
        cls._test_stringify_repo_people()