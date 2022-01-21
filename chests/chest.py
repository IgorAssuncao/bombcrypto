from .chest_color import ChestColor
from .chest_rewards import ChestRewards
from .chest_type import ChestType


class Chest():
    def __init__(self, name: str, color: ChestColor = ChestColor.GREEN) -> None:
        self.name = f'{name} chest'
        self.color = color
        self.ChestType = ChestType[name.upper()]
        self.rewards = ChestRewards(self.ChestType)

    def get_bcoin_rewards(self) -> float:
        return self.rewards.bcoin
