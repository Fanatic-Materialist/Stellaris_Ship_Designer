from stellaris_ship_design.constants import *
from stellaris_ship_design.object import *
from stellaris_ship_design.local import *


class Weapon(Object):
    size = ''
    cost = 0.0
    power = 0.0
    avg_damage = 0.0
    cooldown = 0.0
    range = 0.0
    accuracy = 0.0
    tracking = 0.0
    target = TARGET_TYPE.NONE

    def __init__(self, id_, size, cost, power, avg_damage, cooldown, range_,
                 accuracy, tracking, modifiers=None):
        super().__init__(id_, modifiers)
        self.size = size
        self.cost = cost
        self.power = power
        self.avg_damage = avg_damage
        self.cooldown = cooldown
        self.range = range_
        self.accuracy = accuracy
        self.tracking = tracking

    def set_target(self, target: TARGET_TYPE):
        self.target = target

    def __str__(self):
        return '<%s> %s' % (type(self).__name__, local(self.id))


class WeaponTargetModifier(Modifier):
    suitable_type = Weapon

    hull_damage = 1
    shield_damage = 1
    shield_penetration = 0
    armor_damage = 1
    armor_penetration = 0

    def __init__(self, hull_damage: float = 1, shield_damage: float = 1,
                 shield_penetration: float = 0, armor_damage: float = 1,
                 armor_penetration: float = 0):
        super().__init__()
        self.hull_damage = hull_damage
        self.shield_damage = shield_damage
        self.shield_penetration = shield_penetration
        self.armor_damage = armor_damage
        self.armor_penetration = armor_penetration

    def generate_desc(self):
        # TODO Automatically generate modifier description while initializing
        pass

    def modify(self, obj: suitable_type):
        if obj.target == TARGET_TYPE.NONE:
            return
        elif obj.target == TARGET_TYPE.SHIELD:
            obj.avg_damage = obj.avg_damage * self.shield_damage * self.shield_penetration
        elif obj.target == TARGET_TYPE.ARMOR:
            obj.avg_damage = obj.avg_damage * self.armor_damage * self.armor_penetration
        elif obj.target == TARGET_TYPE.HULL:
            obj.avg_damage *= self.hull_damage


if __name__ == '__main__':
    pass
    # w = Weapon('速子光矛', WEAPON_SIZES.EXTRA_LARGE, 325, 250, 1400, 70, 150, 0.85,
    #            0)
    #
    # m = WeaponTargetModifier(1.50, 0.50, 0.00, 2.00, 0.00)
    # w.add_modifier(m)
    #
    # w.set_target(TARGET_TYPE.HULL)
    #
    # print(w.modified.avg_damage)
