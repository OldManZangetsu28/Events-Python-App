from controller.ui import *
from repository.list.repo import Repo
import unittest


class TestDomain(unittest.TestCase):
    def setUp(self):
        self.event1 = Event(1245, 12, 5, 2025, 3, 30, "Zilele Zalăului")
        self.event2 = Event(54262, 12, 5, 2025, 3, 30, "Zilele Zalăului")
        self.empty_event = Event()
        self.pers = Person(5001, "Popa Grigore", "Cluj", "Plopilor", 11)
        self.pers2 = Person(132, "Popa Grigore", "Cluj", "Plopilor", 11)
        self.empty_pers = Person()
        
    def test_event(self):
        self.assertIsNone(self.empty_event.get_id())
        self.assertIsNone(self.empty_event.get_desc())
        self.assertIsNone(self.empty_event.get_data())
        self.assertIsNone(self.empty_event.get_timp())
        self.assertEqual(self.event1.get_id(), 1245)
        self.assertEqual(self.event1.get_data(), {"zi": 12, "luna": 5, "an": 2025})
        self.assertEqual(self.event1.get_timp(), {"ore": 3, "min": 30})
        self.assertEqual(self.event1.get_desc(), "Zilele Zalăului")
        self.assertEqual(self.event1, self.event2)
        self.event2.set_data(1, 10, 2005)
        self.assertEqual(self.event2.get_data()["zi"], 1)
        self.assertEqual(self.event2.get_data()["luna"], 10)
        self.assertEqual(self.event2.get_data()["an"], 2005)
        self.event2.set_timp(4, 20)
        self.assertEqual(self.event2.get_timp()["ore"], 4)
        self.assertEqual(self.event2.get_timp()["min"], 20)
        self.event2.set_desc("Deschiderea Universității Zalău")
        self.assertEqual(self.event2.get_desc(), "Deschiderea Universității Zalău")
        self.assertNotEqual(self.event2, self.event1)
        self.assertEqual(str(self.event1), "Evenimentul 1245 din 12.5.2025, 3 ore 30 min, Zilele Zalăului")
        self.assertEqual(str(self.event2), "Evenimentul 54262 din 1.10.2005, 4 ore 20 min, Deschiderea Universității Zalău")
                
    def test_person(self):
        self.assertEqual(self.pers.get_id(), 5001)
        self.assertEqual(self.pers.get_nume(), "Popa Grigore")
        self.assertEqual(self.pers.get_adress()["oras"], "Cluj")
        self.assertEqual(self.pers.get_adress()["strada"], "Plopilor")
        self.assertEqual(self.pers.get_adress()["numar"], 11)
        self.assertIsNone(self.empty_pers.get_id())
        self.assertIsNone(self.empty_pers.get_nume())
        self.assertIsNone(self.empty_pers.get_adress())
        self.assertEqual(self.pers.get_nume(), self.pers2.get_nume())
        self.assertEqual(self.pers.get_adress(), self.pers2.get_adress())
        self.assertEqual(self.pers, self.pers2)
        self.empty_pers.set_nume("Gicu Ticu")
        self.assertEqual(self.empty_pers.get_nume(), "Gicu Ticu")
        self.empty_pers.set_adress("Turda", "Ploii", 22)
        self.assertEqual(self.empty_pers.get_adress()["oras"], "Turda")
        self.assertEqual(self.empty_pers.get_adress()["strada"], "Ploii")
        self.assertEqual(self.empty_pers.get_adress()["numar"], 22)
        self.assertNotEqual(self.empty_pers, self.pers)
        self.assertEqual(str(self.pers), "Persoana 5001, Popa Grigore, Cluj, str.Plopilor, nr.11")


