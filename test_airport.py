#here are the tests8
from passenger import *
from plane import *
from flight_trip import *
import pytest
def test_create_passenger_test():
    assert Passenger('Birt Kuman','B13927').name == 'Birt Kuman'
    assert Passenger('Birt Kuman','B13927').passport == 'B13927'
    assert Passenger('Joana Thomson','B343123').name =='Joana Thomson'
    assert Passenger('Joana Thomson','B343123').passport == 'B343123'
    with pytest.raises(TypeError):
        Passenger()
def test_plane_test():
    assert Plane('a1515252').flight_number == 'a1515252'

# def flight_trip_test():
#     assert Flight_trip
def test_flight():
    te_flight = Flight_trip()
    assert te_flight.plane == None
    assert te_flight.passenger == None
    assert te_flight.origin == None
    assert te_flight.destination == None
    # create an objct
    new_test = Flight_trip('a1521','Majorca','London','Charlie')
    # then call the method
    #
    assert new_test.add_plane('a15215') == 'a15215'
    assert  new_test.add_destination('Palma',) == 'Palma'
    assert  new_test.add_origin('Paris') == 'Paris'
    assert 'Bob' in new_test.add_passenger_list('Bob')



