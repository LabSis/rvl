import importlib
import itertools
from os import listdir
from os.path import join, isdir
from input_output.reflective import PackageReflective
from gui.objects_group import ObjectsGroup
from gui.object_button import ObjectButton


class ObjectsLoader:
    """
    Clase para la carga de ObjectsGroup.
    El nombre que se le asigna a cada ObjectsGroup debe estar definido en el diccionario
    CONFIG en la entrada GROUP_NAME, el mismo debe estar en el archivo __init__.py del package.
    """
    path_topology = 'topology'
    config_key = 'CONFIG'
    group_name_key = 'GROUP_NAME'

    def loader(self):
        groups = []
        directories = [d for d in listdir(ObjectsLoader.path_topology)
                            if isdir(join(ObjectsLoader.path_topology, d))
                            and d != "__pycache__"]
        for directory in directories:
            module_name = "%s.%s" % (ObjectsLoader.path_topology, directory)
            module = importlib.import_module(module_name)

            config = getattr(module, ObjectsLoader.config_key)
            group_name = config[ObjectsLoader.group_name_key]

            object_group = ObjectsGroup(group_name)

            reflective = PackageReflective("%s/%s" % (ObjectsLoader.path_topology, directory))
            objects = reflective.get_objects()

            # reflective.get_objects() devuelve una lista por modulo. Por lo que armo una sola lista
            objects = list(itertools.chain.from_iterable(objects))

            position = 0
            for object in objects:
                name = object.get_tool_name()
                path_icon = object.get_url_icon()

                object_group.add_object(ObjectButton(name, path_icon, position))
                position = position + 1

            groups.append(object_group)

        return groups
