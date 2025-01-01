from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENTS = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENTS.keys():
            raise ValueError("Invalid equipment type!")

        new_equipment = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS.keys():
            raise ValueError("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self.find_equipment(equipment_type)
        team = self.find_team(team_name)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.find_team(team_name)

        if not team:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_equipments = 0

        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                changed_equipments += 1

        return f"Successfully changed {changed_equipments}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first_team = self.find_team(team_name1)
        second_team = self.find_team(team_name2)

        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_points = sum(e.protection for e in first_team.equipment) + first_team.advantage
        second_team_points = sum(e.protection for e in second_team.equipment) + second_team.advantage

        if first_team_points > second_team_points:
            first_team.win()
            return f"The winner is {team_name1}."

        if second_team_points > first_team_points:
            second_team.win()
            return f"The winner is {team_name2}."

        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        info = '\n'.join([t.get_statistics() for t in sorted_teams])
        result = f"Tournament: {self.name}\n" \
                 f"Number of Teams: {len(self.teams)}\n" \
                 f"Teams:\n" \
                 f"{info}"

        return result

    def find_equipment(self, equipment_type):
        try:
            equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]
            return equipment
        except IndexError:
            return None

    def find_team(self, team_name):
        try:
            team = [t for t in self.teams if t.name == team_name][0]
            return team
        except IndexError:
            return None
