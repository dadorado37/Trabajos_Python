# este link es para asegurarse de que un usuario ingrese un numero entero y no un caracter
# https://mail.python.org/pipermail/python-es/2011-September/030635.html
# paseo.py
# comparar con 16 estudiantes opcion 1 montenegro = 6 habitaciones,otras cantidades = 1,2,4,5,101,salento123
import math,os

def uno():
	print "\nEsa opcion es correcta\n"
	print "Paseo en Montenegro"
	
	limite_estudiantes = 423	

	while 1:
		print "digite la cantidad de estudiantes"
		cantidad_estudiantes = raw_input()
		if cantidad_estudiantes.isdigit():
			cantidad_estudiantes = int(cantidad_estudiantes)
			break	

	while (cantidad_estudiantes > limite_estudiantes ):
		print "digite la cantidad de estudiantes"
		cantidad_estudiantes = input()
		

	if (cantidad_estudiantes <= 300):
		print "si se hace el paseo\n"	
		cupo_bus = 38
		cantidad_buses = (float(cantidad_estudiantes) / float(cupo_bus))
		cantidad_buses_aproximada = math.ceil(cantidad_buses)
		cantidad_buses_aproximada = int(cantidad_buses_aproximada)
	
		cantidad_maxima_habitacion_1_piso = 3
		cantidad_maxima_habitacion_2_piso = 4
		cantidad_maxima_habitacion_1_piso_hospedaje = 3
		cantidad_personas_1_piso = 100
		cantidad_personas_2_piso = 150
		cantidad_personas_maximo_montenegro = cantidad_personas_1_piso + cantidad_personas_2_piso
		
		cantidad_estudiantes_menor_100 = cantidad_personas_1_piso - cantidad_estudiantes
		diferencia_limite_piso_1 = cantidad_personas_1_piso - cantidad_estudiantes_menor_100
	
		cantidad_habitaciones_menor_limite_piso_1 = (float(diferencia_limite_piso_1) / float(cantidad_maxima_habitacion_1_piso))
		cantidad_habitaciones_menor_limite_piso_1_aproximada = math.ceil(cantidad_habitaciones_menor_limite_piso_1)
		cantidad_habitaciones_menor_limite_piso_1_aproximada = int(cantidad_habitaciones_menor_limite_piso_1_aproximada)
	
		cantidad_habitaciones_1_piso_limite = ((cantidad_personas_1_piso) / (cantidad_maxima_habitacion_1_piso))
		cantidad_habitaciones_2_piso_limite = ((cantidad_personas_2_piso) / (cantidad_maxima_habitacion_2_piso))
	
		cantidad_estudiantes_menor_3 = (float(cantidad_estudiantes) / float(cantidad_maxima_habitacion_1_piso))
		cantidad_estudiantes_menor_3_aproximada = math.ceil(cantidad_estudiantes_menor_3)
		cantidad_estudiantes_menor_3_aproximada = int(cantidad_estudiantes_menor_3_aproximada)
	
		diferencia_capacidad_entre_pisos = cantidad_estudiantes - cantidad_personas_1_piso
		habitaciones_faltantes = (float(diferencia_capacidad_entre_pisos) / float(cantidad_maxima_habitacion_2_piso))
		habitaciones_faltantes_aproximadas = math.ceil(habitaciones_faltantes)
		habitaciones_faltantes_aproximadas = int(habitaciones_faltantes_aproximadas)
	
		cantidad_personas_hospedaje_alterno = cantidad_estudiantes - (cantidad_personas_1_piso + cantidad_personas_2_piso)
		cantidad_habitaciones_1_hospedaje = (float(cantidad_personas_hospedaje_alterno) / float(cantidad_maxima_habitacion_1_piso_hospedaje))
		cantidad_habitaciones_1_hospedaje_aproximada = math.ceil(cantidad_habitaciones_1_hospedaje)
		cantidad_habitaciones_1_hospedaje_aproximada = int(cantidad_habitaciones_1_hospedaje_aproximada)
	
		
		if (cantidad_estudiantes <= 300):
			print "cantidad de buses que necesita: ", cantidad_buses_aproximada
		if (cantidad_estudiantes > 0)and(cantidad_estudiantes < cantidad_maxima_habitacion_1_piso):
			print "cantidad de habitaciones que necesita:", cantidad_estudiantes_menor_3_aproximada 
		if (cantidad_estudiantes >= cantidad_maxima_habitacion_1_piso)and(cantidad_estudiantes <= cantidad_personas_1_piso): 
			print "se necesitan", cantidad_habitaciones_menor_limite_piso_1_aproximada, "habitaciones en el primer piso"
		if (cantidad_estudiantes > cantidad_personas_1_piso)and(cantidad_estudiantes <= cantidad_personas_maximo_montenegro):
			print "se necesitan" , cantidad_habitaciones_1_piso_limite, "habitaciones en el primer piso"
			print "se necesitan" , habitaciones_faltantes_aproximadas, "habitaciones en el segundo piso"			
		if cantidad_personas_hospedaje_alterno < 0:
			print "no necesita hospedaje alterno"
		else:
			print "se necesitan", cantidad_habitaciones_1_piso_limite, "habitaciones en el primer piso"
			print "se necesitan", cantidad_habitaciones_2_piso_limite, "habitaciones en el segundo piso"
			print "la cantidad de personas en el hospedaje alterno es de: ", cantidad_personas_hospedaje_alterno
			print "se necesitan", cantidad_habitaciones_1_hospedaje_aproximada, "habitaciones en el primer piso del hospedaje alterno"
	else:
		print "no se hace el paseo"
	
