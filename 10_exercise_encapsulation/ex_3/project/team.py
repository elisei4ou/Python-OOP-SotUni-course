from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def search_player(self, p_n: str, p_l: List[Player]):
        try:
            searched_player = next(filter(lambda x: x.name == p_n, p_l))
            return searched_player
        except StopIteration:
            return None

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        searched_player = self.search_player(player_name, self.__players)

        if searched_player:
            self.__players.remove(searched_player)
            return searched_player
        return f"Player {player_name} not found"

