class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_idx = len(self.iterable)
        self.end_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start_idx -= 1
        if self.start_idx >= self.end_idx:
            return self.iterable[self.start_idx]
        raise StopIteration


reversed_list = reverse_iter([5, 4, 6, 1])
for item in reversed_list:
    print(item)
