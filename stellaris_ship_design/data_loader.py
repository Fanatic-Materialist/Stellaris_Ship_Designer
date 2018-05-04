from stellaris_ship_design.weapon import *

def load_weapons(csv_string: str, sep: str = ',', line_sep: str = '\n'):
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


def load_ship_classes(csv_string: str, sep: str = ',', line_sep: str = '\n'):
    ship_classes = []
    lines = csv_string.split(line_sep)


if __name__ == '__main__':
    with open('data/weapons.csv') as f:
        csv_string = f.read()

    w = load_weapons(csv_string)

    for i in w:
        print(i)
