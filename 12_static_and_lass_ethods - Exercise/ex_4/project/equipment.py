from project.next_id_mixin import NextID


class Equipment(NextID):
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.incrementation()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
