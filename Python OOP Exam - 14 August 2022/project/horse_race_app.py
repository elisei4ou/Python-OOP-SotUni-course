from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self.find_obj(horse_name, self.horses)
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.HORSE_TYPES:
            new_horse = self.HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.find_obj(jockey_name, self.jockeys)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        horse_race = self.find_horse_race(race_type)
        if horse_race:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey: Jockey = self.find_obj(jockey_name, self.jockeys)
        horse = self.find_horse_by_type(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.find_horse_race(race_type)
        jockey: Jockey = self.find_obj(jockey_name, self.jockeys)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_horse_race(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = race.jockeys[0]
        for j in race.jockeys:
            if j.horse.speed > winner.horse.speed:
                winner = j

        return f"The winner of the {race_type} race, " \
               f"with a speed of {winner.horse.speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."

    def find_obj(self, name, collection):
        try:
            return next(filter(lambda x: x.name == name, collection))
        except StopIteration:
            return None

    def find_horse_race(self, race_type):
        try:
            return next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            return None

    def find_horse_by_type(self, horse_type):
        try:
            horse = [h for h in self.horses if h.__class__.__name__ == horse_type][-1]
            return horse
        except IndexError:
            return None

    def find_jockey_in_race(self, jockey, race):
        try:
            person = [j for j in race.jockeys if j is jockey][0]
            return person
        except IndexError:
            return None
