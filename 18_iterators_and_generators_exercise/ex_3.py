class countdown_iterator:
    def __init__(self, count: int):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count >= 0:
            return self.count
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
