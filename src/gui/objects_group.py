class ObjectsGroup:

    def __init__(self, label, list=None):
        self.label = label
        self.list = list if list else []

    def add_object(self, button):
        self.list.append(button)