def dos():
	print "\nEsa opcion es correcta\n"
	print "Paseo en Salento"
	limite_estudiantes = 423	

	while 1:
		print "digite la cantidad de estudiantes"
		cantidad_estudiantes = raw_input()
		if cantidad_estudiantes.isdigit():
			cantidad_estudiantes = int(cantidad_estudiantes)
			break	

	while (cantidad_estudiantes > limite_estudiantes ):
		print "digite la cantidad de estudiantes"
		cantidad_estudiantes = input()
		

	if (cantidad_estudiantes <= 232):
		print "si se hace el paseo\n"	
		cupo_bus = 38
		cantidad_buses = (float(cantidad_estudiantes) / float(cupo_bus))
		cantidad_buses_aproximada = math.ceil(cantidad_buses)
		cantidad_buses_aproximada = int(cantidad_buses_aproximada)
	
		cantidad_maxima_habitacion_1_piso = 3
		cantidad_maxima_habitacion_2_piso = 4
		cantidad_maxima_habitacion_1_piso_hospedaje = 3
		cantidad_personas_1_piso = 122
		cantidad_personas_2_piso = 80
		cantidad_personas_maximo_salento = cantidad_personas_1_piso + cantidad_personas_2_piso
		
		cantidad_estudiantes_menor_122 = cantidad_personas_1_piso - cantidad_estudiantes
		diferencia_limite_piso_1 = cantidad_personas_1_piso - cantidad_estudiantes_menor_122
	
		cantidad_habitaciones_menor_limite_piso_1 = (float(diferencia_limite_piso_1) / float(cantidad_maxima_habitacion_1_piso))
		cantidad_habitaciones_menor_limite_piso_1_aproximada = math.ceil(cantidad_habitaciones_menor_limite_piso_1)
		cantidad_habitaciones_menor_limite_piso_1_aproximada = int(cantidad_habitaciones_menor_limite_piso_1_aproximada)
	
		cantidad_habitaciones_1_piso_limite = ((cantidad_personas_1_piso) / (cantidad_maxima_habitacion_1_piso))
		cantidad_habitaciones_2_piso_limite = ((cantidad_personas_2_piso) / (cantidad_maxima_habitacion_2_piso))
	
		cantidad_estudiantes_menor_3 = (float(cantidad_estudiantes) / float(cantidad_maxima_habitacion_1_piso))
		cantidad_estudiantes_menor_3_aproximada = math.ceil(cantidad_estudiantes_menor_3)
		cantidad_estudiantes_menor_3_aproximada = int(cantidad_estudiantes_menor_3_aproximada)
	
		diferencia_capacidad_entre_pisos = cantidad_estudiantes - cantidad_personas_1_piso
		habitaciones_faltantes = (float(diferencia_capacidad_entre_pisos) / float(cantidad_maxima_habitacion_2_piso))
		habitaciones_faltantes_aproximadas = math.ceil(habitaciones_faltantes)
		habitaciones_faltantes_aproximadas = int(habitaciones_faltantes_aproximadas)
	
		cantidad_personas_hospedaje_alterno = cantidad_estudiantes - (cantidad_personas_1_piso + cantidad_personas_2_piso)
		cantidad_habitaciones_1_hospedaje = (float(cantidad_personas_hospedaje_alterno) / float(cantidad_maxima_habitacion_1_piso_hospedaje))
		cantidad_habitaciones_1_hospedaje_aproximada = math.ceil(cantidad_habitaciones_1_hospedaje)
		cantidad_habitaciones_1_hospedaje_aproximada = int(cantidad_habitaciones_1_hospedaje_aproximada)
	
		
		if (cantidad_estudiantes <= 232):
			print "cantidad de buses que necesita: ", cantidad_buses_aproximada
		if (cantidad_estudiantes > 0)and(cantidad_estudiantes < cantidad_maxima_habitacion_1_piso):
			print "cantidad de habitaciones que necesita:", cantidad_estudiantes_menor_3_aproximada 
		if (cantidad_estudiantes >= cantidad_maxima_habitacion_1_piso)and(cantidad_estudiantes <= cantidad_personas_1_piso): 
			print "se necesitan", cantidad_habitaciones_menor_limite_piso_1_aproximada, "habitaciones en el primer piso"
		if (cantidad_estudiantes > cantidad_personas_1_piso)and(cantidad_estudiantes <= cantidad_personas_maximo_salento):
			print "se necesitan" , cantidad_habitaciones_1_piso_limite, "habitaciones en el primer piso"
			print "se necesitan" , habitaciones_faltantes_aproximadas, "habitaciones en el segundo piso"			
		if cantidad_personas_hospedaje_alterno < 0:
			print "no necesita hospedaje alterno"
		else:
			print "se necesitan", cantidad_habitaciones_1_piso_limite, "habitaciones en el primer piso"
			print "se necesitan", cantidad_habitaciones_2_piso_limite, "habitaciones en el segundo piso"
			print "la cantidad de personas en el hospedaje alterno es de: ", cantidad_personas_hospedaje_alterno
			print "se necesitan", cantidad_habitaciones_1_hospedaje_aproximada, "habitaciones en el primer piso del hospedaje alterno"
	else:
		print "no se hace el paseo"
	
	

