from .vehicle import Vehicle


class Scooter(Vehicle):
    __MAX_SPEED = 35
    __FULL_CHARGE = 100

    def __init__(self, battery=99):
        super().__init__()
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if value < 0:
            self.__battery = 0
        elif value > 100:
            self.__battery = 100
        else:
            self.__battery = value

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value > Scooter.__MAX_SPEED:
            self._current_speed = Scooter.__MAX_SPEED
        else:
            self._current_speed = value

    def _check_battery(self):
        return self.__battery >= 15

    def begin_ride(self):
        super().begin_ride()

    def unlock(self):
        if self._check_battery():
            super().unlock()
        else:
            print('This scooter has no enough battery, please charge it')

    def end_ride(self):
        if super().end_ride():
            self.battery -= 17

    def charge(self):
        self.__battery = Scooter.__FULL_CHARGE