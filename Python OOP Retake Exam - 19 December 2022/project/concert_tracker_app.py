from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        musician = self.find_obg_by_name(name, self.musicians)
        if musician:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self.find_obg_by_name(name, self.bands)

        if band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.find_concert(place)

        if concert:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_obg_by_name(musician_name, self.musicians)
        band = self.find_obg_by_name(band_name, self.bands)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):

        band = self.find_obg_by_name(band_name, self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.find_obg_by_name(musician_name, band.members)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert: Concert = [c for c in self.concerts if c.place == concert_place][0]
        band = self.find_obg_by_name(band_name, self.bands)
        self.check_all_valid_members(band)

        if concert.genre == "Rock":
            profit = self.starting_rock_concert(band, concert)
            return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

        if concert.genre == "Metal":
            profit = self.starting_metal_concert(band, concert)
            return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

        if concert.genre == "Jazz":
            profit = self.starting_jazz_concert(band, concert)
            return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    @staticmethod
    def find_obg_by_name(name, list_with_obj):
        try:
            return next(filter(lambda m: m.name == name, list_with_obj))
        except StopIteration:
            return None

    def find_concert(self, place):
        try:
            return next(filter(lambda c: c.place == place, self.concerts))
        except StopIteration:
            return None

    @staticmethod
    def check_all_valid_members(band: Band):
        NEEDED_MEMBERS = ["Drummer", "Singer", "Guitarist"]

        for musician in band.members:
            if musician.__class__.__name__ in NEEDED_MEMBERS:
                NEEDED_MEMBERS.remove(musician.__class__.__name__)

        if NEEDED_MEMBERS:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

    def starting_rock_concert(self, band, concert):
        for musician in band.members:
            if musician.__class__.__name__ == "Drummer":
                if "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if musician.__class__.__name__ == "Singer":
                if "sing high pitch notes" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if musician.__class__.__name__ == "Guitarist":
                if "play rock" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = concert.calculate_profit()

        return profit

    def starting_metal_concert(self, band, concert):
        for musician in band.members:
            if musician.__class__.__name__ == "Drummer":
                if "play the drums with drumsticks" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if musician.__class__.__name__ == "Singer":
                if "sing low pitch notes" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if musician.__class__.__name__ == "Guitarist":
                if "play metal" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = concert.calculate_profit()

        return profit

    def starting_jazz_concert(self, band, concert):
        for musician in band.members:
            if musician.__class__.__name__ == "Drummer":
                if "play the drums with drum brushes" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if musician.__class__.__name__ == "Singer":
                if "sing low pitch notes" not in musician.skills or "sing high pitch notes" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")
            if musician.__class__.__name__ == "Guitarist":
                if "play jazz" not in musician.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = concert.calculate_profit()

        return profit
