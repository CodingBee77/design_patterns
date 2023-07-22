from abs_car import AbsClass


class Luxury(AbsClass):

    @property
    def description(self):
        return 'Luxury'

    @property
    def cost(self):
        return 18000.00