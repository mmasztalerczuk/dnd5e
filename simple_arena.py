from dnd_5e.character import create_character
from dnd_5e.classes import Fighter
from dnd_5e.races import Human

player_A = create_character(
    clazz=Fighter,
    race=Human,
    name="Player A",
    fighting_style=Fighter.FightingStyle.Defense,
)

player_B = create_character(
    clazz=Fighter,
    race=Human,
    name="Player B",
    fighting_style=Fighter.FightingStyle.Dueling,
)

current_player = player_A
second_player = player_B

while True:
    roll = current_player.attack_roll()
    if roll >= second_player.get_armor_class():
        print(f"{current_player.name} rolls {roll} and hit!")
        dmg = current_player.damage_roll()
        second_player.current_health -= dmg
        print(f"{current_player.name} hit for {dmg}. {second_player.name} has {second_player.current_health} hp")
        if second_player.current_health <= 0:
            print(f"{current_player.name} wins! {second_player.name} is dead.")
            break
    else:
        print(f"{current_player.name} rolls {roll} and missed")

    current_player, second_player = second_player, current_player
