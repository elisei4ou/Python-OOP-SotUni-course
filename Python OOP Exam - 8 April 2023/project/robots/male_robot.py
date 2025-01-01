from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    WEIGHT = 9
    WANTED_SERVICE = "MainService"

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.WEIGHT)

    def eating(self):
        self.weight += 3
