import unittest
from classes.guests import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Stuart", 25, "Golden Oldies")
        self.guest2 = Guest("Rhian", 25, "Pop")
        self.guest3 = Guest("Michael", 24, "Pop")
        self.guest4 = Guest("Emma", 25, "Pop")
        self.guest5 = Guest("Liam", 25, "Rap")
        self.guest6 = Guest("Caragh", 26, "Metal")
        self.guest7 = Guest("Andrew", 25, "Metal")
        self.guest8 = Guest("Mirza", 25, "Rap")
        self.guest9 = Guest("Lisa", 26, "Golden Oldies")
        self.guest10 = Guest("Alexa Bliss", 29, "Metal")

    def test_guest_has_name(self):
        self.assertEqual("Stuart", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(26, self.guest9.age)

    def test_guest_has_a_preferred_genre(self):
        self.assertEqual("Rap", self.guest5.preferred_genre)
