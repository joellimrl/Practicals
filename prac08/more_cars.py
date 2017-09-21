from prac08.car import Car

class GasGuzzler(Car):
    def drive(self, distance):
        if distance * 1.5 > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= 1.5 * distance
        self.odometer += distance
        return distance

class Bomb(Car):
    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        return distance