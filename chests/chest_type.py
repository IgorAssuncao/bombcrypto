from enum import Enum, auto, unique


@unique
class ChestType(Enum):
    REGULAR = auto()
    WOODEN = auto()
    METAL = auto()
    GOLD = auto()
    CRYSTAL = auto()
    ADVENTURE = auto()
    JAIL = auto()
