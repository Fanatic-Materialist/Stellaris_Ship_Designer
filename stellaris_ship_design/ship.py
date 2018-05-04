from stellaris_ship_design.constants import *
from stellaris_ship_design.object import *

class Ship(Object):
    class_ = SHIP_CLASSES.CORVETTE
    sections = {}
    cmd_pts = 0
    cost = 0
    build_time = 0
    hull = 0
    evasion = 0.0
    speed = 0

    def __init__(self, id, class_, sections, cmd_pts, cost, build_time, hull,
                 evasion, speed, modfiers = None):
        super().__init__(id, modfiers)
        self.class_ = class_
        self.sections = sections
        self.cmd_pts = cmd_pts
        self.cost = cost
        self.build_time = build_time
        self.hull = hull
        self.evasion = evasion
        self.speed = speed