class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1

        if self.idx < len(self.keys):
            return (self.keys[self.idx], self.dictionary[self.keys[self.idx]])
        raise StopIteration


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