def tres():
	print "\nEsa opcion es correcta\n"		
	print "Paseo en el parque del cafe"
	limite_estudiantes = 423	

	while 1:
		print "digite la cantidad de estudiantes"
		cantidad_estudiantes = raw_input()
		if cantidad_estudiantes.isdigit():
			cantidad_estudiantes = int(cantidad_estudiantes)
			break	

	if (cantidad_estudiantes <= limite_estudiantes ):
		
		if (cantidad_estudiantes <= 423):
			print "si se hace el paseo\n"	
			cupo_bus = 38
			cantidad_buses = (float(cantidad_estudiantes) / float(cupo_bus))
			cantidad_buses_aproximada = math.ceil(cantidad_buses)
			cantidad_buses_aproximada = int(cantidad_buses_aproximada)
		
			cantidad_maxima_habitacion_1_piso = 3
			cantidad_maxima_habitacion_2_piso = 4
			cantidad_maxima_habitacion_1_piso_hospedaje = 3
			cantidad_personas_1_piso = 195
			cantidad_personas_2_piso = 105
			cantidad_personas_maximo_parque = cantidad_personas_1_piso + cantidad_personas_2_piso
			
			cantidad_estudiantes_menor_195 = cantidad_personas_1_piso - cantidad_estudiantes
			diferencia_limite_piso_1 = cantidad_personas_1_piso - cantidad_estudiantes_menor_195
	
			cantidad_habitaciones_menor_limite_piso_1 = (float(diferencia_limite_piso_1) / float(cantidad_maxima_habitacion_1_piso))
			cantidad_habitaciones_menor_limite_piso_1_aproximada = math.ceil(cantidad_habitaciones_menor_limite_piso_1)
			cantidad_habitaciones_menor_limite_piso_1_aproximada = int(cantidad_habitaciones_menor_limite_piso_1_aproximada)
	
			cantidad_habitaciones_1_piso_limite = ((cantidad_personas_1_piso) / (cantidad_maxima_habitacion_1_piso))
			cantidad_habitaciones_2_piso_limite = ((cantidad_personas_2_piso) / (cantidad_maxima_habitacion_2_piso))
	
			cantidad_estudiantes_menor_3 = (float(cantidad_estudiantes) / float(cantidad_maxima_habitacion_1_piso))
			cantidad_estudiantes_menor_3_aproximada = math.ceil(cantidad_estudiantes_menor_3)
			cantidad_estudiantes_menor_3_aproximada = int(cantidad_estudiantes_menor_3_aproximada)
	
			diferencia_capacidad_entre_pisos = cantidad_estudiantes - cantidad_personas_1_piso
			habitaciones_faltantes = (float(diferencia_capacidad_entre_pisos) / float(cantidad_maxima_habitacion_2_piso))
			habitaciones_faltantes_aproximadas = math.ceil(habitaciones_faltantes)
			habitaciones_faltantes_aproximadas = int(habitaciones_faltantes_aproximadas)
	
			cantidad_personas_hospedaje_alterno = cantidad_estudiantes - (cantidad_personas_1_piso + cantidad_personas_2_piso)
			cantidad_habitaciones_1_hospedaje = (float(cantidad_personas_hospedaje_alterno) / float(cantidad_maxima_habitacion_1_piso_hospedaje))
			cantidad_habitaciones_1_hospedaje_aproximada = math.ceil(cantidad_habitaciones_1_hospedaje)
			cantidad_habitaciones_1_hospedaje_aproximada = int(cantidad_habitaciones_1_hospedaje_aproximada)
	
		
			if (cantidad_estudiantes <= 423):
				print "cantidad de buses que necesita: ", cantidad_buses_aproximada
			if (cantidad_estudiantes > 0)and(cantidad_estudiantes < cantidad_maxima_habitacion_1_piso):
				print "cantidad de habitaciones que necesita:", cantidad_estudiantes_menor_3_aproximada 
			if (cantidad_estudiantes >= cantidad_maxima_habitacion_1_piso)and(cantidad_estudiantes <= cantidad_personas_1_piso): 
				print "se necesitan", cantidad_habitaciones_menor_limite_piso_1_aproximada, "habitaciones en el primer piso"
			if (cantidad_estudiantes > cantidad_personas_1_piso)and(cantidad_estudiantes <= cantidad_personas_maximo_parque):
				print "se necesitan" , cantidad_habitaciones_1_piso_limite, "habitaciones en el primer piso"
				print "se necesitan" , habitaciones_faltantes_aproximadas, "habitaciones en el segundo piso"			
			if cantidad_personas_hospedaje_alterno < 0:
				print "no hay necesidad de acampar en la finca"
			else:
				print "se necesitan", cantidad_habitaciones_1_piso_limite, "habitaciones en el primer piso"
				print "se necesitan", cantidad_habitaciones_2_piso_limite, "habitaciones en el segundo piso"
				print "la cantidad de personas que van a acampar en la finca son: ", cantidad_personas_hospedaje_alterno
				print "por cada carpa pueden acampar: 3 personas"
				print "se necesitan", cantidad_habitaciones_1_hospedaje_aproximada, "carpas para acampar en la finca"
		else:
			print "no se hace el paseo"
	else:
		print "no se hace el paseo"

def salir():
	print "\nGracias por utilizar nuestro servicio\n"
	

# ya
seleccion_menu_uno = 4
	
while seleccion_menu_uno >= 1 and seleccion_menu_uno > 3:
	
	menu_uno = {1 : uno,  
	            2 : dos,   
		    3 : tres,
	            0 : salir,}
	while 1:
	
		print "Cupo Maximo Para Viajar a Montenegro es de 300 personas"
		print "Cupo Maximo Para Viajar a Salento es de 232 personas"
		print "Cupo Maximo Para Viajar al Parque del Cafe es de 423 personas\n\n"
		
		print "opcion 1.- Paseo en Montenegro"
		print "opcion 2.- Paseo en Salento"
		print "opcion 3.- Paseo en Parque del Cafe"
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
