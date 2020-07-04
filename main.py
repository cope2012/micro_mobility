from micro_mobility import Bicycle
from micro_mobility import Scooter
from micro_mobility import ElectricBicycle
import json


file = open('db.json', 'r')
raw_data = file.read()
file.close()
vehicles_data = json.loads(raw_data)
scooters_from_db = filter(lambda x: x['type'] == 'scooter', vehicles_data['vehicles'])
bikes_from_db = filter(lambda x: x['type'] == 'bicycle', vehicles_data['vehicles'])
scooters_list = []
bicycles_list = []

for scooter_item in scooters_from_db:
    scooters_list.append(Scooter.from_db(**scooter_item))

for bicycle_item in bikes_from_db:
    bicycles_list.append(Bicycle.from_db(**bicycle_item))

# s1 = scooters_list[0]
# print(s1)
# print(s1.battery)
# b1 = bicycles_list[0]
# print(b1)
# print(s1)
# print(s1.battery)
# s1.unlock()
# s1.begin_ride()
# s1.end_ride()
# print(s1.status)
