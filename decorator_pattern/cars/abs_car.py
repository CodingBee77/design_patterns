import abc


class AbsCar(abc.ABC):
    @property
    @abc.abstractmethod
    def description(self):
        pass

    @property
    @abc.abstractmethod
    def cost(self):
        pass
