# este link es para asegurarse de que un usuario ingrese un numero entero y no un caracter
# https://mail.python.org/pipermail/python-es/2011-September/030635.html

# empresa_arranque_gana.py
seleccion_menu_uno = 5
# define the function blocks
def uno():
	print("\nEsa opcion es correcta\n")
	print "cliente categoria 1"
	print "nombre del cliente: ", nombre_cliente
	print "la cantidad de escobas es: ", cantidad_escobas
	print "el costo total de las escobas es: ", costo_total_escobas
	print "la cantidad de recogedores es: ", cantidad_recogedores
	print "el costo total de los recogedores es: ", costo_total_recogedores
	print "la cantidad de aromatizantes es: ", cantidad_aromatizantes
	print "el costo total de los aromatizantes es: ", costo_total_aromatizantes
	print "la cantidad total de productos es: ", cantidad_total_productos
	print "el subtotal de la compra es: ", subtotal_compra
	descuento_compra = (subtotal_compra * 5) / 100
	total_compra = subtotal_compra - descuento_compra
	print "el total de compra es: ", total_compra
	
def dos():
	print("\nEsa opcion es correcta\n")
	print "cliente categoria 2"
	print "nombre del cliente: ", nombre_cliente
	print "la cantidad de escobas es: ", cantidad_escobas
	print "el costo total de las escobas es: ", costo_total_escobas
	print "la cantidad de recogedores es: ", cantidad_recogedores
	print "el costo total de los recogedores es: ", costo_total_recogedores
	print "la cantidad de aromatizantes es: ", cantidad_aromatizantes
	print "el costo total de los aromatizantes es: ", costo_total_aromatizantes
	print "la cantidad total de productos es: ", cantidad_total_productos
	print "el subtotal de la compra es: ", subtotal_compra
	descuento_compra = (subtotal_compra * 8) / 100
	total_compra = subtotal_compra - descuento_compra
	print "el total de compra es: ", total_compra
	
	
def tres():
	print("\nEsa opcion es correcta\n")
	print "cliente categoria 3"
	print "nombre del cliente: ", nombre_cliente
	print "la cantidad de escobas es: ", cantidad_escobas
	print "el costo total de las escobas es: ", costo_total_escobas
	print "la cantidad de recogedores es: ", cantidad_recogedores
	print "el costo total de los recogedores es: ", costo_total_recogedores
	print "la cantidad de aromatizantes es: ", cantidad_aromatizantes
	print "el costo total de los aromatizantes es: ", costo_total_aromatizantes
	print "la cantidad total de productos es: ", cantidad_total_productos
	print "el subtotal de la compra es: ", subtotal_compra
	descuento_compra = (subtotal_compra * 12) / 100
	total_compra = subtotal_compra - descuento_compra
	print "el total de compra es: ", total_compra
	
	
def cuatro():
	print("\nEsa opcion es correcta\n")
	print "cliente categoria 4"
	print "nombre del cliente: ", nombre_cliente
	print "la cantidad de escobas es: ", cantidad_escobas
	print "el costo total de las escobas es: ", costo_total_escobas
	print "la cantidad de recogedores es: ", cantidad_recogedores
	print "el costo total de los recogedores es: ", costo_total_recogedores
	print "la cantidad de aromatizantes es: ", cantidad_aromatizantes
	print "el costo total de los aromatizantes es: ", costo_total_aromatizantes
	print "la cantidad total de productos es: ", cantidad_total_productos
	print "el subtotal de la compra es: ", subtotal_compra
	descuento_compra = (subtotal_compra * 15) / 100
	total_compra = subtotal_compra - descuento_compra
	print "el total de compra es: ", total_compra
	

costo_escoba = 5000
costo_recogedor = 2000
costo_aromatizante = 3000
	
	
print "cual es su nombre"
nombre_cliente = raw_input()

print "\ndesea comprar escobas S / N "
desea_comprar_escobas = raw_input()

