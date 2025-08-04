class Event():
    """
    Clasa ce modeleaza un eveniment
    eventID: identificatorul numeric unic al instantei
    data: data calendaristica valida la care a avut loc evenimentul. Este compusa din zi, luna, an
    timp: timpul cat dureaza evenimentul. Este compus din ore(h) si minute(min)
    descriere: descrierea evenimentului
    """

    def __init__(self, ID=None, zi=None, luna=None, an=None, h=None, min=None, desc=None):
        """
        Initializeaza instanta cu parametrii dati
        Antetul functiei utilizeaza argument inspection. Parametrii sunt optionali.
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
