from tests.tests import *

class App():
    """
    Clasa ce modeleaza ideea de aplicatie python. Contine metoda run(), ce porneste aplicatia
    """
    @staticmethod
    def run():
        ui = UI()
        ui.run()