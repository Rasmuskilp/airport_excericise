# Passengers
# as a user I can create a Passanger
# It can be created with name and passport number
# I can create 'Joana Thomson' with the Passport number 'B343123'
# I can create 'Birt Kuman' with the Passport number 'B13927'
# If I try to create a user with out a name or a passport number I get an error
# Plane
class Passenger():
    def __init__(self,name,passport):
        self.name = name
        self.passport = passport
   # def create_passenger(self,name,passport):
