import math
costo_empanada = 600
costo_papa_aborrajada = 600
costo_papa_rellena = 1000
costo_aborrajado = 1000
costo_bofe = 3500
costo_gaseosa_personal = 1500
costo_gaseosa_litro = 3000
print "-------------------------------------------------------------------------------------"
print "cuanto desea comprar en empanadas"
presupuesto_empanadas = input()
presupuesto_empanadas = float(presupuesto_empanadas)
print "-------------------------------------------------------------------------------------"
print "cuanto desea comprar en papas aborrajadas"
presupuesto_papas_aborrajadas = input()
presupuesto_papas_aborrajadas = float(presupuesto_papas_aborrajadas)
print "-------------------------------------------------------------------------------------"
print "cuanto desea comprar en papas rellenas"
presupuesto_papas_rellenas = input()
presupuesto_papas_rellenas = float(presupuesto_papas_rellenas)
print "-------------------------------------------------------------------------------------"
print "cuanto desea comprar en maduros aborrajados"
presupuesto_aborrajados = input()
presupuesto_aborrajados = float(presupuesto_aborrajados)
print "-------------------------------------------------------------------------------------"
print "cuanto desea comprar en bofe"
presupuesto_bofe = input()
presupuesto_bofe = float(presupuesto_bofe)
print "-------------------------------------------------------------------------------------"
print "cuantas gaseosas personales desea comprar"
presupuesto_gaseosa_personal = input()
presupuesto_gaseosa_personal = float(presupuesto_gaseosa_personal)
print "-------------------------------------------------------------------------------------"
print "cuantas gaseosas litro y medio desea comprar"
presupuesto_gaseosa_litro = input()
presupuesto_gaseosa_litro = float(presupuesto_gaseosa_litro)
print "-------------------------------------------------------------------------------------"

cantidad_empanadas = presupuesto_empanadas / costo_empanada
cantidad_empanadas_enteras = math.trunc(cantidad_empanadas)
costo_total_empanadas = cantidad_empanadas_enteras * costo_empanada
devuelta_empanadas = presupuesto_empanadas - costo_total_empanadas
devuelta_empanadas_enteras = math.trunc(devuelta_empanadas)
print "-------------------------------------------------------------------------------------"
cantidad_papas_aborrajadas = presupuesto_papas_aborrajadas / costo_papa_aborrajada
cantidad_papas_aborrajadas_enteras = math.trunc(cantidad_papas_aborrajadas)
costo_total_papas_aborrajadas = cantidad_papas_aborrajadas_enteras * costo_papa_aborrajada
devuelta_papas_aborrajadas = presupuesto_papas_aborrajadas - costo_total_papas_aborrajadas
devuelta_papas_aborrajadas_enteras = math.trunc(devuelta_papas_aborrajadas)
print "-------------------------------------------------------------------------------------"
cantidad_papas_rellenas = presupuesto_papas_rellenas / costo_papa_rellena
cantidad_papas_rellenas_enteras = math.trunc(cantidad_papas_rellenas)
costo_total_papas_rellenas = cantidad_papas_rellenas_enteras * costo_papa_rellena
devuelta_papas_rellenas = presupuesto_papas_rellenas - costo_total_papas_rellenas
devuelta_papas_rellenas_enteras = math.trunc(devuelta_papas_rellenas)
print "-------------------------------------------------------------------------------------"
cantidad_aborrajados = presupuesto_aborrajados / costo_aborrajado
cantidad_aborrajados_enteros = math.trunc(cantidad_aborrajados)
costo_total_aborrajados = cantidad_aborrajados_enteros * costo_aborrajado
devuelta_aborrajados = presupuesto_aborrajados - costo_total_aborrajados
devuelta_aborrajados_enteros = math.trunc(devuelta_aborrajados)
print "-------------------------------------------------------------------------------------"
cantidad_bofe = presupuesto_bofe / costo_bofe
cantidad_bofe_entero = math.trunc(cantidad_bofe)
costo_total_bofe = cantidad_bofe_entero * costo_bofe
devuelta_bofe = presupuesto_bofe - costo_total_bofe
devuelta_bofe_entero = math.trunc(devuelta_bofe)
print "-------------------------------------------------------------------------------------"
cantidad_gaseosas_personales = presupuesto_gaseosa_personal / costo_gaseosa_personal
cantidad_gaseosas_personales_enteras = math.trunc(cantidad_gaseosas_personales)
costo_total_gaseosas_personales = cantidad_gaseosas_personales_enteras * costo_gaseosa_personal
devuelta_gaseosas_personales = presupuesto_gaseosa_personal - costo_total_gaseosas_personales
devuelta_gaseosas_personales_enteras = math.trunc(devuelta_gaseosas_personales)
print "-------------------------------------------------------------------------------------"
cantidad_gaseosas_litro = presupuesto_gaseosa_litro / costo_gaseosa_litro
cantidad_gaseosas_litro_enteras = math.trunc(cantidad_gaseosas_litro)
costo_total_gaseosas_litro = cantidad_gaseosas_litro_enteras * costo_gaseosa_litro
devuelta_gaseosas_litro = presupuesto_gaseosa_litro - costo_total_gaseosas_litro
devuelta_gaseosas_litro_enteras = math.trunc(devuelta_gaseosas_litro)
print "-------------------------------------------------------------------------------------"
devuelta_total = devuelta_empanadas_enteras + devuelta_papas_aborrajadas_enteras + devuelta_papas_rellenas_enteras + devuelta_aborrajados_enteros + devuelta_bofe_entero + devuelta_gaseosas_personales_enteras + devuelta_gaseosas_litro_enteras

