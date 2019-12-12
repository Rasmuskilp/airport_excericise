from flight_trip import *
from passenger import *
from plane import *
while True:
    count = 0
    print('1 - if you wish to add passenger details')
    print('2 - if you wish to add plane details')
    print('3 - if you wish to add flight_trip details')
    details = input('enter the correct number:')
    if '1' in details:
        pass_name = input('add passenger details:')
        passport_details = input('add passport number:')
        new_name = Passenger(pass_name,passport_details)
    elif '2' in details:
        plane_num = input('add plane number:')
        plane_num = Plane(plane_num)
    elif '3' in details:
        planes_num = input('add plane number')
        dest_det = input('add destination')
        origin_det = input('add origin')
        passeng_num = input('add passenger')
        origin_det = Flight_trip(planes_num,dest_det,origin_det,passeng_num,[])
        origin_det.passenger_list.append(passeng_num)
        count += 1
    else:
        print('you did not input a correct number!')
        exit()