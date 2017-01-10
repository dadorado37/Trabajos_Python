# este link es para asegurarse de que un usuario ingrese un numero entero y no un caracter
# https://mail.python.org/pipermail/python-es/2011-September/030635.html
# paseo.py
# comparar con 16 estudiantes opcion 1 montenegro = 6 habitaciones,otras cantidades = 1,2,4,5,101,salento123
import math,os

def uno():
	print "\nEsa opcion es correcta\n"
	print "casa en el norte"
	
	cuartos   = 37500
	servicios = 14000
	patio     = 40000
	garage    = 80000
	
	total = cuartos + servicios + patio + garage
	diferencia_presupuesto = presupuesto - total
	diferencia_carro = diferencia_presupuesto - carro
	
	print "el presupuesto para la casa en el norte es de $ ", total
	print "le quedan $ ", diferencia_presupuesto
	if diferencia_presupuesto >= 400000:
		print "le alcanza para comprar el carro"
		print "le queda un saldo de $ ", diferencia_carro
	else:
		print "no le alcanza para comprar el carro"

def dos():
	print "\nEsa opcion es correcta\n"
	print "casa en el sur"
	
	cuartos   = 52000
	servicios = 24000
	patio     = 15000
	garage    = 70000
	
	total = cuartos + servicios + patio + garage
	diferencia_presupuesto = presupuesto - total
	diferencia_carro = diferencia_presupuesto - carro
	
	print "el presupuesto para la casa en el sur es de $ ", total
	print "le quedan $ ", diferencia_presupuesto
	if diferencia_presupuesto >= 400000:
		print "le alcanza para comprar el carro"
		print "le queda un saldo de $ ", diferencia_carro
	else:
		print "no le alcanza para comprar el carro"


def tres():
	print "\nEsa opcion es correcta\n"
	print "apartamento en el norte"
	
	cuartos   = 50000
	servicios = 14000
	balcon    = 0
	garage    = 160000
	
	total = cuartos + servicios + balcon + garage
	diferencia_presupuesto = presupuesto - total
	diferencia_carro = diferencia_presupuesto - carro
	
	print "el presupuesto para el apartamento en el norte es de $ ", total
	print "le quedan $ ", diferencia_presupuesto
	if diferencia_presupuesto >= 400000:
		print "le alcanza para comprar el carro"
		print "le queda un saldo de $ ", diferencia_carro
	else:
		print "no le alcanza para comprar el carro"

def cuatro():
	print "\nEsa opcion es correcta\n"
	print "apartamento en el sur"
	
	cuartos   = 39000
	servicios = 8000
	balcon    = 0
	garage    = 35000
	
	total = cuartos + servicios + balcon + garage
	diferencia_presupuesto = presupuesto - total
	diferencia_carro = diferencia_presupuesto - carro
	
	print "el presupuesto para el apartamento en el sur es de $ ", total
	print "le quedan $ ", diferencia_presupuesto
	if diferencia_presupuesto >= 400000:
		print "le alcanza para comprar el carro"
		print "le queda un saldo de $ ", diferencia_carro
	else:
		print "no le alcanza para comprar el carro"

	
def cinco():
	print "\nEsa opcion es correcta\n"
	print "finca en jamundi"
	
	cuartos       = 70000
	servicios     = 30000
	zona_verde    = 70000
	zona_parqueo  = 100000
	
	total = cuartos + servicios + zona_verde + zona_parqueo
	diferencia_presupuesto = presupuesto - total
	diferencia_carro = diferencia_presupuesto - carro
	
	print "el presupuesto para la finca en jamundi es de $ ", total
	print "le quedan $ ", diferencia_presupuesto
	if diferencia_presupuesto >= 400000:
		print "le alcanza para comprar el carro"
		print "le queda un saldo de $ ", diferencia_carro
	else:
		print "no le alcanza para comprar el carro"


def seis():
	print "\nEsa opcion es correcta\n"		
	print "finca en el cauca"
	
	cuartos       = 70000
	servicios     = 22500
	zona_verde    = 120000
	cultivos      = 160000
	
	total = cuartos + servicios + zona_verde + cultivos
	diferencia_presupuesto = presupuesto - total
	diferencia_carro = diferencia_presupuesto - carro
	
	print "el presupuesto para la finca en el cauca es de $ ", total
	print "le quedan $ ", diferencia_presupuesto
	if diferencia_presupuesto >= 400000:
		print "le alcanza para comprar el carro"
		print "le queda un saldo de $ ", diferencia_carro
	else:
		print "no le alcanza para comprar el carro"

def salir():
	print "\nGracias por utilizar nuestro servicio\n"
	
	
presupuesto = 500000
carro = 400000
seleccion_menu_uno = 7



while seleccion_menu_uno >= 1 and seleccion_menu_uno > 6:
	
	menu_uno = {1 : uno,  
				2 : dos,   
				3 : tres,
				4 : cuatro,
				5 : cinco,
				6 : seis,
				0 : salir,}

	while seleccion_menu_uno != 4:
					
		while 1:
			
			print "presupuesto de vivienda $ 500000\n"
			print "opcion 1.- Casa en el Norte"
			print "opcion 2.- Casa en el Sur"
			print "opcion 3.- Apartamento en el Norte"
			print "opcion 4.- Apartamento en el Sur"
			print "opcion 5.- Finca en Jamundi"
			print "opcion 6.- Finca en el Cauca"
			print "opcion 0.- salir del programa"
			print "\nescoja una opcion\n\n"
			seleccion_menu_uno = raw_input()
		
			if seleccion_menu_uno.isdigit():
				seleccion_menu_uno = int(seleccion_menu_uno)
				try:
					menu_uno[seleccion_menu_uno]() 
				except:
					print("\nEsa opcion no es correcta")
				break
			else:
				print("\nEsa opcion no es correcta")