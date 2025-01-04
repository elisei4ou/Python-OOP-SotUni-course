from collections.abc import Iterable
from copy import deepcopy


class CustomList:
    def __init__(self):
        self.list = []

    def append(self, value: any):
        return self.list.append(value)

    def remove(self, index: int):
        if isinstance(index, int) and index is not True:
            return self.list.pop(index)
        else:
            return "You can not remove with invalid index"

    def get(self, index: int):
        try:
            return self.list[index]
        except TypeError:
            return "You can not get with invalid index"

    def extend(self, iterable: Iterable):
        try:
            self.list.extend(iterable)
            return self.list
        except TypeError:
            return "You can not extend with not iterable object"

    def insert(self, index: int, value: any):
        if not isinstance(index, int):
            return f"You can not insert with {index.__class__.__name__}"
        if index < 0:
            return "You can not insert with negative index"
        elif index > len(self.list):
            return "You can not insert with invalid index"

        self.list.insert(index, value)
        return self.list

    def pop(self):
        if not self.list:
            return "You can not pop when the list is empty"

        return self.list.pop()

    def clear(self):
        if not self.list:
            return "You can not clear when the list is already empty"

        self.list.clear()

    def index(self, value: any):
        try:
            return self.list.index(value)
        except ValueError:
            return "The index is invalid"

    def count(self, value: any):
        if value in self.list:
            return self.list.count(value)
        return "The value is not in the list"

    def reverse(self):
        if self.list:
            return self.list[::-1]
        return "The list have no values"

    def copy(self):
        if self.list:
            return deepcopy(self.list)

    def size(self):
        return len(self.list)

    def add_first(self, value: any):
        self.list.insert(0, value)

    def dictionize(self):
        dictionized_list = {}
        for i in range(0, len(self.list), 2):
            key = self.list[i]
            try:
                value = self.list[i + 1]
                dictionized_list[key] = value
            except IndexError:
                dictionized_list[key] = " "

        return dictionized_list

    def move(self, amount):
        if amount > len(self.list):
            return "You can not move when the amount is invalid"
        return self.list[amount:] + self.list[:amount]

    def sum(self):
        amount = 0
        for el in self.list:
            try:
                amount += el
            except TypeError:
                amount += len(el)

        return amount

    def overbound(self):
        if not self.list:
            return "The list is empty"

        amount = float('-inf')
        largest = None

        for el in self.list:
            try:
                if el > amount:
                    amount = el
                    largest = el
            except TypeError:
                if len(el) > amount:
                    amount = len(el)
                    largest = el

        return self.list.index(largest)

    def underbound(self):
        if not self.list:
            return "The list is empty"

        amount = float('+inf')
        largest = None

        for el in self.list:
            try:
                if el < amount:
                    amount = el
                    largest = el
            except TypeError:
                if len(el) < amount:
                    amount = len(el)
                    largest = el

        return self.list.index(largest)
