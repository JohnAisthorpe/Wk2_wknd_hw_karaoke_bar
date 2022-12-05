class Room:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []

    def song_count(self):
        return len(self.songs)

    def guest_count(self):
        return len(self.guests)

    def add_song(self, song):
        self.songs.append(song)
    
    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)