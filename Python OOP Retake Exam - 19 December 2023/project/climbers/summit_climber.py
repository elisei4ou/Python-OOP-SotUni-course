from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5
        self.conquered_peaks.append(peak.name)
