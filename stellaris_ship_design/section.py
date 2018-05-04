from stellaris_ship_design.object import *
from stellaris_ship_design.constants import *


class Section(Object):
    ship_type = SHIP_CLASSES.

    def __index__(self, id, modifiers=None):
        super().__init__(id, modifiers)
