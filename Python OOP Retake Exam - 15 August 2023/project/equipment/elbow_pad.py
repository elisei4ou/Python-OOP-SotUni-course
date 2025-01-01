from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    ELBOW_PROTECTION: int = 90
    ELBOW_PRICE: float = 25.0
    TYPE_ = "ElbowPad"

    def __init__(self):
        super().__init__(self.ELBOW_PROTECTION, self.ELBOW_PRICE)

    def increase_price(self):
        self.price *= 1.1
