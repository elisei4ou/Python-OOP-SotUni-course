class NextID:
    id = -1  # not needed, only to avoid warnings

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def incrementation(cls):
        cls.id += 1