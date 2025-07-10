import random
from room import Room

class Dungeon:
    def __init__(self, num_rooms=10):
        """Initialize the dungeon with a set number of randomly generated rooms."""
        self.rooms = [self.generate_room(i) for i in range(num_rooms)]
        self.current_room_index = 0
    
    def generate_room(self, room_id):
        """Generate a random room with possible enemies, items, or events."""
        return Room(room_id)
    
    def __iter__(self):
        """Make Dungeon iterable to allow sequential exploration."""
        return iter(self.rooms)
    
    def is_exit(self, room):
        """Check if the given room is the last room (dungeon exit)."""
        return self.rooms.index(room) == len(self.rooms) - 1
