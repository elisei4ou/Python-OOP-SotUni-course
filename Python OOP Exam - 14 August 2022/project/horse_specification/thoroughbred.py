from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_HORSE_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + 3 > self.MAX_HORSE_SPEED:
            self.speed = self.MAX_HORSE_SPEED
        else:
            self.speed += 3
