import abc


class Subscription(abc.ABC):

    def __init__(self, subscriber, enrolled):
        self._subscriber = subscriber
        self._enrolled = enrolled

    @property
    def subscriber(self):
        return self._subscriber

    @property
    def enrolled(self):
        return self._enrolled

    @property
    @abc.abstractmethod
    def price(self):
        pass

    @property
    @abc.abstractmethod
    def expiration(self):
        pass
