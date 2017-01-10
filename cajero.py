# cajero:, decir si era tarjeta credito o debito y los valores que
# podida retirar 120000,250000,380000,520000,750000,890000
# y que identificara los billetes de 1000 3000 30000 150000

import math,os

def uno():
	print "\nEsa opcion es correcta\n"
	
	billete_1000    = 1000
	billete_3000    = 3000
	billete_30000   = 30000
	billete_150000  = 150000
	
	cantidad = 120000
	
	retiro = cantidad / billete_30000
	
	print "su retiro es de $", cantidad
	print "su retiro es de ", retiro, "billetes de $ ", billete_30000
	
def dos():
	print "\nEsa opcion es correcta\n"
	
	billete_1000    = 1000
	billete_3000    = 3000
	billete_30000   = 30000
	billete_150000  = 150000
	
	cantidad = 250000
	retiro = cantidad / billete_150000
	retiro_entero = math.ceil(retiro)
	retiro_entero = int(retiro_entero)
	
	retiro_parcial_mayor = cantidad - billete_150000 
	retiro_parcial_menor = retiro_parcial_mayor / billete_30000
	retiro_parcial_menor_entero = math.ceil(retiro_parcial_menor)
	retiro_parcial_menor_entero = int(retiro_parcial_menor_entero)
	
	retiro_diferencia_mayor = cantidad - retiro_parcial_mayor
	
	operacion_complemento = retiro_diferencia_mayor + (billete_30000 * retiro_parcial_menor_entero)
	
	retiro_sencilla = cantidad - operacion_complemento
	retiro_parcial_sencilla = retiro_sencilla / billete_3000
	retiro_sencilla_entero = math.ceil(retiro_parcial_sencilla)
	retiro_sencilla_entero = int(retiro_sencilla_entero)
	
	retiro_diferencia_sencilla = retiro_sencilla - (billete_3000 * retiro_sencilla_entero)
	comprobar_cantidad_sencilla = retiro_diferencia_sencilla / billete_1000
	
	
	
	print "su retiro es de $", cantidad
	print "su retiro es de ", retiro_entero, "billete de $ ", billete_150000
	print "su retiro es de ", retiro_parcial_menor_entero, "billetes de $ ", billete_30000
	print "su retiro es de ", retiro_sencilla_entero, "billetes de $ ", billete_3000
	print "su retiro es de ", comprobar_cantidad_sencilla, "billetes de $ ", billete_1000
		
def tres():
	print "\nEsa opcion es correcta\n"		
	
	billete_1000    = 1000
	billete_3000    = 3000
	billete_30000   = 30000
	billete_150000  = 150000
	
	cantidad = 380000
	retiro = cantidad / billete_150000
	retiro_entero = math.ceil(retiro)
	retiro_entero = int(retiro_entero)
	
	retiro_parcial_mayor = cantidad - (billete_150000 * retiro_entero)
	retiro_parcial_menor = retiro_parcial_mayor / billete_30000
	retiro_parcial_menor_entero = math.ceil(retiro_parcial_menor)
	retiro_parcial_menor_entero = int(retiro_parcial_menor_entero)
	
	retiro_diferencia_mayor = cantidad - retiro_parcial_mayor
	
	operacion_complemento = retiro_diferencia_mayor + (billete_30000 * retiro_parcial_menor_entero)
	
	retiro_sencilla = cantidad - operacion_complemento
	retiro_parcial_sencilla = retiro_sencilla / billete_3000
	retiro_sencilla_entero = math.ceil(retiro_parcial_sencilla)
	retiro_sencilla_entero = int(retiro_sencilla_entero)
	
	retiro_diferencia_sencilla = retiro_sencilla - (billete_3000 * retiro_sencilla_entero)
	comprobar_cantidad_sencilla = retiro_diferencia_sencilla / billete_1000
	
	print "su retiro es de $", cantidad
	print "su retiro es de ", retiro_entero, "billete de $ ", billete_150000
	print "su retiro es de ", retiro_parcial_menor_entero, "billetes de $ ", billete_30000
	print "su retiro es de ", retiro_sencilla_entero, "billetes de $ ", billete_3000
	print "su retiro es de ", comprobar_cantidad_sencilla, "billetes de $ ", billete_1000

	
