from cars.economy import Economy
from decorators.v6 import V6


def show(car):
    print(f'Description: {car.description}; cost: ${car.cost}')


def main():
    car = Economy()
    show(car)
    # Economy car is decorated with an engine
    car = V6(car)
    show(car)


if __name__ == '__main__':
    main()
