def conversor(tipo_moneda, valor_dolar):
    mon = input("¿Cuanto " + tipo_moneda + " quieres cambiar?: ")
    mon = float(mon)
    dolares = mon/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")


menu=""" 
	Bienvenido al conversor de monedas

	1 - Pesos Colombianos
	2 - Pesos Argentinos
	3 - Pesos Mexicanos
	4 - Bolivares 
	0 - Invertir conversor

	Elige una opción: """

opcion=input(menu)

if opcion=='1':
	conversor("Colombianos", 3722)
elif opcion=='2':
	conversor("Argentinos", 99)
elif opcion=='3':
	conversor("Mexicanos", 20)
elif opcion=='4':
	conversor("Venezolanos", 4.12)
elif opcion=='0':
	menu2="""

	5 - Pesos Colombianos
	6 - Pesos Argentinos
	7 - Pesos Mexicanos
	8 - Bolivares 

	"""
	option=input(menu2)
	if opcion=='5':
		conversor("Colombianos", 3722)
	elif opcion=='6':
		conversor("Argentinos", 99)
	elif opcion=='7':
		conversor("Mexicanos", 20)
	elif opcion=='8':
		conversor("Venezolanos", 4.12)
	else:
		print('Ingresa una opción correcta por favor')

else:
	print('Ingresa una opción correcta por favor')


