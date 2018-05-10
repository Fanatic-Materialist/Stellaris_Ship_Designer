from stellaris_ship_design.constants import UTIL_SIZES
from stellaris_ship_design.object import *

# TODO Develop CSV format for the utilities

class Utility(Equipment):

    def __init__(self, _id, size, cost, power, modifiers):
        if type(size) == str:
            size = UTIL_SIZES(size)
        super().__init__(_id, size, cost, power, modifiers)
