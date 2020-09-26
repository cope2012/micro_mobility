from bicycle import Bicycle
from scooter import Scooter
from electric_bicycle import ElectricBicycle
import json


with open('db.json', 'r') as f:
    vehicles_data = json.load(f)
    # print(vehicles_data)


scooters_from_db = filter(lambda x: x['type'] == 'scooter', vehicles_data['vehicles'])
bicycles_from_db = filter(lambda x: x['type'] == 'bicycle', vehicles_data['vehicles'])
electric_bicycles_from_db = filter(lambda x: x['type'] == 'electric-bicycle', vehicles_data['vehicles'])
scooters_list = []
bicycles_list = []
electric_bicycles_list = []

for scooter_item in scooters_from_db:
    scooters_list.append(
        Scooter.from_db(
            uuid=scooter_item['uuid'],
            battery=scooter_item['battery'],
            status=scooter_item['status']
        )
    )

# for bicycle_item in bicycles_from_db:
#     bicycles_list.append(Bicycle())
#
# for electric_bicycle_item in electric_bicycles_from_db:
#     electric_bicycles_list.append(
#         ElectricBicycle(battery=electric_bicycle_item['battery'])
#     )


s1 = scooters_list[0]
print(s1.uuid)
print(s1.status)
print(s1.battery)
s1.unlock()
