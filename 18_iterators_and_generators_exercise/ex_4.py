class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.start = -1
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start < self.number:
            self.idx += 1
            if self.idx >= len(self.sequence):
                self.idx = 0
            return self.sequence[self.idx]
        raise StopIteration


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

