class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0 - self.step
        self.end = (self.step * self.count) - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start <= self.end:
            return self.start
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

