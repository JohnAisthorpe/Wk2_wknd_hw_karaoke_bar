class Bar:
    
    def __init__(self, name, ):
        self.name = name
        self.rooms = []

    def room_count(self):
        return len(self.rooms)

    def create_room(self, room):
        self.rooms.append(room)

    
        
