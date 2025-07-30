from tests.tests import *

class App():
    """
    Clasa ce modeleaza ideea de aplicatie python. Contine metoda run(), ce porneste aplicatia
    """
    @staticmethod
    def run():
        all_tests = Tests()
        all_tests.run()
        print("All tests passed!")
        ui = UI()
        ui.run()