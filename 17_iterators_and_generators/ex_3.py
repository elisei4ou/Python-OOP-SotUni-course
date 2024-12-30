class vowels:
    VOWELS = ["a", "e", "i", "o", "u", "y"]

    def __init__(self, string: str):
        self.string = string
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            self.idx += 1

            if self.idx >= len(self.string):
                break
            if self.string[self.idx].lower() in vowels.VOWELS:
                return self.string[self.idx]
    
        raise StopIteration


my_string = vowels('dfgjdlfjsadlfjklewjfewesdvg')
for char in my_string:
    print(char)

