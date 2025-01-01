from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    INITIAL_BUDGET: float = 1000.0
    TYPE_ = "OutdoorTeam"

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.INITIAL_BUDGET)

    def win(self):
        self.advantage += 115
        self.wins += 1
