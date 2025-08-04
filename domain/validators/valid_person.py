from domain.persoana import *

class ValidatePerson:
    """
    Clasa ce valideaza instantele clasei Person
    """
    def __init__(self, person):
        """
        Constructorul clasei ValidatePerson
        :param person: O instanta a clasei Person
        :raises: ValueError, daca person nu e o instanta a clasei Person
        """
        if not isinstance(person, Person):
            raise ValueError("Expected Person instance not found!")
        self.person = person


    def __call__(self):
        """
        Valideaza o instanta a clasei Person
        O instanta valida a clasei Person respecta urmatoarele conditii
            1) personID: 'int' strict pozitiv
            2) nume: 'string'
            3) adresa: {"oras": 'string', "strada": 'string', "numar": 'int'}
        :return: void
        :raises: ValueError, daca paramterii instantei person nu respecta conditiile specificate mai sus
        """
        errors = "INVALID PERSON INSTANCE! Params: "
        if str(type(self.person.get_id())) == "<class 'int'>":
            if self.person.get_id() <= 0:
                errors += "'id', "
        else:
            errors += "'id', "

        from re import search
        if str(type(self.person.get_nume())) == "<class 'str'>":
            x = search("[^ a-zA-Z]", self.person.get_nume())
            if x != None : errors += "'name', "
        else:
            errors += "'name', "

        if str(type(self.person.get_adress()["oras"])) == "<class 'str'>":
            x = search("[^ a-zA-Z]", self.person.get_adress()["oras"])
            if x != None: errors += "'oras', "
        else:
            errors += "'oras', "

        if str(type(self.person.get_adress()["strada"])) == "<class 'str'>":
            x = search("[^ a-zA-Z]", self.person.get_adress()["strada"])
            if x != None: errors += "'strada', "
        else:
            errors += "'strada', "

        if str(type(self.person.get_adress()["numar"])) == "<class 'int'>":
            if self.person.get_adress()["numar"] <= 0:
                errors += "'numar', "
        else:
            errors += "'numar', "

        if errors != "INVALID PERSON INSTANCE! Params: ":
            errors = errors[:-2]
            errors += " NOT VALID!"
            raise ValueError(errors)
