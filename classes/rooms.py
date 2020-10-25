class Room:
    def __init__(self, name, genre, capacity):
        self.name = name
        self.genre = genre
        self.capacity = capacity
        self.song_list = []
        self.guest_list = []

    def check_song_list(self, song_list):
        room_songs = []
        for song in song_list:
            room_songs.append(song)
        return room_songs

    def add_guest_to_room(self, guest):
        self.guest_list.append(guest)

    def if_room_full_KB(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
        else:
            print("Sorry! This room is full!")

    def guest_leaves_room(self, guest):
        self.guest_list.remove(guest)