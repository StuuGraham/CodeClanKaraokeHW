import unittest
from classes.rooms import Room
from classes.songs import Song
from classes.guests import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("POP-pin Bottles", "Pop", 6, 15)
        self.room2 = Room("Screamo If You Want More", "Metal", 4, 10)
        self.room3 = Room("Timewarp", "Golden Oldies", 8, 20)
        self.room4 = Room("Get Lowww", "Rap", 4, 10)

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

        self.song1 = Song("Angels", "Robbie Williams", "Pop")
        self.song2 = Song("C'est La Vie", "Bewitched", "Pop")
        self.song3 = Song("Holy Diver", "Dio", "Metal")
        self.song4 = Song("Run To The Hills", "Iron Maiden", "Metal")
        self.song5 = Song("Dreams", "Fleetwood Mac", "Golden Oldies")
        self.song6 = Song("Hotel California", "Eagles", "Golden Oldies")
        self.song7 = Song("Till The End", "Logic", "Rap")
        self.song8 = Song("No Role Modelz", "J. Cole", "Rap")

        # guests = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5, 
                # self.guest6, self.guest7, self.guest8, self.guest9, self.guest10]
        
    def test_rooms_have_names(self):
        self.assertEqual("Timewarp", self.room3.name)

    def test_rooms_have_genres(self):
        self.assertEqual("Pop", self.room1.genre)

    def test_rooms_have_capacities(self):
        self.assertEqual(4, self.room2.capacity)

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room1.guest_list))

    def test_if_room_full_KB(self):
        self.room2.guest_list = [self.guest1, self.guest2, self.guest3, self.guest4]
        self.room2.if_room_full_KB(self.guest5)
        self.assertEqual(4, len(self.room2.guest_list))

    def test_guest_leaves_room(self):
        self.room1.guest_list = [self.guest1, self.guest2, self.guest3, self.guest4]
        self.room1.guest_leaves_room(self.guest1)
        self.assertEqual(3, len(self.room1.guest_list))

    def test_add_song_to_room(self):
        self.room3.add_song_to_room(self.song5)
        self.assertEqual(1, len(self.room3.song_list))

    def test_room_has_entry_fee(self):
        self.assertEqual(15, self.room1.entry_fee)

    def test_guest_can_afford_room__true(self):
        self.room1.guest_can_afford_room(self.guest1)
        self.assertEqual("Come on in!", self.room1.guest_can_afford_room(self.guest1))