from micro_mobility import Bicycle
from micro_mobility import Scooter


print('================== BIKE TESTS =======================')
b1 = Bicycle()
# ============= First iteration =============
assert b1.status == 'locked'
assert not b1.maintenance
assert b1.current_speed == 0
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.current_speed = 30
assert b1.current_speed == 30
b1.end_ride()
assert b1.current_speed == 0
assert b1.status == 'locked'  # only when the status changes from 'ín-ride' to 'locked' the num_rides should increment
# ============= First iteration end =============

# ============= Second iteration =============
assert not b1.maintenance
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.end_ride()
assert b1.status == 'locked'
# ============= Second iteration end =============

# ============= Third iteration =============
assert not b1.maintenance
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.end_ride()
assert b1.status == 'locked'
# ============= Third iteration end =============

# ============= Fourth iteration =============
assert b1.maintenance
b1.unlock()
assert b1.status == 'locked'
b1.repair()
assert not b1.maintenance
b1.unlock()
assert b1.status == 'unlocked'
b1.begin_ride()
assert b1.status == 'in-ride'
b1.end_ride()
assert b1.status == 'locked'
# ============= Fourth iteration end =============
print('All bikes tests passed')
print('================== BIKE TESTS END =======================')

print('================== SCOOTER TESTS =======================')
s1 = Scooter()
# ============= First iteration =============
assert s1.status == 'locked'
assert s1.current_speed == 0
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.current_speed = 20
assert s1.current_speed == 20
s1.end_ride()
assert s1.status == 'locked'  # only when the status changes from 'ín-ride' to 'locked' the battery should decrement
assert s1.battery == 82
# assert s1.current_speed == 'You are riding at 0 km/h'  # This should be changed to 0 once the vehicle is locked
# ============= First iteration end =============

# ============= Second iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 65
# ============= Second iteration end =============

# ============= Third iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 48
# ============= Third iteration end =============

# ============= Fourth iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 31
# ============= Fourth iteration end ============

# ============= Fifth iteration =============
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.end_ride()
assert s1.status == 'locked'
assert s1.battery == 14
# ============= Fifth iteration end =============

# ============= Sixth iteration =============
s1.unlock()
assert s1.status == 'locked'
s1.charge()
s1.unlock()
assert s1.status == 'unlocked'
s1.begin_ride()
assert s1.status == 'in-ride'
s1.current_speed = 50
assert s1.current_speed == 35
# ============= Sixth iteration end =============
print('All scooter tests passed')
print('================== SCOOTER TESTS END =======================')