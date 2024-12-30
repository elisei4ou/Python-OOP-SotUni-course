import math

from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {"AMD Ryzen 9 5950X": 900,
                  "Intel Core i9-11900H": 1050,
                  "Apple M1 Pro": 1200}
    RAMS = [2, 4, 8, 16, 32, 64]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop  {self.manufacturer} {self.model}!")
        if ram not in self.RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop  {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        processor_price = self.PROCESSORS[processor]
        ram_price = int(math.log(self.ram, 2)) * 100
        self.price += processor_price + ram_price

        return f"Created {self.__repr__()} for {self.price}$."