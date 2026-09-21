from app.knight import Knight
from app.fight import Fight
from app.constants import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot_data = knights_config["lancelot"]

    lancelot = Knight(
        lancelot_data["name"], lancelot_data["power"], lancelot_data["hp"]
    )
    lancelot.battle_preparation(
        lancelot_data["armour"],
        lancelot_data["weapon"],
        lancelot_data["potion"],
    )

    arthur_data = knights_config["arthur"]

    arthur = Knight(
        arthur_data["name"],
        arthur_data["power"],
        arthur_data["hp"],
    )
    arthur.battle_preparation(
        arthur_data["armour"], arthur_data["weapon"], arthur_data["potion"]
    )

    mordred_data = knights_config["mordred"]

    mordred = Knight(
        mordred_data["name"], mordred_data["power"], mordred_data["hp"]
    )
    mordred.battle_preparation(
        mordred_data["armour"], mordred_data["weapon"], mordred_data["potion"]
    )

    red_knight_data = knights_config["red_knight"]

    red_knight = Knight(
        red_knight_data["name"],
        red_knight_data["power"],
        red_knight_data["hp"],
    )
    red_knight.battle_preparation(
        red_knight_data["armour"],
        red_knight_data["weapon"],
        red_knight_data["potion"],
    )

    Fight.fight(lancelot, mordred)
    Fight.fight(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
