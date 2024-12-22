class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return  self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        reversed_string = reversed(self.data)
        return f"[{', '.join(reversed_string)}]"
