import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_song_1 = Song("Beautiful Day", "U2", 4.05)
        self.instance_of_song_2 = Song("Supermassive Black Hole", "Muse", 3.35)
        self.instance_of_room = Room("Skye", 12)
        self.instance_of_guest = Guest("John", 26)

    def test_add_song(self):
        self.instance_of_room.add_song(self.instance_of_song_1)
        self.instance_of_room.add_song(self.instance_of_song_2)
        self.assertEqual(2, self.instance_of_room.song_count())

    def test_check_in_guest(self):
        self.instance_of_room.check_in_guest(self.instance_of_guest)
        self.assertEqual(1, self.instance_of_room.guest_count())
        
    def test_check_out_guest(self):
        self.instance_of_room.check_in_guest(self.instance_of_guest)
        self.instance_of_room.check_out_guest(self.instance_of_guest)
        self.assertEqual(0, self.instance_of_room.guest_count())

    
        
    

