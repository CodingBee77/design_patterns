from abs_car import AbsClass


class Sport(AbsClass):

    @property
    def description(self):
        return 'Sport'

    @property
    def cost(self):
        return 15000.00