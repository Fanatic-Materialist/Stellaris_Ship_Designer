from enum import Enum, unique

@unique
class TARGET_TYPE(Enum):
    SHIELD = 'SHIELD'
    ARMOR = 'ARMOR'
    HULL = 'HULL'
    NONE = None


@unique
class SHIP_CLASSES(Enum):
    CORVETTE = 'CORVETTE'
    DESTROYER = 'DESTROYER'
    CRUISER = 'CRUISER'
    BATTLESHIP = 'BATTLESHIP'
    TITAN = 'TITAN'
    COLOSSUS = 'COLOSSUS'
    DEFENSE_PLATFORM = 'DEFENSE_PLATFORM'
    NONE = None


@unique
class SHIP_SECTIONS(Enum):
    CORE = 'CORE'
    BOW = 'BOW'
    STERN = 'STERN'
    DEFENSE_PLATFORM = 'DEFENSE_PLATFORM'
    NONE = None


@unique
class EQUIPMENT_SIZES(Enum):
    pass  # The inheritance of a enum with defined members is not allowed in Python


@unique
class SLOT_TYPES(Enum):
    WEAPON = 'Weapon'
    UTILITY = 'Utility'
    NONE = None


@unique
class WEAPON_SIZES(EQUIPMENT_SIZES):
    NONE = None
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'X'
    POINT_DEFENSE = 'P'
    GUIDED = 'G'
    HANGAR = 'H'
    # AUXILIARY = 'A'
    # CORE = 'C'
    TITAN = 'T'
    # WORLD_DESTROYER = 'W'


@unique
class UTIL_SIZES(EQUIPMENT_SIZES):
    NONE = None
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    AUXILIARY = 'A'