class TestValidatorEvent(unittest.TestCase):
    def setUp(self):
        self.v_e0 = Event(201, 31, 12, 2001, 500, 0, "Fodder")
        self.v_e1 = Event(201, 29, 2, 2000, 0, 59, "Fodder Todder")
        self.inv_e2 = Event(-201, 29, 2, 2001, 500, 60, "Fod.der")
        self.validate_v_e0 = ValidateEvent(self.v_e0)
        self.validate_v_e1 = ValidateEvent(self.v_e1)
        self.validate_inv_e2 = ValidateEvent(self.inv_e2)

    def test_validate_event(self):
        self.validate_v_e0()
        self.validate_v_e1()
        self.assertRaisesRegex(ValueError, "Expected Event instance not found!", ValidateEvent, "Tractor")
        self.assertRaisesRegex(ValueError, "INVALID EVENT INSTANCE! Params: 'id', 'data', 'timpul', 'descriprion' NOT VALID!", self.validate_inv_e2)


class TestValidatorPerson(unittest.TestCase):
    def setUp(self):
        self.p0 = Person(124, "Gigi Costel", "Baia Medie", "Giurgiului", 20)
        self.p1 = Person(0, "Gigi Costel", "Baia Medie", "Giurgiului", 20)
        self.p2 = Person(-124, "Gigi Costel", "Baia Medie", "Giurgiului", -20)
        self.p3 = Person(124, "Gigi 3Costel", "Baia Medi.e", "Giurg.iului", 20)
        self.p4 = Person([""], "Gigi Costel", "Baia    Medie", "Giurgi123ului", "5")
        self.p5 = Person(12.4, "Gigi Costel", "Baia Medie", "Giurgiului", 1.5)
        self.validate_p0 = ValidatePerson(self.p0)
        self.validate_p1 = ValidatePerson(self.p1)
        self.validate_p2 = ValidatePerson(self.p2)
        self.validate_p3 = ValidatePerson(self.p3)
        self.validate_p4 = ValidatePerson(self.p4)
        self.validate_p5 = ValidatePerson(self.p5)

    def test_validate_person(self):
        self.assertRaisesRegex(ValueError, "Expected Person instance not found!", ValidatePerson, "Tractoare")
        ValidatePerson(self.p0)()
        self.assertRaisesRegex(ValueError, "INVALID PERSON INSTANCE! Params: 'id' NOT VALID!", self.validate_p1)
        self.assertRaisesRegex(ValueError, "INVALID PERSON INSTANCE! Params: 'id', 'numar' NOT VALID!", self.validate_p2)
        self.assertRaisesRegex(ValueError, "INVALID PERSON INSTANCE! Params: 'name', 'oras', 'strada' NOT VALID!", self.validate_p3)
        self.assertRaisesRegex(ValueError, "INVALID PERSON INSTANCE! Params: 'id', 'strada', 'numar' NOT VALID!", self.validate_p4)
        self.assertRaisesRegex(ValueError, "INVALID PERSON INSTANCE! Params: 'id', 'numar' NOT VALID!", self.validate_p5)


