from chest_color import ChestColor
from chest_rewards import ChestRewards
from chest_type import ChestType


class Chest:
    def __init__(self, name: str, color: ChestColor = ChestColor.GREEN) -> None:
        self.name = f'{name} chest'
        self.color = color
        self.chest_type = ChestType(name.upper())

    def get_bcoin_rewards(self) -> float:
        return self.chest_type.rewards.bcoin
