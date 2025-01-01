from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = ["ArcticClimber", "SummitClimber"]
    VALID_PEAKS = ["ArcticPeak", "SummitPeak"]

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def finding_climber(self, climber_name):
        try:
            return [c for c in self.climbers if c.name == climber_name][0]
        except IndexError:
            return None

    def finding_peak(self, peak_name):
        try:
            return [p for p in self.peaks if p.name == peak_name][0]
        except IndexError:
            return None

    @staticmethod
    def is_gear_missing(gear: list, peak):
        missing_gears = []

        for every_g in peak.get_recommended_gear():
            if every_g not in gear:
                missing_gears.append(every_g)

        return sorted(missing_gears)

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        climber = self.finding_climber(climber_name)
        if climber:
            return f"{climber_name} has been already registered."

        if climber_type == "ArcticClimber":
            new_climber = ArcticClimber(climber_name)
            self.climbers.append(new_climber)
        else:
            new_climber = SummitClimber(climber_name)
            self.climbers.append(new_climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == "ArcticPeak":
            new_peak = ArcticPeak(peak_name, peak_elevation)
            self.peaks.append(new_peak)
        else:
            new_peak = SummitPeak(peak_name, peak_elevation)
            self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear):
        climber = self.finding_climber(climber_name)
        peak = self.finding_peak(peak_name)
        missing_gear = self.is_gear_missing(gear, peak)

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. " \
                   f"Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.finding_climber(climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = self.finding_peak(peak_name)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        total_conquered_peaks = []
        info_about_climbers = []

        for climber in self.climbers:
            for conquered_peak in climber.conquered_peaks:
                if conquered_peak not in total_conquered_peaks:
                    total_conquered_peaks.append(conquered_peak)

        for climber in self.climbers:
            if climber.conquered_peaks:
                info_about_climbers.append(climber)

        info_about_climbers = sorted(info_about_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))

        result = f"Total climbed peaks: {len(total_conquered_peaks)}\n" \
                 f"**Climber's statistics:**\n" \

        result += '\n'.join([str(c) for c in info_about_climbers])

        return result