while (desea_comprar_escobas != 's') or (desea_comprar_escobas != 'S') or (desea_comprar_escobas != 'n') or (desea_comprar_escobas != 'N'):
	if (desea_comprar_escobas == 's') or (desea_comprar_escobas == 'S') or (desea_comprar_escobas != 'n') or (desea_comprar_escobas != 'N'):
		break
	else:
		print "\ningreso la opcion incorrecta"
		print "desea comprar escobas S / N "
		desea_comprar_escobas = raw_input()
		
print "\nok ingreso la opcion correcta"		

print "\ndesea comprar recogedores S / N "
desea_comprar_recogedores = raw_input()

while (desea_comprar_recogedores != 's')or(desea_comprar_recogedores != 'S') or (desea_comprar_recogedores != 'n')or(desea_comprar_recogedores != 'N'):
	if (desea_comprar_recogedores == 's')or(desea_comprar_recogedores == 'S') or (desea_comprar_recogedores != 'n')or(desea_comprar_recogedores != 'N'):
		break
	else:
		print "\ningreso la opcion incorrecta"
		print "desea comprar recogedores S / N "
		desea_comprar_recogedores = raw_input()
		
print "\nok ingreso la opcion correcta"	

print "\ndesea comprar aromatizantes S / N "
desea_comprar_aromatizantes = raw_input()

while (desea_comprar_aromatizantes != 's')or(desea_comprar_aromatizantes != 'S') or (desea_comprar_aromatizantes != 'n')or(desea_comprar_aromatizantes != 'N'):
	if (desea_comprar_aromatizantes == 's')or(desea_comprar_aromatizantes == 'S') or (desea_comprar_aromatizantes != 'n')or(desea_comprar_aromatizantes != 'N'):
		break
	else:
		print "\ningreso la opcion incorrecta"
		print "desea comprar aromatizantes S / N "
		desea_comprar_aromatizantes = raw_input()
		
print "\nok ingreso la opcion correcta\n"	

if (desea_comprar_escobas == 's') or (desea_comprar_escobas == 'S'):
	while 1:
		print "digite la cantidad de escobas"
		cantidad_escobas = raw_input()
		if cantidad_escobas.isdigit():
			cantidad_escobas = int(cantidad_escobas)
			break
elif (desea_comprar_escobas == 'n') or (desea_comprar_escobas == 'N'):
	cantidad_escobas = 0
			
if (desea_comprar_recogedores == 's')or(desea_comprar_recogedores == 'S'):
	while 1:
		print "digite la cantidad de recogedores"
		cantidad_recogedores = raw_input()
		if cantidad_recogedores.isdigit():
			cantidad_recogedores = int(cantidad_recogedores)
			break
elif (desea_comprar_recogedores == 'n') or (desea_comprar_recogedores == 'N'):
	cantidad_recogedores = 0
			
if (desea_comprar_aromatizantes == 's') or (desea_comprar_aromatizantes == 'S'):
	while 1:
		print "digite la cantidad de aromatizantes"
		cantidad_aromatizantes = raw_input()
		if cantidad_aromatizantes.isdigit():
			cantidad_aromatizantes = int(cantidad_aromatizantes)
			break
elif (desea_comprar_aromatizantes == 'n') or (desea_comprar_aromatizantes == 'N'):
	cantidad_aromatizantes = 0
	
	
costo_total_escobas = costo_escoba * cantidad_escobas
costo_total_recogedores = costo_recogedor * cantidad_recogedores
costo_total_aromatizantes = costo_aromatizante * cantidad_aromatizantes

cantidad_total_productos = cantidad_escobas + cantidad_recogedores + cantidad_aromatizantes

subtotal_compra = costo_total_escobas + costo_total_recogedores + costo_total_aromatizantes
			
while seleccion_menu_uno > 4:
	# map the inputs to the function blocks
	menu_uno = {1 : uno,  
	            2 : dos,   
				3 : tres,
				4 : cuatro,}
	while 1:
		print("opcion 1.- cliente categoria 1 se le descuenta el 5%")
		print("opcion 2.- cliente categoria 2 se le descuenta el 8%")
		print("opcion 3.- cliente categoria 3 se le descuenta el 12%")
		print("opcion 4.- cliente categoria 4 se le descuenta el 15%")
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