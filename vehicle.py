import json

class Vehicle:

    def __init__(self, *args, **kwargs):
        self.__uuid = kwargs['uuid']
        self.__status = 'locked'
        self._current_speed = 0
        super().__init__(*args, **kwargs)

    @property
    def uuid(self):
        return self.__uuid

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
        self.update_vehicle_on_db()

    def unlock(self):
        if self.__status == 'locked':
            self.status = 'unlocked'
        else:
            print(f'{self.__status} to \'unlocked\' is not a valid transition')

    def pick_up(self):
        if self.__status == 'locked':
            self.status = 'in-transit'
        else:
            print(f'{self.__status} to \'in-transit\' is not a valid transition')

    def stashed(self):
        if self.__status == 'in-transit':
            self.status = 'in-warehouse'
        else:
            print(f'{self.__status} to \'in-warehouse\' is not a valid transition')

    def back_to_service(self):
        if self.__status == 'in-warehouse':
            self.status = 'deploying'
        else:
            print(f'{self.__status} to \'in-warehouse\' is not a valid transition')

    def deploy(self):
        if self.__status == 'deploying':
            self.status = 'locked'
        else:
            print(f'{self.__status} to \'deploying\' is not a valid transition')

    def begin_ride(self):
        if self.__status == 'unlocked':
            self.status = 'in-ride'
        else:
            print(f'{self.__status} to \'in-ride\' is not a valid transition')

    def end_ride(self):
        if self.__status == 'in-ride' and self._current_speed == 0:
            self.status = 'locked'
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

    def update_vehicle_on_db(self):
        with open('db.json', 'r') as f:
            vehicles_data = json.load(f)

        this_vehicle = next(filter(lambda x: x['uuid'] == self.__uuid, vehicles_data['vehicles']))
        this_vehicle['status'] = self.status
        # print(this_vehicle)
        updated_data = list(map(lambda x: self.update_db_item(x) if x['uuid'] == self.uuid else x, vehicles_data['vehicles']))
        vehicles_data['vehicles'] = updated_data
        # print(updated_data)

        with open('db.json', 'w') as f:
            f.write(json.dumps(vehicles_data))

    def update_db_item(self, item):
        item['status'] = self.status

        return item
