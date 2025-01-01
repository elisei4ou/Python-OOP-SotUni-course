from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5
        self.conquered_peaks.append(peak.name)
