from enum import Enum, unique


@unique
class TARGET_TYPE(Enum):
    SHIELD = 'shield'
    ARMOR = 'armor'
    HULL = 'hull'
    NONE = None


@unique
class SHIPT_CLASSES(Enum):
    COVETTE = 'COVETTE'
    DESTOROYER = 'DESTOROYER'
    CRUISER = 'CRUISER'
    BATTLESHIP = 'BATTLESHIP'
    TITAN = 'TITAN'
    COLOSSUS = 'COLOSSUS'
    DEFENSE_PLATFORM = 'DEFENSE_PLATFORM'


@unique
class SHIP_SECTIONS(Enum):
    CORE = 'CORE'
    BOW = 'BOW'
    STERN = 'STERN'
    DEFENSE_PLATFORM = 'DEFENSE_PLATFORM'


@unique
class WEAPON_SIZES(Enum):
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
class UTIL_SIZES(Enum):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    AUXILIARY = 'A'
