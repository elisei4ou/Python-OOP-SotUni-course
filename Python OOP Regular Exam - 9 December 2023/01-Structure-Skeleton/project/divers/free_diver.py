from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, self.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        if self.oxygen_level - round(0.6 * time_to_catch) <= 0:
            self.oxygen_level = 0
            self.has_health_issue = True
        else:
            self.oxygen_level -= round(0.6 * time_to_catch)

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL
