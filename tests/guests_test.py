import unittest
from classes.guests import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Stuart", 25, "Golden Oldies", 40)
        self.guest2 = Guest("Rhian", 25, "Pop", 40)
        self.guest3 = Guest("Michael", 24, "Pop", 60)
        self.guest4 = Guest("Emma", 25, "Pop", 30)
        self.guest5 = Guest("Liam", 25, "Rap", 50)
        self.guest6 = Guest("Caragh", 26, "Metal", 5)
        self.guest7 = Guest("Andrew", 25, "Metal", 40)
        self.guest8 = Guest("Mirza", 25, "Rap", 75)
        self.guest9 = Guest("Lisa", 26, "Golden Oldies", 50)
        self.guest10 = Guest("Alexa Bliss", 29, "Metal", 100)

        guests = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5,
                    self.guest6, self.guest7, self.guest8, self.guest9, self.guest10]

    def test_guest_has_name(self):
        self.assertEqual("Stuart", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(26, self.guest9.age)

    def test_guest_has_a_preferred_genre(self):
        self.assertEqual("Rap", self.guest5.preferred_genre)

    def test_guest_has_a_wallet(self):
        self.assertEqual(50, self.guest9.wallet)
