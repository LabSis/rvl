# coding:utf-8
"""
Módulo que prueba la clase PropReader del módulo input_output.prop_reader.
"""
import configparser
import unittest


class TestConfigFile(unittest.TestCase):
    def setUp(self):
        self.config = config_file.ConfigFile('configuracion/prop.ini')        

    def test_get_atributo(self):
        self.assertEqual('2', self.config.get_value('padding_izq_imagen_dispositivo', 'IMAGENESDISPOSITIVOS'))
        self.assertRaises(configparser.NoSectionError, self.config.get_value, 'basket', 'deporte');
        self.assertRaises(configparser.NoOptionError, self.config.get_value, 'basket', 'IMAGENESDISPOSITIVOS');

if __name__ == "__main__":
    import sys
    sys.path.append(".")
    import input_output.config_file as config_file
    unittest.main()
