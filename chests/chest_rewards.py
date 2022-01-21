from .chest_type import ChestType


class ChestRewards():
    def __init__(self, chest_type: ChestType) -> None:
        self.bcoin = 0
        self.hero = False
        self.adventure_key = False
        if chest_type == chest_type.JAIL:
            self.hero = True
        if chest_type == chest_type.ADVENTURE:
            self.adventure_key = True
        if chest_type == chest_type.WOODEN:
            self.bcoin = 0.01425
        if chest_type == chest_type.METAL:
            self.bcoin = 0.0325
        if chest_type == chest_type.GOLD:
            self.bcoin = 0.1625
        if chest_type == chest_type.CRYSTAL:
            self.bcoin = 0.325
