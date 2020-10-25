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