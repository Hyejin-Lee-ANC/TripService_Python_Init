
class User:

    def __init__(self):
        self.trips = []
        self.friend = []

    def get_friends(self):
        return self.friend

    def add_friend(self, user):
        self.friend.append(user)

    def add_trip(self, trip):
        self.trips.append(trip)

    def trips(self):
        return self.trips