print "su pedido en empanadas es de",cantidad_empanadas_enteras,"empanadas"
print "las ",cantidad_empanadas_enteras,"empanadas cuestan $",costo_total_empanadas
print "su devuelta es de $",devuelta_empanadas_enteras
print "gracias por su compra"
print "-------------------------------------------------------------------------------------"
print "su pedido en papas aborrajadas es de",cantidad_papas_aborrajadas_enteras,"papas aborrajadas"
print "las",cantidad_papas_aborrajadas_enteras,"papas aborrajadas cuestan $",costo_total_papas_aborrajadas
print "su devuelta es de $",devuelta_papas_aborrajadas_enteras
print "gracias por su compra"
print "-------------------------------------------------------------------------------------"
print "su pedido en papas rellenas es de",cantidad_papas_rellenas_enteras,"papas rellenas"
print "las",cantidad_papas_rellenas_enteras,"papas rellenas cuestan $",costo_total_papas_rellenas
print "su devuelta es de $",devuelta_papas_rellenas_enteras
print "gracias por su compra"
print "-------------------------------------------------------------------------------------"
print "su pedido en maduros aborrajados es de",cantidad_aborrajados_enteros,"aborrajados"
print "los",cantidad_aborrajados_enteros,"aborrajados cuestan $",costo_total_aborrajados
print "su devuelta es de $",devuelta_aborrajados_enteros
print "gracias por su compra"
print "-------------------------------------------------------------------------------------"
print "su pedido de bofe es de",cantidad_bofe_entero,"porciones"
print "las",cantidad_bofe_entero,"porciones de bofe cuestan $",costo_total_bofe
print "su devuelta es de $",devuelta_bofe_entero
print "gracias por su compra"
print "-------------------------------------------------------------------------------------"
print "su pedido de gaseosas personales es de",cantidad_gaseosas_personales_enteras,"gaseosas"
print "las",cantidad_gaseosas_personales_enteras,"gaseosas cuestan $",costo_total_gaseosas_personales
print "su devuelta es de $",devuelta_gaseosas_personales_enteras
print "gracias por su compra"
print "-------------------------------------------------------------------------------------"
print "su pedido de gaseosas litro es de",cantidad_gaseosas_litro_enteras,"gaseosas"
print "las",cantidad_gaseosas_litro_enteras,"gaseosas cuestan $",costo_total_gaseosas_litro
print "su devuelta es de $",devuelta_gaseosas_litro_enteras
print "gracias por su compra"
print "-------------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------------"
print "-------------------------------------------------------------------------------------"
print "su devuelta total es de $",devuelta_total

