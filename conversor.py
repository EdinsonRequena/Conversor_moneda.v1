"""
    Conversor Logic
"""

def conversor(type: str, value: int):

    mon = input(f"¿Cuanto {type} quieres cambiar?: ")
    mon = float(mon)
    dolars = mon/value
    dolars = round(dolars, 2)
    dolars = str(dolars)
    res = print(f"Tienes $ {dolars} dólares")

    return res
