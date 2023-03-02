from autofactory import AutoFactory


if __name__ == "__main__":
    factory = AutoFactory()
    for car_name in "Chevy", "Ford", "Jeep", "Tesla":
        car = factory.create_instance(car_name)
        car.start()
        car.stop()
