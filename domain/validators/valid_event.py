from domain.eveniment import *

class ValidateEvent():
    """
    Clasa ce valideaza instantele clasei Event
    """
    def __init__(self, event):
        """
        Constructorul clasei ValidateEvent
        :param event: O instanta a clasei Event
        :raises: ValueError, daca person nu e o instanta a clasei Event
        """
        if not isinstance(event, Event):
            raise ValueError("Expected Person instance not found!")
        self.event = event

    def __call__(self):
        """
        Valideaza o instanta a clasei Event()
        :return: void
        :raises: ValueError, daca paramterii instantei person nu respecta preconditiile din specificatia clasei Event()
        """
        errors = "INVALID EVENT INSTANCE! Params: "

        if str(type(self.event.get_id())) == "<class 'int'>":
            if self.event.get_id() <= 0:
                errors += "'id', "
        else:
            errors += "'id', "

        date = self.event.get_data()
        time = self.event.get_timp()
        invalid_date = False
        invalid_time = False

        if str(type(date["zi"])) == "<class 'int'>" and str(type(date["luna"])) == "<class 'int'>" and str(type(date["an"])) == "<class 'int'>":
            max_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if date["an"] % 4 == 0:
                max_day[1] = 29
            if not ((1000 <= date["an"] <= 9999) and (1 <= date["luna"] <= 12) and (1 <= date["zi"] <= max_day[date["luna"] - 1])):
                invalid_date = True
        else:
            invalid_date = True
        if invalid_date:
            errors += "'data', "

        if str(type(time["ore"])) == "<class 'int'>" and str(type(time["min"])) == "<class 'int'>":
            if not (0 <= time["min"] <= 59) or time["ore"] < 0:
                invalid_time = True
        else:
            invalid_time = True
        if invalid_time:
            errors += "'timpul', "

        from re import search
        if str(type(self.event.get_desc())) == "<class 'str'>":
            x = search("[^ a-zA-Z]", self.event.get_desc())
            if x != None: errors += "'descriprion', "
        else:
            errors += "'description', "

        if errors != "INVALID EVENT INSTANCE! Params: ":
            errors = errors[:-2]
            errors += " NOT VALID!"
            raise ValueError(errors)


    @staticmethod
    def test():
        v_e0 = Event(201, 31, 12, 2001, 500, 0, "Fodder")
        v_e1 = Event(201, 29, 2, 2000, 0, 59, "Fodder Todder")
        inv_e2 = Event(201, 3, 12, 2001, 500, 59, "Fodder")
        inv_e3 = Event(201, 3, 12, 2001, 500, 59, "Fodder")
        inv_e4 = Event(201, 3, 12, 2001, 500, 59, "Fodder")
        ValidateEvent(v_e0)()
        ValidateEvent(v_e1)()