def cuatro():
	print "\nEsa opcion es correcta\n"		
	
	billete_1000    = 1000
	billete_3000    = 3000
	billete_30000   = 30000
	billete_150000  = 150000
	
	cantidad = 520000
	
	retiro = cantidad / billete_150000
	retiro_entero = math.ceil(retiro)
	retiro_entero = int(retiro_entero)
	
	retiro_parcial_mayor = cantidad - (billete_150000 * retiro_entero)
	retiro_parcial_menor = retiro_parcial_mayor / billete_30000
	retiro_parcial_menor_entero = math.ceil(retiro_parcial_menor)
	retiro_parcial_menor_entero = int(retiro_parcial_menor_entero)
	
	retiro_diferencia_mayor = cantidad - retiro_parcial_mayor
	
	operacion_complemento = retiro_diferencia_mayor + (billete_30000 * retiro_parcial_menor_entero)
	
	retiro_sencilla = cantidad - operacion_complemento
	retiro_parcial_sencilla = retiro_sencilla / billete_3000
	retiro_sencilla_entero = math.ceil(retiro_parcial_sencilla)
	retiro_sencilla_entero = int(retiro_sencilla_entero)
	
	retiro_diferencia_sencilla = retiro_sencilla - (billete_3000 * retiro_sencilla_entero)
	comprobar_cantidad_sencilla = retiro_diferencia_sencilla / billete_1000
	
	print "su retiro es de $", cantidad
	print "su retiro es de ", retiro_entero, "billete de $ ", billete_150000
	print "su retiro es de ", retiro_parcial_menor_entero, "billetes de $ ", billete_30000
	print "su retiro es de ", retiro_sencilla_entero, "billetes de $ ", billete_3000
	print "su retiro es de ", comprobar_cantidad_sencilla, "billetes de $ ", billete_1000
	
def cinco():
	print "\nEsa opcion es correcta\n"		
	
	billete_1000    = 1000
	billete_3000    = 3000
	billete_30000   = 30000
	billete_150000  = 150000
	
	cantidad = 750000
	
	retiro = cantidad / billete_150000
	
	print "su retiro es de $", cantidad
	print "su retiro es de ", retiro, "billetes de $ ", billete_150000

	
def seis():
	print "\nEsa opcion es correcta\n"		
	
	billete_1000    = 1000
	billete_3000    = 3000
	billete_30000   = 30000
	billete_150000  = 150000
	
	cantidad = 890000
	
	retiro = cantidad / billete_150000
	retiro_entero = math.ceil(retiro)
	retiro_entero = int(retiro_entero)
	
	retiro_parcial_mayor = cantidad - (billete_150000 * retiro_entero)
	retiro_parcial_menor = retiro_parcial_mayor / billete_30000
	retiro_parcial_menor_entero = math.ceil(retiro_parcial_menor)
	retiro_parcial_menor_entero = int(retiro_parcial_menor_entero)
	
	retiro_diferencia_mayor = cantidad - retiro_parcial_mayor
	
	operacion_complemento = retiro_diferencia_mayor + (billete_30000 * retiro_parcial_menor_entero)
	
	retiro_sencilla = cantidad - operacion_complemento
	retiro_parcial_sencilla = retiro_sencilla / billete_3000
	retiro_sencilla_entero = math.ceil(retiro_parcial_sencilla)
	retiro_sencilla_entero = int(retiro_sencilla_entero)
	
	retiro_diferencia_sencilla = retiro_sencilla - (billete_3000 * retiro_sencilla_entero)
	comprobar_cantidad_sencilla = retiro_diferencia_sencilla / billete_1000
	
	print "su retiro es de $", cantidad
	print "su retiro es de ", retiro_entero, "billete de $ ", billete_150000
	print "su retiro es de ", retiro_parcial_menor_entero, "billetes de $ ", billete_30000
	print "su retiro es de ", retiro_sencilla_entero, "billetes de $ ", billete_3000
	print "su retiro es de ", comprobar_cantidad_sencilla, "billetes de $ ", billete_1000

def salir():
	print "\nGracias por utilizar nuestro servicio\n"
clave = 0
while clave != 123:
	while 1:
		print "digite la clave"
		clave = raw_input()
		if clave.isdigit():
			clave = int(clave)
			break	
		break

print "que tipo de cuenta"
print "1. debito"
print "2. credito"

opcion = 0
while opcion != 1 and opcion != 2:
	while 1:
		print "digite el tipo de cuenta"
		opcion = raw_input()
		if opcion.isdigit():
			opcion = int(opcion) 
			break	
		break
		
if opcion == 1:
	seleccion_menu_uno = 7	
	while seleccion_menu_uno >= 1 and seleccion_menu_uno > 6:
	
		menu_uno = {1 : uno,  
					2 : dos,   
					3 : tres,
					4 : cuatro,
					5 : cinco,
					6 : seis,
					0 : salir,}
		while 1:
	
			print "cuanto desea retirar\n\n"
		
			print "opcion 1.- 120000"
			print "opcion 2.- 250000"
			print "opcion 3.- 380000"
			print "opcion 4.- 520000"
			print "opcion 5.- 750000"
			print "opcion 6.- 890000"
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

if opcion == 2:
	print "no hay credito"