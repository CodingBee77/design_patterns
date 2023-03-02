from .abs_auto import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, car_name):
        self._car_name = car_name

    def start(self):
        print(f"Unknown car {self._car_name}")

    def stop(self):
        pass
