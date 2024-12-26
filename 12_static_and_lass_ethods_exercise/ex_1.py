from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for x in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        page = 1
        for every_page in self.photos:
            if len(every_page) < 4:
                every_page.append(label)
                return f"{label} photo added successfully on page {page} slot {len(every_page)}"
            page += 1

        return "No more free slots"

    def display(self):
        result = ["-----------"]

        for x in range(self.pages):
            current_page = f'{"[] " * len(self.photos[x])}'
            result.append(current_page.strip())
            result.append("-----------")

        return '\n'.join(result)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())






