from random import randint

def roll_dice(number = 1, sides = 20):
    result = 0

    for i in range(0, number):
        result += randint(1, sides)
    return result

def generate_new_character():

    character = {}

    character['str'] = roll_dice(3,6)
    character['dex'] = roll_dice(3,6)
    character['con'] = roll_dice(3,6)
    character['wis'] = roll_dice(3,6)
    character['int'] = roll_dice(3,6)
    character['cha'] = roll_dice(3,6)

    return character

new_character = generate_new_character()
print(new_character)