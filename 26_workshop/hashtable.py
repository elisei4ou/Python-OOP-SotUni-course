class HashTable:
    def __init__(self):
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4

    def __setitem__(self, key: str, value: any):
        if self.count() == self.__length:
            self.erase_length()

        hash_idx = self.hash(key)
        index = self.find_idx(hash_idx)
        self.__keys[index] = key
        self.__values[index] = value

    def __getitem__(self, key):
        try:
            key_idx = self.__keys.index(key)
            return self.__values[key_idx]
        except ValueError:
            raise KeyError("The key does not exist")

    def __len__(self):
        return self.__length

    def __str__(self):
        result = ""
        for i in range(len(self.__keys)):
            if self.__keys[i]:
                result += f"'{self.__keys[i]}': {self.__values[i]} "

        return "{" + result.strip() + "}"

    def get_keys(self):
        return self.__keys

    def get_values(self):
        return self.__values

    def hash(self, key):
        idx = sum([ord(el) for el in key]) % self.__length
        return idx

    def find_idx(self, idx):
        current_idx = self.__keys[idx]
        if current_idx == self.__length:
            current_idx = 0
        if current_idx is not None:
            return self.find_idx(idx + 1)
        return idx

    def erase_length(self):
        self.__keys = self.__keys + [None] * self.__length
        self.__values = self.__values + [None] * self.__length
        self.__length *= 2

    def count(self):
        count_of_elements = len([el for el in self.__keys if el])
        return count_of_elements

    def add(self, key: str, value: any):
        self.__setitem__(key, value)

    def get(self, key, default=None):
        try:
            key_idx = self.__keys.index(key)
            return self.__values[key_idx]
        except ValueError:
            return default

    def sort(self):
        keys = [el for el in self.__keys if el]
        values = [el for el in self.__values if el]
        dif = self.__length - len(keys)
        sorted_zip = list(zip(keys, values))
        sorted_result = sorted(sorted_zip, key=lambda t: t[0])

        table = HashTable()
        table._HashTable__keys = [t[0] for t in sorted_result] + [None] * dif
        table._HashTable__values = [t[1] for t in sorted_result] + [None] * dif

        return table

table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
print(table.sort())

