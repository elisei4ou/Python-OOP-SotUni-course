from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            searched_room = next(filter(lambda x: x.number == room_number, self.rooms))
        except StopIteration:
            return

        result = searched_room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            searched_room = next(filter(lambda x: x.number == room_number, self.rooms))
        except StopIteration:
            return

        people = searched_room.guests
        result = searched_room.free_room()

        if not result:
            self.guests -= people

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
               f"Free rooms: {', '.join(str(x.number) for x in self.rooms if not x.is_taken)}\n"\
               f"Taken rooms: {', '.join(str(x.number) for x in self.rooms if x.is_taken)}"
