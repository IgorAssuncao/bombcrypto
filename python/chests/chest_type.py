from enum import Enum, auto, unique
from chest_rewards import ChestRewards


@unique
class ChestTypeEnum(Enum):
    REGULAR = auto()
    WOODEN = auto()
    METAL = auto()
    GOLD = auto()
    CRYSTAL = auto()
    ADVENTURE = auto()
    JAIL = auto()


class ChestType:
    def __init__(self, name: str):
        self.chest_type = ChestTypeEnum[name.upper()]
        self.rewards = ChestRewards(chest_type=self.chest_type)
