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


class Modifier:
    suitable_type = Object

    def modify(self, obj: suitable_type):
        # a callable method that takes an object to modify
        pass

    desc = ''  # modifier description displayed to user

    def __init__(self, suitable_type: type = Object,
                 modify: callable = None,
                 desc: str = '(Modifier without description)'):
        self.suitable_type = suitable_type
        if modify is not None:
            self.modify = modify
        self.desc = desc

    def __str__(self):
        return '<%s> %s' % (type(self).__name__, self.desc)
