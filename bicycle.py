from .vehicle import Vehicle


class Bicycle(Vehicle):
    MAX_NUM_OF_RIDES = 3

    def __init__(self):
        super().__init__()
        self.__maintenance = False
        self.__continues_rides = 0

    @property
    def maintenance(self):
        return self.__maintenance

    @property
    def continues_rides(self):
        return self.__continues_rides

    def check_maintenance(self):
        if self.continues_rides == Bicycle.MAX_NUM_OF_RIDES:
            self.__maintenance = True

    def begin_ride(self):
        if not self.maintenance:
            super().begin_ride()
        else:
            print('This bike needs maintenance and therefore it can\'t initiate a ride')

    def back_to_service(self):
        if not self.maintenance:
            super().back_to_service()
        else:
            print('The bike needs maintenance, can\'t leave warehouse')

    def unlock(self):
        if not self.maintenance:
            super().unlock()
        else:
            print('This bike needs maintenance and therefore it can\'t be unlocked')

    def end_ride(self):
        if super().end_ride():
            self.__continues_rides += 1
            self.check_maintenance()

    def repair(self):
        if self.maintenance:
            if self.status == 'in-warehouse':
                self.__maintenance = False
                self.__continues_rides = 0
        else:
            print('this bike doesn\'t need reparation')
