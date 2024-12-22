from typing import List

from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = songs
        self.published = False
        self.songs: List[Song] = [x for x in songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            searched_song = next(filter(lambda x: x.name == song_name, self.songs))
            self.songs.remove(searched_song)
            return f"Removed song {song_name} from album {self.name}."
        except StopIteration:
            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"

        for s in self.songs:
            result += f"== {s.get_info()}\n"

        return result


