from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    def get_species(self):
        return self.__class__.__name__


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "bark bark"


class Chicken(Animal):
    def make_sound(self):
        return "quack"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]

animal_sound(animals)
