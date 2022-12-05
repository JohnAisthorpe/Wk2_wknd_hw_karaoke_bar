import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.bar import Bar

class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_bar = Bar("Codeclan Karaoke")
        self.instance_of_room = Room("Skye", 12)

    def test_bar_has_name(self):
        self.assertEqual("Codeclan Karaoke", self.instance_of_bar.name)

    def test_create_rooms(self):
        self.instance_of_bar.create_room(self.instance_of_room)
        self.assertEqual(1, self.instance_of_bar.room_count())