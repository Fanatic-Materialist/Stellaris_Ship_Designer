from stellaris_ship_design.ship import *
from stellaris_ship_design.weapon import *


# TODO Create global resource dict and load all data from csv while importing

def load_weapon_templates(csv_string: str, sep: str = ',', line_sep: str = '\n'):
    weapons = []
    lines = csv_string.split(line_sep)
    for line in lines[1:]:  # start from the second line
        if line != '' and not line.startswith(
                '#'):  # if this line is not empty or comment
            values = line.split(sep)
            params = values[0:1] + values[2:10]
            target_modifiers = values[-5:]
            w = Weapon(*params)
            m = WeaponTargetModifier(*target_modifiers)
            w.add_modifier(m)
            weapons.append(w)
    return weapons


def load_ship_templates(csv_string: str, sep: str = ',', line_sep: str = '\n'):
    ship_templates = []
    lines = csv_string.split(line_sep)
    for line in lines[1:]:  # start from the second line
        if line != '' and not line.startswith(
                '#'):  # if this line is not empty or comment
            values = line.split(sep)
            section_names = values[1].split(' ')
            sections = {}
            for section_name in section_names:
                sections[SHIP_SECTIONS(section_name)] = None
                # TODO Move the string to constant converting to Ship and Section class
            ship = Ship(values[0], SHIP_CLASSES(values[0]), sections,
                        *values[2:], modfiers=None)
            ship_templates.append(ship)
    return ship_templates

if __name__ == '__main__':

    # Weapon loading

    with open('data/weapons.csv') as f:
        csv_string = f.read()

    w = load_weapon_templates(csv_string)

    for i in w:
        print(i)
