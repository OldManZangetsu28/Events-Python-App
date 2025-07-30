class Event():
    """
    ABSTRACT:
        Clasa ce modeleaza un eveniment
        eventID: identificatorul numeric unic al instantei
        data: data calendaristica valida la care a avut loc evenimentul
        timp: timpul cat dureaza evenimentul
        descriere: descrierea evenimentului
    DOMAIN:
        eventID: numar intreg ('int') strict pozitiv
        data: {"zi": z, "luna": l, "an": a}
              z,l,a 'int' strict pozitive
              1<=z<=31, 1<=l<=12, 1000<=a<=9999
        timp: {"ore": h, "min": m}
              h,m 'int' pozitive
              0<=min<=59
        descriere: string, ale carui caractere au urmatorul domeniu: [ a-zA-z]
    """

    def __init__(self, ID=None, zi=None, luna=None, an=None, h=None, min=None, desc=None):
        """
        initializeaza instanta cu parametrii dati
        Functia utilizeaza argument inspection. Parametrii pot lispi.
        Totusi, daca acestia exista, sunt modelati astfel:
        :param ID,zi,luna,an,h,min: numere intregi pozitive, care inseamna id-ul instantei, ziua, luna, anul la care evenimentul
                                    are loc, respectiv durata evenimentului exprimate in ore(h) si minute(m)
        :param desc: string, semnifica descrierea evenimentului
        """
        params = [ID, zi, luna, an, h, min, desc]
        if params == [None] * 7:
            for p in params:
                self.__eventID = None
                self.__data = None
                self.__timp = None
                self.__descriere = None
        else:
            self.__eventID = ID
            self.__data = {
                "zi": zi,
                "luna": luna,
                "an": an
            }
            self.__timp = {
                "ore": h,
                "min": min
            }
            self.__descriere = desc

    def get_id(self):
        """
        Getter-ul ID-ului
        """
        return self.__eventID

    def get_data(self):
        """
        Getter-ul datei
        """
        return self.__data

    def get_timp(self):
        """
        Getter-ul duratei de timp
        """
        return self.__timp

    def get_desc(self):
        """
        Getter-ul descrierii
        """
        return self.__descriere

    def set_data(self, zi, luna, an):
        """
        Setter al datei
        """
        self.__data = {"zi": zi, "luna": luna, "an": an}

    def set_timp(self, ore, min):
        """
        Setter al duratei de timp
        """
        self.__timp = {"ore": ore, "min": min}

    def set_desc(self, description):
        """
        Setter al descrierii
        """
        self.__descriere = description

    def __eq__(self, other):
        """
        Verifica daca self si other au toti parametrii egali, mai putin id-ul
        :return: True, daca self.__data == other.__data and self.__timp == other.__timp and self.__descriere == self.descriere
                 False, altfel
        """
        return self.__eventID == other.__eventID or (self.__data == other.__data and self.__timp == other.__timp and self.__descriere == self.__descriere)

    def __str__(self):
        """
        :return: string ce stilizeaza toti parametrii instantei clasei
        """
        data = str(self.__data["zi"]) + "." + str(self.__data["luna"]) + "." + str(self.__data["an"])
        durata = str(self.__timp["ore"]) + " ore " + str(self.__timp["min"]) + " min"
        return "Evenimentul " + str(self.__eventID) + " din " + data + ", " + durata + ", " + str(self.__descriere)

    @staticmethod
    def test():
        empty_event = Event()
        event1 = Event(1245, 12, 5, 2025, 3, 30, "Zilele Zalăului")
        assert empty_event.get_id() == None
        assert empty_event.get_desc() == None
        assert empty_event.get_data() == None
        assert empty_event.get_timp() == None
        assert event1.get_id() == 1245
        assert event1.get_data() == {"zi": 12, "luna": 5, "an": 2025}
        assert event1.get_timp() == {"ore": 3, "min": 30}
        assert event1.get_desc() == "Zilele Zalăului"
        event2 = Event(54262, 12, 5, 2025, 3, 30, "Zilele Zalăului")
        assert event1 == event2
        event2.set_data(1,10,2005)
        assert event2.get_data()["zi"] == 1
        assert event2.get_data()["luna"] == 10
        assert event2.get_data()["an"] == 2005
        event2.set_timp(4,20)
        assert event2.get_timp()["ore"] == 4
        assert event2.get_timp()["min"] == 20
        event2.set_desc("Deschiderea Universității Zalău")
        assert event2.get_desc() == "Deschiderea Universității Zalău"
        assert event2 != event1
        assert str(event1) == "Evenimentul 1245 din 12.5.2025, 3 ore 30 min, Zilele Zalăului"
        assert str(event2) == "Evenimentul 54262 din 1.10.2005, 4 ore 20 min, Deschiderea Universității Zalău"
