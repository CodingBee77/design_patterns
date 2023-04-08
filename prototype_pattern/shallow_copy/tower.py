from abs_computer import AbsComputer
from abc_prototype import AbsPrototype
import copy


class MainBoard(object):
    manufacturer: str
    model: str

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model


class Tower(AbsComputer, AbsPrototype):
    def __init__(self, model, mainboard, processor, memory, hard_drive,
                 graphics, monitor):
        self.model = model
        self.mainboard = mainboard
        self.processor = processor
        self.memory = memory
        self.hard_drive = hard_drive
        self.graphics = graphics
        self.monitor = monitor

    def display(self):
        print(f"Custom Computer: {self.model}")
        print(f"Mainboard: {self.mainboard.model}")
        print(f"Processor: {self.processor}")
        print(f"Memory: {self.memory}")
        print(f"Hard drive: {self.hard_drive}")
        print(f"Graphics: {self.graphics}")
        print(f"Monitor: {self.monitor if self.monitor else 'None'}")

    def clone(self):
        return copy.deepcopy(self)
