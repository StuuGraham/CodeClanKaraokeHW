import unittest
from classes.songs import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Angels", "Robbie Williams", "Pop")
        self.song2 = Song("C'est La Vie", "Bewitched", "Pop")
        self.song3 = Song("Holy Diver", "Dio", "Metal")
        self.song4 = Song("Run To The Hills", "Iron Maiden", "Metal")
        self.song5 = Song("Dreams", "Fleetwood Mac", "Golden Oldies")
        self.song6 = Song("Hotel California", "Eagles", "Golden Oldies")
        self.song7 = Song("Say My Name", "Destiny's Child", "RnB/Hip-Hop")
        self.song8 = Song("Still D.R.E.", "Dr Dre", "RnB/Hip-Hop")

    def test_song_has_a_name(self):
        self.assertEqual("Holy Diver", self.song3.name)

    def test_song_has_an_artist(self):
        self.assertEqual("Eagles", self.song6.artist)

    def test_song_has_a_genre(self):
        self.assertEqual("Pop", self.song1.genre)