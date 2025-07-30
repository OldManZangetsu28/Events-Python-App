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
        Valideaza o instanta a clasei Person()
        :return: void
        :raises: ValueError, daca paramterii instantei person nu respecta preconditiile din specificatia clasei Person()
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


    @staticmethod
    def test():
        p0 = Person(124, "Gigi Costel", "Baia Medie", "Giurgiului", 20)
        p1 = Person(0, "Gigi Costel", "Baia Medie", "Giurgiului", 20)
        p2 = Person(-124, "Gigi Costel", "Baia Medie", "Giurgiului", -20)
        p3 = Person(124, "Gigi 3Costel", "Baia Medi.e", "Giurg.iului", 20)
        p4 = Person([""], "Gigi Costel", "Baia    Medie", "Giurgi123ului", "5")
        p5 = Person(12.4, "Gigi Costel", "Baia Medie", "Giurgiului", 1.5)
        try:
            ValidatePerson("Tractoare")()
            assert False
        except ValueError as err:
            assert str(err) == "Expected Person instance not found!"
        ValidatePerson(p0)()
        try:
            ValidatePerson(p1)()
            assert False
        except ValueError as err:
            assert str(err) == "INVALID PERSON INSTANCE! Params: 'id' NOT VALID!"
        try:
            ValidatePerson(p2)()
            assert False
        except ValueError as err:
            assert str(err) == "INVALID PERSON INSTANCE! Params: 'id', 'numar' NOT VALID!"
        try:
            ValidatePerson(p3)()
            assert False
        except ValueError as err:
            assert str(err) == "INVALID PERSON INSTANCE! Params: 'name', 'oras', 'strada' NOT VALID!"
        try:
            ValidatePerson(p4)()
            assert False
        except ValueError as err:
            assert str(err) == "INVALID PERSON INSTANCE! Params: 'id', 'strada', 'numar' NOT VALID!"
        try:
            ValidatePerson(p5)()
            assert False
        except ValueError as err:
            assert str(err) == "INVALID PERSON INSTANCE! Params: 'id', 'numar' NOT VALID!"
