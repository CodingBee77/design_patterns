class Vendor(object):
    def __init__(self, name, number, address):
        self._name = name
        self._number = number
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def address(self):
        return self._address
