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
	cop = input("¿Cuantos pesos colombianos quieres cambiar?: ")
	cop = float(cop)
	cop_dolar = 3722
	dolares=cop/cop_dolar
	dolares=round(dolares, 2)
	dolares=str(dolares)
	print("Tienes $" + dolares + "dólares")
elif opcion=='2':
	ars = input("¿Cuantos pesos Argentinos quieres cambiar?: ")
	ars = float(ars)
	ars_dolar = 99
	dolares=ars/ars_dolar
	dolares=round(dolares, 2)
	dolares=str(dolares)
	print("Tienes $" + dolares + "dólares")
elif opcion=='3':
	mxn = input("¿Cuantos pesos Mexicanos quieres cambiar?: ")
	mxn = float(mxn)
	mxn_dolar = 20
	dolares=mxn/mxn_dolar
	dolares=round(dolares, 2)
	dolares=str(dolares)
	print("Tienes $" + dolares + "dólares")
elif opcion=='4':
	bs = input("¿Cuantos bolivares quieres cambiar?: ")
	bs = float(bs)
	bs_dolar = 4
	dolares=bs/bs_dolar
	dolares=round(dolares, 2)
	dolares=str(dolares)
	print("Tienes $" + dolares + "dólares")
elif opcion=='0':
	menu2="""

	5 - Pesos Colombianos
	6 - Pesos Argentinos
	7 - Pesos Mexicanos
	8 - Bolivares 

	"""
	option=input(menu2)
	if opcion=='5':
		cop = input("¿Cuantos dólares cambiar a pesos colombianos?: ")
		cop = float(cop)
		cop_dolar = 3722
		dolares=cop_dolar/cop
		dolares=round(dolares, 2)
		dolares=str(dolares)
		print("Tienes $" + dolares + "dólares")
	elif opcion=='6':
		ars = input("¿Cuantos dólares cambiar a pesos Argentinos?: ")
		ars = float(ars)
		ars_dolar = 99
		dolares=ars/ars_dolar
		dolares=round(dolares, 2)
		dolares=str(dolares)
		print("Tienes $" + dolares + "dólares")
	elif opcion=='7':
		mxn = input("¿Cuantos dólares cambiar a pesos Mexicanos ?: ")
		mxn = float(mxn)
		mxn_dolar = 20
		dolares=mxn/mxn_dolar
		dolares=round(dolares, 2)
		dolares=str(dolares)
		print("Tienes $" + dolares + "dólares")
	elif opcion=='8':
		bs = input("¿Cuantos dólares cambiar a bolivares?: ")
		bs = float(bs)
		bs_dolar = 4
		dolares=bs_dolar/bs
		dolares=round(dolares, 2)
		dolares=str(dolares)
		print("Tienes $" + dolares + "dólares")
	else:
		print('Ingresa una opción correcta por favor')

else:
	print('Ingresa una opción correcta por favor')


