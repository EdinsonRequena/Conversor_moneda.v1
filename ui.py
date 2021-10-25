"""
    UI Module
"""

from utils import col, arg, mex, vef

def ui():

    menu = """
        Bienvenido al conversor de monedas

        1 - 'Pesos Colombianos'
        2 - 'Pesos Argentinos'
        3 - 'Pesos Mexicanos'
        4 - 'Bolivares'

        Elige una opción: """

    opcion=input(menu)

    if opcion == '1': res = col("Colombianos", 3722)
    elif opcion == '2': res = arg("Argentinos", 99)
    elif opcion == '3': res = mex("Mexicanos", 0.038)
    elif opcion == '4': res = vef("Bolivares", 0.0003)
    else: res = print('Ingresa una opción correcta por favor')

    return res
