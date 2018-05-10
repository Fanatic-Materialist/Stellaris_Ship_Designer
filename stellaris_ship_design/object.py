from stellaris_ship_design.local import local


class Object:
    id = ''
    modifiers = []
    children = []
    parent = None

    def __init__(self, id, modifiers=None, children=None, parent=None):
        self.id = id
        if modifiers is None:
            self.modifiers = []
        else:
            self.modifiers = modifiers
        if children is None:
            self.children = []
        else:
            self.children = children
        self.parent = parent

    @property
    def modified(self):
        from copy import deepcopy
        modified_obj = deepcopy(self)
        # iterate all modifiers assigned to this object
        for modifier in self.get_modifiers():
            # if the modifier is suitable for this object
            if issubclass(type(self), modifier.suitable_type):
                modifier.modify(modified_obj)
        return modified_obj

    def get_modifiers(self):
        return Object._get_modifiers_recursive(self, type(self))

    @staticmethod
    def _get_modifiers_recursive(obj, obj_type: type):
        modifiers = []
        if obj.parent is not None:
            modifiers += Object._get_modifiers_recursive(obj.parent, obj_type)
        for modifier in obj.modifiers:
            if issubclass(obj_type, modifier.suitable_type):
                modifiers.append(modifier)
        return modifiers

    def add_modifier(self, modifier):
        # add modifier to its own modifier list
        self.modifiers.append(modifier)
        # # add modifier to all its children objects
        # for child in self.children:
        #     child.add_modifier(modifier)

    def __str__(self):
        return '<%s> %s' % (type(self).__name__, local(self.id))


class Modifier:
    suitable_type = Object
    desc = ''  # modifier description displayed to user

    def modify(self, obj: suitable_type):
        # a callable method that takes an object to modify
        pass


    def __init__(self, suitable_type: type = Object,
                 modify: callable = None,
                 desc: str = '(Modifier without description)'):
        self.suitable_type = suitable_type
        if modify is not None:
            self.modify = modify
        self.desc = desc

    def __str__(self):
        return '<%s> %s' % (type(self).__name__, self.desc)


class Equipment(Object):  # Abstract super class for Weapons and Utilities
    size = None
    cost = 0.0
    power = 0.0

    # TODO

    def __init__(self, _id, size, cost, power, modifiers=None):
        super().__init__(_id, modifiers)
        if type(size) == str:
            pass  # The classes that extends Equipment should accept 'str' type
            # as the input of parameter 'size', and convert it to a constant
        self.size = size
        self.cost = cost
        self.power = power
