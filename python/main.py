from chests.chest import Chest
from chests.chest_color import ChestColor

CHESTS = [
    Chest(name = 'Regular'),
    Chest(name = 'Wooden', color = ChestColor.BROWN),
    Chest(name = 'Metal', color = ChestColor.PURPLE),
    Chest(name = 'Gold', color = ChestColor.GOLD),
    Chest(name = 'Crystal', color = ChestColor.BLUE),
    Chest(name = 'Jail', color = ChestColor.GRAY),
    Chest(name = 'Adventure', color = ChestColor.RED)
]

def find_chest_by_color(color: ChestColor) -> Chest:
    for chest in CHESTS:
        if chest.color == color:
            return chest
    return None


def calculate_chest_bcoin_rewards(chest: Chest) -> float:
    return chest.get_bcoin_rewards()

if __name__ == '__main__':
    chest = find_chest_by_color(ChestColor.BROWN)
    print(9 * calculate_chest_bcoin_rewards(chest))
