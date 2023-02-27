from chevyvolt import ChevyVolt
from fordfusion import FordFusion
from jeepsahara import JeepSahara
from nullcar import NullCar


def get_car(car_name):
    if car_name == "Chevy" or car_name == "Chevrolet":
        return ChevyVolt()
    elif car_name == "Ford":
        return FordFusion()
    elif car_name == "Jeep Sahara":
        return JeepSahara()
    else:
        return NullCar(car_name)


if __name__ == "__main__":
    for car_name in "Chevy", "Ford", "Jeep", "Tesla":
        car = get_car(car_name)
        car.start()
        car.stop()
