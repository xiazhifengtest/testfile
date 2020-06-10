class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('this car has ' + str(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you can not roll back an odometer')

    def incremeter_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('this is car has a ' + str(self.battery_size) + ' k  m')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'this car can go approxmately' + str(range)
        message += 'miles on a full charge'
        print(message)


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        self.battery_size = 70

    def describe_battery(self):
        print('this is car has a ' + str(self.battery_size) + ' k  m')


def fill_gas_tank():
    print('this car doesnt need a gas tahk')
