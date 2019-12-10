# As a user I can create a flight with no specific information
# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin
# As a user I can add a Passanger to the list of passangers
# Passanger list is a list of objct that are Passanger
class Flight_trip():
    def __init__(self,plane = None,destination = None,origin = None,passenger = None,passenger_list = 0):
        self.plane = plane
        self.destination = destination
        self.origin = origin
        self.passenger = passenger
        self.passenger_list = []
    def add_plane(self,plane):
        self.plane = plane
        return plane
    def add_destination(self,destination):
        self.destination = destination
        return destination
    def add_origin(self,origin):
        self.origin = origin
        return origin
    def add_passenger_list(self,passenger):
        self.passenger = passenger
        self.passenger_list.append(passenger)
        return passenger, self.passenger_list
    def return_list(self):
        return  self.passenger_list

