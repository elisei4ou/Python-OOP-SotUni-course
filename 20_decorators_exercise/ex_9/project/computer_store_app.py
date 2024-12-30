from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTER:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)
            return result

        if type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)
            return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        found_computer = None

        for computer in self.warehouse:
            if computer.price <= client_budget:
                if computer.processor == wanted_processor:
                    if computer.ram >= wanted_ram:
                        found_computer = computer

        if not found_computer:
            raise Exception("Sorry, we don't have a computer for you.")

        sale_price = client_budget - found_computer.price
        self.profits += sale_price
        self.warehouse.remove(found_computer)

        return f"{str(found_computer)} sold for {client_budget}$."



