class Room:
    def __init__(self, name, genre, capacity):
        self.name = name
        self.genre = genre
        self.capacity = capacity
        self.song_list = []
        self.guest_list = []