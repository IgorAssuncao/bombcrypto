from chests.chest import Chest
from chests.chest_color import ChestColor
from common.helpers import get_user_int_input

CHESTS = [
    Chest(name='Regular'),
    Chest(name='Wooden', color=ChestColor.BROWN),
    Chest(name='Metal', color=ChestColor.PURPLE),
    Chest(name='Gold', color=ChestColor.GOLD),
    Chest(name='Crystal', color=ChestColor.BLUE),
    Chest(name='Jail', color=ChestColor.GRAY),
    Chest(name='Adventure', color=ChestColor.RED)
]


def find_chest_by_color(color: ChestColor) -> Chest | None:
    for chest in CHESTS:
        if chest.color == color:
            return chest
    return None


def calculate_chest_bcoin_rewards(chest: Chest, quantity) -> float:
    return chest.get_bcoin_rewards() * quantity


if __name__ == '__main__':
    wooden_chest = find_chest_by_color(ChestColor.BROWN)
    metal_chest = find_chest_by_color(ChestColor.PURPLE)
    gold_chest = find_chest_by_color(ChestColor.GOLD)
    crystal_chest = find_chest_by_color(ChestColor.BLUE)
    adventure_chest = find_chest_by_color(ChestColor.RED)
    jail_chest = find_chest_by_color(ChestColor.GRAY)

    wooden_chests_quantity = get_user_int_input("Quantity of wood (brown) chests: ")
    metal_chests_quantity = get_user_int_input("Quantity of metal (purple) chests: ")
    gold_chests_quantity = get_user_int_input("Quantity of gold (yellow) chests: ")
    crystal_chests_quantity = get_user_int_input("Quantity of crystal (blue) chests: ")
    adventure_chests_quantity = get_user_int_input("Quantity of adventure (red) chests: ")
    jail_chests_quantity = get_user_int_input("Quantity of jail (gray) chests: ")

    wooden_chest_rewards = calculate_chest_bcoin_rewards(wooden_chest, wooden_chests_quantity)
    metal_chest_rewards = calculate_chest_bcoin_rewards(metal_chest, metal_chests_quantity)
    gold_chest_rewards = calculate_chest_bcoin_rewards(gold_chest, gold_chests_quantity)
    crystal_chest_rewards = calculate_chest_bcoin_rewards(crystal_chest, crystal_chests_quantity)
    adventure_chest_rewards = calculate_chest_bcoin_rewards(adventure_chest, adventure_chests_quantity)
    jail_chest_rewards = calculate_chest_bcoin_rewards(jail_chest, jail_chests_quantity)

    print()
    print(f'Wooden chests rewards: {wooden_chest_rewards:.5f}')
    print(f'Metal chests rewards: {metal_chest_rewards:.5f}')
    print(f'Gold chests rewards: {gold_chest_rewards:.5f}')
    print(f'Crystal chests rewards: {crystal_chest_rewards:.5f}')
    print(f'Adventure chests rewards: {adventure_chest_rewards:.5f}')
    print(f'Jail chests rewards: {jail_chest_rewards:.5f}')

    print()
    total_bcoins = wooden_chest_rewards + metal_chest_rewards + gold_chest_rewards + crystal_chest_rewards
    print(f'Total bcoins: {total_bcoins:.5f}')

    input('Press any key to exit.')
