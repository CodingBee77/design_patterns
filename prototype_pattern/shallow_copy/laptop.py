from abs_computer import AbsComputer
from abc_prototype import AbsPrototype
import copy


class Laptop(AbsComputer, AbsPrototype):
    def __init__(self, model, processor, memory, hard_drive, graphics, screen):
        self.model = model
        self.processor = processor
        self.memory = memory
        self.hard_drive = hard_drive
        self.graphics = graphics
        self.screen = screen

    def __str__(self):
        return f"Custom Computer: {self.model} \n Processor: {self.processor} \n Memory: {self.memory} \n Hard drive: {self.hard_drive} \n Graphics: {self.graphics} \n Screen: {self.screen}"


    def display(self):
        print(f"Custom Computer: {self.model}")
        print(f"Processor: {self.processor}")
        print(f"Memory: {self.memory}")
        print(f"Hard drive: {self.hard_drive}")
        print(f"Graphics: {self.graphics}")
        print(f"Screen: {self.screen}")

    def clone(self):
        return copy.copy(self)
