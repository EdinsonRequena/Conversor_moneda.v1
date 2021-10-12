pesos = input("¿Cuantos pesos colombianos quieres cambiar?: ")
pesos = float(pesos)
pesos_dolar = 3753
dolares=pesos/pesos_dolar
dolares=round(dolares, 2)
dolares=str(dolares)
print("Tienes $" + dolares + "dólares")

bolivares=input("¿Cuantos bolivares quieres cambiar?: ")
bolivares=float(bolivares)
bolivares_dolar=5.38
dolareb=bolivares/bolivares_dolar
dolareb=round(dolareb, 2)
dolareb=str(dolareb)
print("Tienes $" + dolareb + "dólares")