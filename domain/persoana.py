class Person:
    """
    ABSTRACT:
        Clasa ce modeleaza o persoana, ca participant la un eveniment
        personID: identificatorul numeric unic al persoanei
        nume: numele persoanei
        adresa: adresa la care locuieste persoana
    DOMAIN:
        personID: 'int' strict pozitiv
        nume: 'string'
        adresa: {"oras": 'string', "strada": 'string', "numar": 'int'}
    """

    def __init__(self, ID=None, name=None, oras=None, strada=None, numar=None):
        """
        Initializeaza o instanta a clasei Person
        Utilizez argument inspection. Parametrii sunt optionali.
        Totusi, daca acestia exista, sunt modelati astfel:
        :param ID: nr intreg strict pozitiv
        :params name, oras: string-uri ale caror caractere au urmatorul domeniu [ a-zA-Z]
        :params strada: string, ale carui caractere au urmatorul domeniu: [ a-zA-z]
        :param numar: nr intreg strict pozitiv
        """
        params = [ID, name, oras, strada, numar]
        if params == [None] * 5:
            self.__personID = None
            self.__nume = None
            self.__adresa = None
        else:
            self.__personID = ID
            self.__nume = name
            self.__adresa = {
                "oras": oras,
                "strada": strada,
                "numar": numar
            }

    def get_id(self):
        """
        Getter al id-ului instantei
        :return: id-ul instantei
        """
        return self.__personID

    def get_nume(self):
        """
        Getter al numelui instantei
        :return: numele instantei
        """
        return self.__nume

    def get_adress(self):
        """
        Getter al adresei instantei
        :return: adresa instantei
        """
        return self.__adresa

    def set_nume(self, nume):
        """
        Setter al numelui instantei
        """
        self.__nume = nume

    def set_adress(self, oras, strada, numar):
        """
        Setter al adresei instantei
        """
        self.__adresa = {"oras": oras, "strada": strada, "numar": numar}

    def __eq__(self, other):
        """
        Verifica daca other si self au toti parametrii egali, mai putin id
        :return: True, daca self.__nume == other.__nume and self.__adresa == other.__adresa
                 False, altfel
        """
        return self.__personID == other.__personID or (self.__nume == other.__nume and self.__adresa == other.__adresa)

    def __str__(self):
        """
        :return: string ce stilizeaza toti parametrii instantei clasei
        """
        adresa = str(self.__adresa["oras"]) + ", str." + str(self.__adresa["strada"]) + ", nr." + str(self.__adresa["numar"])
        return "Persoana " + str(self.__personID) + ", " + self.__nume + ", " + adresa

    @staticmethod
    def test():
        pers = Person(5001, "Popa Grigore", "Cluj", "Plopilor", 11)
        assert pers.get_id() == 5001
        assert pers.get_nume() == "Popa Grigore"
        assert pers.get_adress()["oras"] == "Cluj"
        assert pers.get_adress()["strada"] == "Plopilor"
        assert pers.get_adress()["numar"] == 11
        empty_pers = Person()
        assert empty_pers.get_id() == None
        assert empty_pers.get_nume() == None
        assert empty_pers.get_adress() == None
        pers2 = Person(132,"Popa Grigore", "Cluj", "Plopilor", 11)
        assert pers.get_nume() == pers2.get_nume()
        assert pers.get_adress() == pers2.get_adress()
        assert pers == pers2
        empty_pers.set_nume("Gicu Ticu")
        assert empty_pers.get_nume() == "Gicu Ticu"
        empty_pers.set_adress("Turda", "Ploii", 22)
        assert empty_pers.get_adress()["oras"] == "Turda"
        assert empty_pers.get_adress()["strada"] == "Ploii"
        assert empty_pers.get_adress()["numar"] == 22
        assert empty_pers != pers
        assert str(pers) == "Persoana 5001, Popa Grigore, Cluj, str.Plopilor, nr.11"
