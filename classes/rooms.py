class Room:
    def __init__(self, name, genre, capacity, entry_fee):
        self.name = name
        self.genre = genre
        self.capacity = capacity
        self.song_list = []
        self.guest_list = []
        self.entry_fee = entry_fee

    def add_guest_to_room(self, guest):
        self.guest_list.append(guest)

    def if_room_full_KB(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
        else:
            print("Sorry! This room is full!")

    def guest_leaves_room(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_room(self, song):
        self.song_list.append(song)

    def guest_can_afford_room(self, guest):
        if self.entry_fee < guest.wallet:
            return "Come on in!"
        else:
            return "Sorry mate, you can't afford this"
