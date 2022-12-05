import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_song_1 = Song("Beautiful Day", "U2", 4.05)

    def test_song_has_name(self):
        self.assertEqual("Beautiful Day", self.instance_of_song_1.name)

    
