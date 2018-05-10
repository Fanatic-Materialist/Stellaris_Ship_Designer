from stellaris_ship_design.object import *
from stellaris_ship_design.constants import *


class Section(Object):
    ship_type = SHIP_CLASSES.NONE
    section_type = SHIP_SECTIONS.NONE
    slots = []

    def __init__(self, _id, ship_type, section_type, slots, modifiers=None):
        super().__init__(_id, modifiers)
        self.ship_type = ship_type
        self.section_type = section_type
        self.slots = slots

    class Slot(Object):
        equipment = None
        type_ = SLOT_TYPES.NONE
        size = EQUIPMENT_SIZES.NONE

        def __init__(self, id_, slot_type: SLOT_TYPES, slot_size: EQUIPMENT_SIZES,
                     equipment=None, modifiers=None):
            super().__init__(id_, modifiers)
            self.type_ = slot_type
            self.size = slot_size
            self.equipment = equipment

        def add_item(self, equipment: Equipment):
            if type(equipment).__name__ == self.type_.value:  # TODO Try to use another method to determine the typea
                if equipment.size == self.size:
                    self.equipment = equipment
