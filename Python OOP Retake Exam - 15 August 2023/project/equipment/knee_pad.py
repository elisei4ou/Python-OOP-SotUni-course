from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    KNEE_PROTECTION: int = 120
    KNEE_PRICE: float = 15.0
    TYPE_ = "KneePad"

    def __init__(self):
        super().__init__(self.KNEE_PROTECTION, self.KNEE_PRICE)

    def increase_price(self):
        self.price *= 1.2
