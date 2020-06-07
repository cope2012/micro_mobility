class Vehicle:
    # def __new__(cls, *args, **kwargs):
    #     if cls != Vehicle:
    #         return super().__new__(cls, *args, **kwargs)
    #     raise TypeError("Class Vehicle may not be instantiated")

    def __init__(self):
        self.__status = 'locked'
        self._current_speed = 0

    @property
    def status(self):
        return self.__status

    def unlock(self):
        if self.__status == 'locked':
            self.__status = 'unlocked'
        else:
            print(f'{self.__status} to \'unlocked\' is not a valid transition')

    def begin_ride(self):
        if self.__status == 'unlocked':
            self.__status = 'in-ride'
        else:
            print(f'{self.__status} to \'in-ride\' is not a valid transition')

    def end_ride(self):
        if self.__status == 'in-ride':
            self.__status = 'locked'
            self._current_speed = 0
            return True
        else:
            print(f'{self.__status} to \'locked\' is not a valid transition')
            return False

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        self._current_speed = value
