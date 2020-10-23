import unittest
from classes.rooms import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("POPpin Bottles", "Pop", 8)
        self.room2 = Room("Scream If You Want More", "Metal", 8)
        self.room3 = Room("Timewarp", "Pre 2000", 8)
        self.room4 = Room("Get Lowww", "RnB/Hip-Hop", 8)

    def test_rooms_have_names(self):
        self.assertEqual("Timewarp", self.room3.name)