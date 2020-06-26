class Vehicle:
    def __new__(cls, *args, **kwargs):
        if cls != Vehicle:
            return super().__new__(cls, *args, **kwargs)
        raise TypeError("Class Vehicle may not be instantiated")

    def __init__(self, *args, **kwargs):
        self.__status = 'locked'
        self._current_speed = 0
        super().__init__(*args, **kwargs)

    @property
    def status(self):
        return self.__status

    def unlock(self):
        if self.__status == 'locked':
            self.__status = 'unlocked'
        else:
            print(f'{self.__status} to \'unlocked\' is not a valid transition')

    def pick_up(self):
        if self.__status == 'locked':
            self.__status = 'in-transit'
        else:
            print(f'{self.__status} to \'in-transit\' is not a valid transition')

    def stashed(self):
        if self.__status == 'in-transit':
            self.__status = 'in-warehouse'
        else:
            print(f'{self.__status} to \'in-warehouse\' is not a valid transition')

    def back_to_service(self):
        if self.__status == 'in-warehouse':
            self.__status = 'deploying'
        else:
            print(f'{self.__status} to \'in-warehouse\' is not a valid transition')

    def deploy(self):
        if self.__status == 'deploying':
            self.__status = 'locked'
        else:
            print(f'{self.__status} to \'deploying\' is not a valid transition')

    def begin_ride(self):
        if self.__status == 'unlocked':
            self.__status = 'in-ride'
        else:
            print(f'{self.__status} to \'in-ride\' is not a valid transition')

    def end_ride(self):
        if self.__status == 'in-ride' and self._current_speed == 0:
            self.__status = 'locked'
            return True
        elif self._current_speed != 0:
            print(f'vehicle must be in a complete stop in order to end the ride')
        else:
            print(f'{self.__status} to \'locked\' is not a valid transition')
        return False

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if self.__status == 'in-ride':
            self._current_speed = value
