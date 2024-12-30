import math

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {"AMD Ryzen 7 5700G": 500,
                  "Intel Core i5-12600K": 600,
                  "Apple M1 Max": 1800}
    RAMS = [2, 4, 8, 16, 32, 64, 128]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram not in self.RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        processor_price = self.PROCESSORS[processor]
        ram_price = int(math.log(self.ram, 2)) * 100
        self.price += processor_price + ram_price

        return f"Created {self.__repr__()} for {self.price}$."





