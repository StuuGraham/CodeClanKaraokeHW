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
