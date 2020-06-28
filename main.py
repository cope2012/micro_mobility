from micro_mobility import Bicycle
from micro_mobility import Scooter
from micro_mobility import ElectricBicycle
import MySQLdb


db = MySQLdb.connect(user="test", passwd="TestUser2020!", db="mobility-test")
c = db.cursor()
c.execute("""SELECT * FROM scooter""")
columns = [col[0] for col in c.description]
scooters_from_db = [dict(zip(columns, row)) for row in c.fetchall()]
c.close()

scooters_list = []

for scooter_item in scooters_from_db:
    scooters_list.append(Scooter.from_db(**scooter_item))

s1 = scooters_list[0]
print(s1)
s1.begin_ride()
print(s1.status)
s1.current_speed = 50
