from micro_mobility import Bicycle
from micro_mobility import Scooter
from micro_mobility import ElectricBicycle
import json
import MySQLdb


db = MySQLdb.connect(user="test", passwd="TestUser2020!", db="mobility-test")
c = db.cursor()
c.execute("""SELECT * FROM scooter""")
columns = [col[0] for col in c.description]
scooters_from_db = [dict(zip(columns, row)) for row in c.fetchall()]
c.close()

# file = open('db.json', 'r')
# raw_data = file.read()
# file.close()
# vehicles_data = json.loads(raw_data)
# scooters_from_db = filter(lambda x: x['type'] == 'scooter', vehicles_data['vehicles'])
scooters_list = []

for scooter_item in scooters_from_db:
    scooters_list.append(Scooter.from_db(**scooter_item))

s1 = scooters_list[0]
# s2 = scooters_list[1]
print(s1)
# s1.unlock()
# s1.begin_ride()
s1.current_speed = 50
# s1.end_ride()
# print(s1.status)
