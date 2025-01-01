from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPE = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPE = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = self.find_delicacy(name)

        if delicacy:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.VALID_DELICACY_TYPE:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.VALID_DELICACY_TYPE[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self.find_booth(booth_number)

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.VALID_BOOTH_TYPE:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.VALID_BOOTH_TYPE[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.find_available_booth(number_of_people)

        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_booth(booth_number)
        delicacy = self.find_delicacy(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth(booth_number)
        bill = sum([d.price for d in booth.delicacy_orders]) + booth.price_for_reservation

        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def find_delicacy(self, delicacy_name):
        try:
            delicacy = [d for d in self.delicacies if delicacy_name == d.name][0]
            return delicacy
        except IndexError:
            return None

    def find_booth(self, booth_number):
        try:
            booth = [b for b in self.booths if booth_number == b.booth_number][0]
            return booth
        except IndexError:
            return None

    def find_available_booth(self, number_of_people):
        for b in self.booths:
            if not b.is_reserved and b.capacity >= number_of_people:
                return b

        return None
