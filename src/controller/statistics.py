#coding:utf-8
"""
Módulo de statistics

"""

import constants

table = {}

def statistics(function):
    def f():
        table[function] += 1
    return f