class TestDictionaryRepo(unittest.TestCase):
    def setUp(self):
        self.ev1 = Event(123, 22, 10, 2004, 3, 30, "Facerea")
        self.ev2 = Event(1233, 22, 12, 2004, 1, 20, "Distrugerea")
        self.invalid_ev1 = Event(0, "Gicu Coste123a", 5, "Clujeana", -22)
        self.invalid_ev2 = Event(124001, 22, 1, 2004, 2, 0, "Existenta")
        self.repo_ev = RepoEvent()
        self.repo_p = RepoPerson()
        self.invalid_p0 = Person(0, "Gicu Coste123a", 5, "Clujeana", -22)
        self.p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        self.p2 = Person(300, "Gicu Costea", "Bordieni", "Clujeana", 22)
        self.p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)

    def test_repo_event(self):
        #test_adauga
        self.assertRaisesRegex(ValueError, "REPO ERROR in adauga! Event entity NOT VALID!", self.repo_ev.adauga, self.invalid_ev1)
        self.repo_ev.adauga(self.ev1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in adauga! Event entity NOT UNIQUELEY IDENTIFIED!", self.repo_ev.adauga, self.ev1)
        self.repo_ev.adauga(self.ev2)
        self.assertEqual(self.repo_ev.get_self()[self.ev1.get_id()], self.ev1)
        self.assertEqual(self.repo_ev.get_self()[self.ev2.get_id()], self.ev2)
        #test_cauta_by_id
        found_p = self.repo_ev.cauta_by_id(123)
        assert found_p == self.ev1
        #test_update
        self.assertRaisesRegex(ValueError, "REPO ERROR in update! Event entity NOT VALID!", self.repo_ev.update, self.invalid_ev1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in update! Event entity NOT FOUND!", self.repo_ev.update, self.invalid_ev2)
        update_p1 = Event(123, 1, 11, 2000, 2, 35, "Geneza")
        self.repo_ev.update(update_p1)
        new_pers = self.repo_ev.cauta_by_id(123)
        self.assertEqual(new_pers, update_p1)
        #test_sterge_by_id
        self.assertRaisesRegex(ValueError, "REPO ERROR in sterge_by_id! ID not found!", self.repo_ev.sterge_by_id, 9999)
        self.assertRaisesRegex(ValueError, "REPO ERROR in sterge_by_id! ID not found!", self.repo_ev.sterge_by_id, "Tractor")
        self.repo_ev.sterge_by_id(123)
        self.assertEqual(len(self.repo_ev.get_self()), 1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in sterge_by_id! ID not found!", self.repo_ev.sterge_by_id, 123)
        self.assertEqual(len(self.repo_ev.get_self()), 1)
        self.repo_ev.sterge_by_id(1233)
        self.assertEqual(len(self.repo_ev.get_self()), 0)

    def test_repo_person(self):
        #test_adauga
        self.assertRaisesRegex(ValueError, "REPO ERROR in adauga! Person entity NOT VALID!", self.repo_p.adauga, "Tractor")
        self.repo_p.adauga(self.p1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in adauga! Person entity NOT UNIQUELEY IDENTIFIED!", self.repo_p.adauga, self.p1)
        self.repo_p.adauga(self.p2)
        self.repo_p.adauga(self.p3)
        self.assertEqual(self.repo_p.get_self()[self.p1.get_id()], self.p1)
        self.assertEqual(self.repo_p.get_self()[self.p3.get_id()], self.p3)
        #test_cauta_by_id
        found_p = self.repo_p.cauta_by_id(123)
        self.assertEqual(found_p, self.p1)
        #test_update
        invalid_update_p1 = Person(0, "Gicu Coste123a", 5, "Clujeana", -22)
        invalid_update_p2 = Person(301, "Gigi Costica", "Burdujeni", "Clujului", 27)
        self.assertRaisesRegex(ValueError, "REPO ERROR in update! Person entity NOT VALID!", self.repo_p.update, invalid_update_p1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in update! Person entity NOT FOUND!", self.repo_p.update, invalid_update_p2)
        update_p1 = Person(300, "Gigi Costica", "Burdujeni", "Clujului", 27)
        self.repo_p.update(update_p1)
        new_pers = self.repo_p.cauta_by_id(300)
        self.assertTrue(new_pers, update_p1)
        #test_delete
        self.assertRaisesRegex(ValueError, "REPO ERROR in sterge_by_id! ID not found!", self.repo_p.sterge_by_id, 9999)
        self.assertRaisesRegex(ValueError, "REPO ERROR in sterge_by_id! ID not found!", self.repo_p.sterge_by_id, "Tractor")
        self.repo_p.sterge_by_id(123)
        self.assertEqual(len(self.repo_p.get_self()), 2)
        self.repo_p.sterge_by_id(12463)
        self.assertEqual(len(self.repo_p.get_self()), 1)
        self.repo_p.sterge_by_id(300)
        self.assertEqual(len(self.repo_p.get_self()), 0)


class TestListRepo(unittest.TestCase):
    def setUp(self):
        self.invalid_p0 = Person(0, "Gicu Coste123a", 5, "Clujeana", -22)
        self.p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        self.p2 = Person(300, "Gicu Costea", "Bordieni", "Clujeana", 22)
        self.p3 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        self.repo = Repo()

    def test_list_repo(self):
        #test_adauga
        self.assertRaisesRegex(ValueError, "REPO ERROR in adauga! Person entity NOT VALID!", self.repo.adauga, self.invalid_p0)
        self.repo.adauga(self.p1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in adauga! Person entity NOT UNIQUELEY IDENTIFIED!", self.repo.adauga, self.p1)
        self.repo.adauga(self.p2)
        self.repo.adauga(self.p3)
        self.assertEqual(len(self.repo.get()), 3)
        #test_cauta_by_id
        found_p = self.repo.cauta_by_id(123)
        self.assertEqual(found_p, self.p1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in cauta_by_id! ID not found!", self.repo.cauta_by_id, "Tractor")
        self.assertRaisesRegex(ValueError, "REPO ERROR in cauta_by_id! ID not found!", self.repo.cauta_by_id, 9999)
        #test_update
        invalid_update_p1 = Person(0, "Gicu Coste123a", 5, "Clujeana", -22)
        invalid_update_p2 = Person(301, "Gigi Costica", "Burdujeni", "Clujului", 27)
        self.assertRaisesRegex(ValueError, "REPO ERROR in update! Person entity NOT VALID!", self.repo.update, invalid_update_p1)
        self.assertRaisesRegex(ValueError, "REPO ERROR in update! Person entity NOT FOUND!", self.repo.update, invalid_update_p2)
        update_p1 = Person(300, "Gigi Costica", "Burdujeni", "Clujului", 27)
        self.repo.update(update_p1)
        new_pers = self.repo.cauta_by_id(300)
        self.assertEqual(new_pers, update_p1)
        #test_sterge_by_id
        self.repo.sterge_by_id(123)
        self.assertEqual(len(self.repo.get()), 2)
        self.repo.sterge_by_id(300)
        self.assertEqual(len(self.repo.get()),1)
        self.repo.sterge_by_id(12463)
        self.assertEqual(len(self.repo.get()),0)
        

class TestTabelaInscrieri(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_person_add_event(self):
        T = TabelaInscrieri()
        T.add_event(123)
        T.add_event(123)
        T.add_event(155)
        T.add_event(213)
        T.add_event(155)
        self.assertEqual(len(T), 3)
        T.add_participant(123, 501)
        T.add_participant(123, 513)
        T.add_participant(123, 501)
        T.add_participant(155, 555)
        T.add_participant(155, 555)
        T.add_participant(155, 555)
        self.assertEqual(len(T.get_participants(123)), 2)
        self.assertEqual(len(T.get_participants(155)), 1)

    def test_del_event(self):
        T = TabelaInscrieri()
        T.add_event(123)
        T.add_event(155)
        T.add_event(155)
        T.add_event(106)
        T.add_event(107)
        T.del_event(155)
        self.assertEqual(len(T), 3)
        T.del_event(100)
        self.assertEqual(len(T), 3)
        T.del_event(106)
        self.assertEqual(len(T), 2)
        T.del_event(123)
        T.del_event(107)
        self.assertEqual(len(T), 0)

    def test_del_participant_from_event(self):
        T = TabelaInscrieri()
        T.add_event(123)
        T.add_event(155)
        T.add_participant(107, 555)
        T.add_participant(123, 555)
        T.add_participant(123, 501)
        T.del_participant_from_event(107, 123124)
        T.del_participant_from_event(123, 52323)
        self.assertEqual(len(T.get_participants(123)),2)
        T.del_participant_from_event(123, 555)
        self.assertEqual(len(T.get_participants(123)), 1)
        T.del_participant_from_event(123,501)
        self.assertTrue(len(T.get_participants(123)) == len(T.get_participants(155)) == 0)


class TestService(unittest.TestCase):
    def setUp(self):
        self.inscrieri = TabelaInscrieri()
        self.r_people = RepoPerson(self.inscrieri)
        self.r_events = RepoEvent(self.inscrieri)
        self.service = Service(self.r_events, self.r_people, self.inscrieri)
        self.r_people.adauga(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20))
        self.r_people.adauga(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9))
        self.r_people.adauga(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22))
        self.r_people.adauga(Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50))
        self.r_people.adauga(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2))
        self.r_events.adauga(Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului"))
        self.r_events.adauga(Event(9213, 22, 9, 2001, 10, 55, "Batalia dintre Aizen si Istvan"))
        self.r_events.adauga(Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"))
        self.inscrieri.add_participant(9871, 123)
        self.inscrieri.add_participant(9871, 12463)
        self.inscrieri.add_participant(9871, 6351)
        self.inscrieri.add_participant(9213, 6351)
        self.inscrieri.add_participant(9871, 463)
        self.inscrieri.add_participant(5555, 463)
        self.inscrieri.add_participant(5555, 46351)
        self.inscrieri.add_participant(5555, 6351)

    def test_stringify(self):
        p1 = Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)
        p3 = Person(463, "Gilgamesh", "Uruk", "Gloriei", 22)
        p4 = Person(46351, "Enkidu", "Padurea de Carpini", "Livezii", 50)
        p5 = Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)
        ev1 = Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului")
        ev2 = Event(9213, 22, 9, 2001, 10, 55, "Batalia dintre Aizen si Istvan")
        ev3 = Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich")
        #test_stringify_repo_people
        self.assertTrue(self.service.stringify_repo_people_recursive(list(self.r_people.get_self().keys())) == self.service.stringify_repo_people() == str(
            p1) + "\n" + str(p2) + "\n" + str(p3) + "\n" + str(p4) + "\n" + str(p5) + "\n")
        #test_stringify_repo_events
        self.assertTrue(self.service.stringify_repo_events_recursive(list(self.r_events.get_self().keys())) == self.service.stringify_repo_events() == str(ev1) + "\n" + str(ev2) + "\n" + str(ev3) + "\n")
        #test_stringify_TabelaInscrieri
        pers1 = str(p1.get_id()) + " " + p1.get_nume()
        pers2 = str(p2.get_id()) + " " + p2.get_nume()
        pers3 = str(p3.get_id()) + " " + p3.get_nume()
        pers4 = str(p4.get_id()) + " " + p4.get_nume()
        pers5 = str(p5.get_id()) + " " + p5.get_nume()
        self.assertTrue(self.service.stringify_TabelaInscrieri_simplified() ==
                ev1.get_desc() + ": " + pers1 + ", " + pers2 + ", " + pers5 + ", " + pers3 + "\n" + ev2.get_desc() + ": " + pers5 + "\n" + ev3.get_desc() + ": " + pers3 + ", " + pers4 + ", " + pers5 + "\n")

    def test_rap1(self):
        ev = Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich")
        p1 = Person(123000, "Tudor BigHead", "Rareseni", "Ferdinand", 20)
        p2 = Person(120, "Tudor SmallHead", "Rareseni", "Ferdinand", 20)
        self.assertRaisesRegex(ValueError, "SERVICE ERROR! In rap1, Given entity not a valid instance of Person class!", self.service.rap1, ev)
        self.assertRaisesRegex(ValueError, "SERVICE ERROR! In rap1, Given Person instance not found in repository!", self.service.rap1, p1)
        self.assertRaisesRegex(ValueError, "SERVICE ERROR! In rap1, Given Person instance not found in repository!", self.service.rap1, p2)
        self.assertEqual (self.service.rap1(Person(123, "Tudor BigHead", "Rareseni", "Ferdinand", 20)),
                self.service.rap1(Person(12463, "Rares Von", "Tudoreni", "Costellino", 9)))
        self.assertEqual (self.service.rap1(Person(463, "Gilgamesh", "Uruk", "Gloriei", 22)),
                [Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"),
                 Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului")])
        self.assertEqual (self.service.rap1(Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)),
                [Event(9213, 22, 9, 2001, 10, 55, "Batalia dintre Aizen si Istvan"),
                 Event(5555, 29, 2, 2024, 2, 10, "Campionatul Comunal de Quiddich"),
                 Event(9871, 22, 9, 2027, 3, 45, "Zilele Zalaului")])

    def test_rap2(self):
        self.assertEqual(self.service.rap2(), [Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)])
        self.inscrieri.add_participant(9213, 463)
        self.assertTrue (self.service.rap2() == [Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2),
                            Person(463, "Gilgamesh", "Uruk", "Gloriei", 22)]
                                                            or
                self.service.rap2() == [Person(463, "Gilgamesh", "Uruk", "Gloriei", 22),
                             Person(6351, "Kurosaki Ichigo", "Karakura", "Tensho", 2)])
        self.inscrieri.del_participant_from_event(9213, 463)

    def test_rap_3_4(self):
        rap3 = self.service.rap3()
        ev1 = {"descriere": "Zilele Zalaului", "participanti": 4}
        ev2 = {"descriere": "Batalia cu Aizen si Istvan", "participanti": 4}
        ev3 = {"descriere": "Campionatul Comunal de Quiddich", "participanti": 4}
        self.assertTrue(ev1 in rap3 or ev2 in rap3 or ev3 in rap3)
        #print(self.inscrieri.get_self())
        self.assertEqual(self.service.rap4(),1)
        self.assertEqual(self.service.rap3(), [{"descriere": "Zilele Zalaului", "participanti": 4}])
        self.inscrieri.del_participant_from_event(9871, 463)
        self.assertEqual(self.service.rap4(), 2)
        self.r_events.adauga(Event(4014, 22, 9, 2027, 13, 00, "Gabi Mircea vs Kurt Cobain"))
        self.r_events.adauga(Event(5015, 22, 9, 2001, 2, 55, "Seara de Filme Hermes"))
        self.r_events.adauga(Event(6016, 29, 2, 2024, 2, 10, "Vizita la Malul Marii"))
        self.r_events.adauga(Event(7017, 22, 9, 2027, 3, 45, "Parada Tractoarelor din Municipiul Carei"))
        self.r_events.adauga(Event(8018, 22, 9, 2001, 10, 55, "Concursul Ursului"))
        self.r_events.adauga(Event(9019, 29, 2, 2024, 2, 10, "Vanatoarea de Dinozauri Cluj"))
        self.r_events.adauga(Event(108810, 24, 11, 2027, 0, 0, "Ziua in care Vancea termina la timp"))
        self.r_events.adauga(Event(118811, 22, 3, 2025, 0, 3, "Tudor si fata cu parul roz din blocul meu FAC DRAGOSTE"))
        self.r_events.adauga(Event(128812, 29, 2, 2024, 2, 10, "Campionatul de prins ganduri necurate"))
        self.assertEqual(self.service.rap4(), 9)
        self.inscrieri.add_participant(4014, 123)
        self.inscrieri.add_participant(4014, 12463)
        self.inscrieri.add_participant(4014, 6351)
        self.inscrieri.add_participant(4014, 46351)
        self.inscrieri.add_participant(7017, 6351)
        self.inscrieri.add_participant(7017, 463)
        self.inscrieri.add_participant(7017, 12463)
        self.inscrieri.add_participant(7017, 46351)
        self.inscrieri.add_participant(9871, 463)
        top_ev1 = {"descriere": "Gabi Mircea vs Kurt Cobain", "participanti": 4}
        top_ev2 = {"descriere": "Parada Tractoarelor din Municipiul Carei", "participanti": 4}
        top_ev3 = {'descriere': 'Zilele Zalaului', 'participanti': 4}
        l = self.service.rap3()
        self.assertTrue((top_ev1 in l and top_ev2 in l) or (top_ev1 in l and top_ev3 in l) or (top_ev2 in l and top_ev3 in l))


if __name__ == "__main__":
    unittest.main()
    