import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.instance_of_guest = Guest("Steve", 59)

    def test_guest_has_name(self):
        self.assertEqual("Steve", self.instance_of_guest.name)
