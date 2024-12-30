from abc import ABC, abstractmethod


class Duck(ABC):

    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck:

    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return "Robotic quacking"

    @staticmethod
    def walk():
        return "Robotic walking"

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
