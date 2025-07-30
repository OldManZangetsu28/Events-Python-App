from controller.ui import *

class Tests():
    """
    Clasa cu o singura metoda, care ruleaza toate testele entităților utilizate (domain, repo, service etc.)
    """
    @staticmethod
    def run():
        """
        Ruleaza testele tuturor entitatilor
        :return: void
        """
        pers = Person()
        event = Event()
        pers.test()
        event.test()

        vp = ValidatePerson(pers)
        ve = ValidateEvent(event)
        vp.test()
        ve.test()

        repo_p = RepoPerson()
        repo_e = RepoEvent()
        repo_p.test()
        repo_e.test()

        TI = TabelaInscrieri()
        TI.test()

        S = Service()
        S.test()
