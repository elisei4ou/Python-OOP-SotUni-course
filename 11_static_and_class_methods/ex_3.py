class Integer:
    ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        sum = 0

        for i in range(len(value)):
            if i != 0 and value[i] > value[i - 1]:
                sum += Integer.ROMAN[value[i]] - 2 * Integer.ROMAN[value[i - 1]]
            else:
                sum += Integer.ROMAN[value[i]]

        return cls(sum)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
