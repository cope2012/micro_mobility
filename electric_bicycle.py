from .bicycle import Bicycle
from .mixins.electric_vehicle import ElectricVehicle


class ElectricBicycle(Bicycle, ElectricVehicle):
    __MAX_SPEED = float('inf')
    __EMPTY_BATTERY_MAINTENANCE = 2

    def __init__(self, battery=99):
        super().__init__(battery)
        self.__empty_battery_count = 0

    @property
    def empty_battery_count(self):
        return self.__empty_battery_count

    def check_empty_battery_count(self):
        if self.needs_charge:
            self.__empty_battery_count += 1
            if (not self.maintenance) and (self.__empty_battery_count == ElectricBicycle.__EMPTY_BATTERY_MAINTENANCE):
                self.maintenance = True

    def end_ride(self):
        if super().end_ride():
            self.battery -= 17
            self.check_empty_battery_count()

    def back_to_service(self):
        if not self.needs_charge:
            super().back_to_service()
        else:
            print('The electric bike needs charge, can\'t leave warehouse')

    def unlock(self):
        if not self.needs_charge:
            super().unlock()
        else:
            print('This electric bike has no enough battery, please charge it')

    def charge(self):
        if self.status == 'in-warehouse':
            super().charge()
            if self.__empty_battery_count == ElectricBicycle.__EMPTY_BATTERY_MAINTENANCE:
                self.__empty_battery_count = 0
