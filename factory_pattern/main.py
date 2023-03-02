from autofactory import AutoFactory


if __name__ == "__main__":
    factory = AutoFactory()
    for car_name in "ChevyVolt", "FordFusion", "JeepSahara", "Tesla Roadster":
        car = factory.create_instance(car_name)
        car.start()
        car.stop()
