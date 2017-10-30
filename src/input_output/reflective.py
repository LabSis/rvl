# coding: utf-8
import sys
import inspect
from os import listdir
from os.path import isfile, join
import importlib


def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])

    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


class ModuleReflective():
    """
    Description:
        Importa solo un módulo
    """
    def __init__(self, module):
        self.module = module.replace('/', '.')

    def get_classes(self):
        classes = []
        if self.module is not None:
            mod = sys.modules[self.module]

            for name, obj in inspect.getmembers(mod):
                if inspect.isclass(obj):
                    classes.append(name)
        return classes

    def get_objects(self):
        self.classes = self.get_classes()
        objects = []
        for clase in self.classes:
            try:
                obj = my_import(self.module + "." + clase)()
            except:
                obj = None
            if obj is not None:
                objects.append(obj)
        return objects


class PackageReflective():
    """
    Description:
        Importa e instancia las clases de un paquete.
        Un paquete está conformado por muchos módulos y un módulo puede
        contener muchas clases.
    """

    def __init__(self, package):
        self.package = package
        self.modules = []
        self._import_package()

    def _import_package(self):
        files = self.get_files_from_package()
        package_dot = self.package.replace("/", ".")
        for f in files:
            module = f
            # Quito la extensión.
            module = module[0: len(module) - 3]
            importlib.import_module(package_dot + "." + module)
            self.modules.append(module)

    def get_files_from_package(self):
        """
        Description:
            Retorna los archivos Python de un paquete (o directorio)
            exceptuando al archivo __init__.py
        """
        only_files = [f for f in listdir(self.package)
                if isfile(join(self.package, f)) and f != "__init__.py"
                and f.endswith(".py")]
        return only_files

    def get_objects(self):
        modules = self.modules        
        objects = []
        for module in modules:
            path = self.package + "/" + module
            objeto = ModuleReflective(path).get_objects()
            if(objeto.__len__() != 0):
                objects.append(objeto)
        return objects