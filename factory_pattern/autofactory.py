from inspect import getmembers, isclass, isabstract
import autos


class AutoFactory(object):
    autos = {}  # Key = car model name, Value = class for the car

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbsAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, car_name):
        if car_name in self.autos:
            return self.autos[car_name]()
        else:
            return autos.NullCar(car_name)
