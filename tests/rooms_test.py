import unittest
from classes.rooms import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("POP-pin Bottles", "Pop", 8)
        self.room2 = Room("Screamo If You Want More", "Metal", 8)
        self.room3 = Room("Timewarp", "Golden Oldies", 8)
        self.room4 = Room("Get Lowww", "Rap", 8)
        self.room1.song_list = ["Angels", "C'est La Vie"]
        self.room2.song_list = ["Holy Diver", "Run To The Hills"]
        self.room3.song_list = ["Dreams", "Hotel California"]
        self.room4.song_list = ["Till The End", "No Role Modelz"]

    def test_rooms_have_names(self):
        self.assertEqual("Timewarp", self.room3.name)

    def test_rooms_have_genres(self):
        self.assertEqual("Pop", self.room1.genre)

    def test_rooms_have_capacities(self):
        self.assertEqual(8, self.room2.capacity)

    def test_room_has_song_list(self):
        self.assertEqual(["Dreams", "Hotel California"], self.room3.song_list)

    def test_add_guest_to_room(self):
        