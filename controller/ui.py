from service.service import *
class UI():
    """
    Clasa ce modeleaza interfata cu utilizatorul, de tip consola
    """
    __inscrieri = TabelaInscrieri()
    __repo_events = RepoEvent(__inscrieri)
    __repo_people = RepoPerson(__inscrieri)
    __service = Service(__repo_events, __repo_people, __inscrieri)

    def __init__(self):
        pass

    @staticmethod
    def com0():
        print("Sample command executed!")


    @staticmethod
    def help():
        print("help: afiseaza toate comenzile disponibile")
        print("exit: iesi din program")
        print("show_people: afiseaza toate persoanele adaugate")
        print("show_events: afiseaza toate evenimentele adaugate")
        print("add_person: adauga o persoana")
        print("generate_people: adauga n persoane generata aleatoriu")
        print("add_event: adauga un eveniment")
        print("mod_person: modifica o persoana")
        print("mod_event: modifica un eveniment")
        print("del_person: sterge o persoana")
        print("del_event: sterge un eveniment")
        print("find_person: gaseste o persoana")
        print("find_event: gaseste un eveniment")
        print("add_inscriere: inscrie o persoana la un eveniment")
        print("rap1: afiseaza lista de evenimente la care participă o persoană ordonat alfabetic după descriere, după dată")
        print("rap2: afiseaza persoane participante la cele mai multe evenimente")
        print("rap3: afiseaza primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți)")
        print("rap4: afiseaza nr maxim de evenimente care au acelasi numar de persoane inscrise")
        print("rap_lab12: afiseaza o lista de evenimente sortata crescator dupa nume, descrescator dupa durata de timp")
        print("show_inscrieri: afiseaza toate evenimentele si persoanele inscrise")
        print("show_ins_simplilied: afiseaza o versiune simplificata a comenzii de mai sus")



    @classmethod
    def add_person(cls):
        while True:
            try:
                id = input("ID-ul persoanei: ")
                nume = input("numele persoanei: ")
                oras = input("orasul de domiciliu: ")
                strada = input("strada: ")
                numar = input("numarul: ")
                p = Person(int(id), nume, oras, strada, int(numar))
                ValidatePerson(p)()
                cls.__repo_people.adauga(p)
                print("Persoana adaugata cu succes!")
                break
            except ValueError as err:
                print()
                print(err)
                print("Persoana invalida, mai incercati o data.")
                print()


    @staticmethod
    def generate_random_string(max_length):
        """
        Generaza string aleatoriu
        :param max_length: numar intreg mai mare decat 1
        :return: string format din litere mici aleatorii de lungime <= cu max_length
        """
        if not(str(type(max_length)) == "<class 'int'>") or max_length <= 1:
            raise ValueError("In generate_random_string(), GIVEN INPUT NOT VALID!")
        from random import randrange
        length = randrange(1, max_length)
        string = ""
        for i in range(length):
            ch = chr(randrange(97, 122))
            string += ch
        return string


    @classmethod
    def generate_people(cls):
        import random
        tabela_id = {}
        while True:
            try:
                number = int(input("Cate persoane doriti sa generati: "))
                break
            except:
                print("Numar invalid!")
        for key in cls.__repo_people.get_self():
            tabela_id[key] = 1
        id_limit = 99999
        for attempt in range(number):
            id = random.randrange(1, id_limit)
            while id in tabela_id and tabela_id[id] == 1:
                id = random.randrange(1, id_limit)
            nume = cls.generate_random_string(20).capitalize()
            oras = cls.generate_random_string(10).capitalize()
            strada = cls.generate_random_string(10).capitalize()
            numar = random.randrange(1, 200)
            cls.__repo_people.adauga(Person(id, nume, oras, strada, numar))
            tabela_id[id] = 1
            id_limit += 1
        print("Persoane aleatoare adaugata cu succes!")


    @classmethod
    def add_event(cls):
        while True:
            try:
                id = input("ID-ul evenimentului: ")
                print("Data desfășurării: ")
                z = input("    ziua: ")
                l = input("    luna: ")
                a = input("    anul: ")
                print("Durata evenimentului: ")
                h = input("    ore: ")
                m = input("    minute: ")
                desc = input("Descrierea evenimentului: ")
                ev = Event(int(id), int(z), int(l), int(a), int(h), int(m), desc)
                ValidateEvent(ev)()
                cls.__repo_events.adauga(ev)
                print("Eveniment adăugat cu succes!")
                break
            except ValueError as err:
                print()
                print(err)
                print("Eveniment invalid, mai încercați o dată.")
                print()


    @classmethod
    def mod_person(cls):
        while True:
            print("Daca nu cunoasteti id-ul, apasati 'enter', apoi se vor afisa toate persoanele cu id-urile lor")
            id = input("ID-ul persoanei: ")
            if id == "": UI.print_people()
            else: break
        print("Daca doriti sa modificati un parametru tastati noua sa valoare, altfel, tastati 'enter'")
        while True:
            try:
                ini_p = cls.__repo_people.cauta_by_id(int(id))
                nume = input("numele persoanei: ")
                if nume == "": nume = ini_p.get_nume()
                oras = input("orasul de domiciliu: ")
                if oras == "": oras = ini_p.get_adress()["oras"]
                strada = input("strada: ")
                if strada == "": strada = ini_p.get_adress()["strada"]
                numar = input("numarul: ")
                if numar == "": numar = ini_p.get_adress()["numar"]
                p = Person(int(id), nume, oras, strada, int(numar))
                ValidatePerson(p)()
                cls.__repo_people.update(p)
                print("Persoana modificata cu succes!")
                break
            except ValueError as err:
                print()
                print(err)
                print("Persoana invalida, mai incercati o data.")
                id = input("ID-ul noii persoane: ")
                if id == "": UI.print_people()
                print()


    @classmethod
    def mod_event(cls):
        while True:
            print("Daca nu cunoasteti id-ul, apasati 'enter', apoi se vor afisa toate evenimentele cu id-urile lor")
            id = input("ID-ul evenimentului: ")
            if id == "": UI.print_events()
            else: break
        print("Daca doriti sa modificati un parametru tastati noua sa valoare, altfel, tastati 'enter'")
        while True:
            try:
                ini_ev = cls.__repo_events.cauta_by_id(int(id))
                print("Data desfășurării: ")
                z = input("    ziua: ")
                if z == "": z = ini_ev.get_data()["zi"]
                l = input("    luna: ")
                if l == "": l = ini_ev.get_data()["luna"]
                a = input("    anul: ")
                if a == "": a = ini_ev.get_data()["an"]
                print("Durata evenimentului: ")
                h = input("    ore: ")
                if h == "": h = ini_ev.get_timp()["ore"]
                m = input("    minute: ")
                if m == "": m = ini_ev.get_timp()["min"]
                desc = input("Descrierea evenimentului: ")
                if desc == "": desc = ini_ev.get_desc()
                ev = Event(int(id), int(z), int(l), int(a), int(h), int(m), desc)
                ValidateEvent(ev)()
                cls.__repo_events.update(ev)
                print("Eveniment modificat cu succes!")
                break
            except ValueError as err:
                print()
                print(err)
                print("Eveniment invalid, mai incercati o data.")
                id = input("ID-ul noului eveniment: ")
                if id == "": UI.print_events()
                print()


    @classmethod
    def del_person(cls):
        while True:
            print("Daca nu cunoasteti id-ul, apasati 'enter', apoi se vor afisa toate persoanele cu id-urile lor")
            id = input("ID-ul persoanei: ")
            if id == "": UI.print_people()
            else: break
        while True:
            try:
                cls.__repo_people.sterge_by_id(int(id))
                print("Persoana stearsa cu succes")
                return
            except ValueError as err:
                print()
                print(err)
                print("ID invalid, mai incercati o data.")
                id = input("ID-ul noii persoane: ")
                if id == "": UI.print_people()
                print()


    @classmethod
    def del_event(cls):
        while True:
            print("Daca nu cunoasteti id-ul, apasati 'enter', apoi se vor afisa toate evenimentele cu id-urile lor")
            id = input("ID-ul evenimentului: ")
            if id == "": UI.print_events()
            else: break
        while True:
            try:
                cls.__repo_events.sterge_by_id(int(id))
                print("Eveniment sters cu succes")
                return
            except ValueError as err:
                print()
                print(err)
                print("ID invalid, mai incercati o data.")
                id = input("ID-ul noului eveniment: ")
                if id == "": UI.print_events()
                print()


    @classmethod
    def find_person(cls):
        while True:
            print("Daca nu cunoasteti id-ul, apasati 'enter', apoi se vor afisa toate persoanele cu id-urile lor")
            id = input("ID-ul persoanei: ")
            if id == "": UI.print_people()
            else: break
        while True:
            try:
                print(str(cls.__repo_people.cauta_by_id(int(id))))
                return
            except ValueError as err:
                print()
                if str(err) == "REPO ERROR in cauta_by_id! ID not found!":
                    print("Persoana nu s-a gasit")
                    break
                else:
                    print("ID invalid, mai incercati o data.")
                    id = input("ID-ul noii persoane: ")
                if id == "": UI.print_people()
                else: print()


    @classmethod
    def find_event(cls):
        while True:
            print("Daca nu cunoasteti id-ul, apasati 'enter', apoi se vor afisa toate evenimentele cu id-urile lor")
            id = input("ID-ul evenimentului: ")
            if id == "": UI.print_events()
            else: break
        while True:
            try:
                print(str(cls.__repo_events.cauta_by_id(int(id))))
                return
            except ValueError as err:
                print()
                if str(err) == "REPO ERROR in cauta_by_id! ID not found!":
                    print("Evenimentul nu s-a gasit")
                    break
                else:
                    print("ID invalid, mai incercati o data.")
                    id = input("ID-ul noului eveniment: ")
                if id == "": UI.print_people()
                else: print()


    @classmethod
    def add_inscriere(cls):
        print("Daca nu cunoasteti id-ul persoanei sau evenimentului, apasati 'enter', apoi se vor afisa toate evenimentele sau persoanele cu id-urile lor")
        while True:
            id_ev = input("ID-ul evenimentului: ")
            if id_ev == "": UI.print_events()
            else: break
        while True:
            id_p = input("ID-ul persoanei: ")
            if id_p == "": UI.print_people()
            else: break
        while True:
            try:
                id_ev = int(id_ev)
                id_p = int(id_p)
                if not id_ev in cls.__inscrieri.get_self(): raise ValueError("eveniment negasit!")
                try:
                    if cls.__repo_people.cauta_by_id(id_p): pass
                except ValueError:
                    raise ValueError("persoana negasita!")
                cls.__inscrieri.add_participant(id_ev, id_p)
                print("Inscriere adaugata cu succes!")
                return
            except ValueError as err:
                print()
                if str(err) == "eveniment negasit!":
                    print("id-ul evenimentului negasit!")
                    break
                elif str(err) == "persoana negasita!":
                    print("id-ul persoanei negasit!")
                    break
                else:
                    print("ID-uri invalide!")
                    id_ev = input("ID-ul evenimentului: ")
                    if id_ev == "": UI.print_events()
                    id_p = input("ID-ul persoanei: ")
                    if id_p == "": UI.print_people()


    @classmethod
    def rap1(cls):
        print("Daca nu cunoasteti id-ul, apasati 'enter', apoi se vor afisa toate persoanele cu id-urile lor")
        while True:
            id_p = input("ID-ul persoanei: ")
            if id_p == "": UI.print_people()
            else: break
        while True:
            try:
                id_p = int(id_p)
                p = cls.__repo_people.cauta_by_id(id_p)
                l = cls.__service.rap1(p)
                if l == []:
                    print("Persoana nu este inscrisa la niciun eveniment!")
                for ev in l:
                    print(str(ev))
                return
            except ValueError as err:
                print()
                if str(err) == "REPO ERROR in cauta_by_id! ID not found!":
                    print("Persoana nu s-a gasit")
                    break
                else:
                    print("ID invalid, mai incercati o data.")
                    id_p = input("ID-ul noii persoane: ")
                if id_p == "": UI.print_people()
                else: print()


    @classmethod
    def rap2(cls):
        l = cls.__service.rap2()
        if l == []:
            print("Nicio persoana nu este inscrisa la niciun eveniment!")
        for pers in l:
            print(str(pers))
        return

    @classmethod
    def rap3(cls):
        l = cls.__service.rap3()
        if l == []:
            print("niciun eveniment nu are niciun participant")
        for ev in l:
            print(ev["descriere"] + ": " + str(ev["participanti"]) + " participanti")

    @classmethod
    def rap4(cls):
        print("Nr maxim de evenimente care au acelasi numar de persoane inscrise: ", cls.__service.rap4())


    @classmethod
    def rap_lab12(cls):
        l = cls.__service.rap_laborator12()
        print("Listă de evenimente sortată descrescător după durata de timp și crescător după descriere: ")
        for i in l:
            print(str(i))


    @classmethod
    def show_inscrieri(cls):
        print(cls.__service.stringify_TabelaInscrieri())


    @classmethod
    def show_ins_simplified(cls):
        print(cls.__service.stringify_TabelaInscrieri_simplified())


    @classmethod
    def print_events(cls):
        print(cls.__service.stringify_repo_events())

    @classmethod
    def print_people(cls):
        print(cls.__service.stringify_repo_people())


    @classmethod
    def run(cls):
        print("Pentru a vedea toate comenzile disponibile, tastati: help")
        commands = {
            "show_something": cls.com0,
            "help": cls.help,
            ": help": cls.help,
            " help": cls.help,
            "show_commands": cls.help,
            "add_person": cls.add_person,
            "generate_people": cls.generate_people,
            "add_event": cls.add_event,
            "show_people": cls.print_people,
            "show_events": cls.print_events,
            "mod_person": cls.mod_person,
            "mod_event": cls.mod_event,
            "del_person": cls.del_person,
            "del_event": cls.del_event,
            "find_person": cls.find_person,
            "find_event": cls.find_event,
            "add_inscriere": cls.add_inscriere,
            "rap1": cls.rap1,
            "rap2": cls.rap2,
            "rap3": cls.rap3,
            "rap4": cls.rap4,
            "rap_lab12": cls.rap_lab12,
            "show_inscrieri": cls.show_inscrieri,
            "show_ins_simplified": cls.show_ins_simplified
        }
        cls.__repo_people.adauga(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20))
        cls.__repo_people.adauga(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9))
        cls.__repo_people.adauga(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22))
        cls.__repo_people.adauga(Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50))
        cls.__repo_people.adauga(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2))
        cls.__repo_events.adauga(Event(4014, 22, 9, 2027, 13, 00, "Gabi vs Kurt Cobain"))
        cls.__repo_events.adauga(Event(5015, 22, 9, 2001, 2, 55, "Seara de Filme Hermes"))
        cls.__repo_events.adauga(Event(6016, 29, 2, 2024, 2, 10, "Vizita la Malul Marii"))
        cls.__repo_events.adauga(Event(7017, 22, 9, 2027, 3, 45, "Parada Tractoarelor din Municipiul Carei"))
        cls.__repo_events.adauga(Event(8018, 22, 9, 2001, 13, 00, "Concursul Ursului"))
        cls.__repo_events.adauga(Event(9019, 29, 2, 2024, 2, 10, "Vanatoarea de Dinozauri Cluj"))
        cls.__repo_events.adauga(Event(108810, 24, 11, 2027, 0, 0, "Ziua in care vin la timp"))
        cls.__repo_events.adauga(Event(128812, 29, 2, 2024, 2, 10, "Campionatul de prins ganduri necinstite"))
        cls.__inscrieri.add_participant(4014, 123)
        cls.__inscrieri.add_participant(4014, 463)
        cls.__inscrieri.add_participant(4014, 6351)
        cls.__inscrieri.add_participant(4014, 46351)
        cls.__inscrieri.add_participant(7017, 123)
        cls.__inscrieri.add_participant(7017, 463)
        cls.__inscrieri.add_participant(7017, 6351)
        cls.__inscrieri.add_participant(7017, 46351)
        cls.__inscrieri.add_participant(9019, 123)
        cls.__inscrieri.add_participant(9019, 463)
        cls.__inscrieri.add_participant(9019, 6351)
        cls.__inscrieri.add_participant(9019, 46351)
        while True:
            command = str(input())
            command = command.strip()
            if command == "exit":
                break
            elif command in commands:
                commands[command]()
            else:
                print("invalid command!")
        print("Program Terminat!")