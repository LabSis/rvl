# coding: utf-8
from gui.objects_group import ObjectsGroup
from gui.object_button import ObjectButton


class ObjectsLoader():

    def loader_objects_groups(self):
        list = []
        one_group = ObjectsGroup('Grupo 1')
        a_button = ObjectButton("A", "/sdfa/", 0)
        b_button = ObjectButton("B", "/sdfe/", 1)
        one_group.add_object(b_button)
        one_group.add_object(a_button)
        list.append(one_group)

        two_group = ObjectsGroup('Grupo 2')
        b_button = ObjectButton("B", "/sdfe/", 1)
        two_group.add_object(b_button)
        list.append(two_group)
        return list
