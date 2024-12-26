from typing import List

from ex_4.project import Customer
from ex_4.project import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def search_by_id(_id, list_with_obj):
        try:
            return next(filter(lambda x: x.id == _id, list_with_obj))
        except StopIteration:
            return None

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer: Customer = self.search_by_id(customer_id, self.customers)
        dvd: DVD = self.search_by_id(dvd_id, self.dvds)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer: Customer = self.search_by_id(customer_id, self.customers)
        dvd: DVD = self.search_by_id(dvd_id, self.dvds)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for every_customer in self.customers:
            result.append(repr(every_customer))
        for every_dvd in self.dvds:
            result.append(repr(every_dvd))

        return "\n".join(result)
