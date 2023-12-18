#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:09___
#___Escriba_un_programa_que_permita_hallar_volumen_de_una_esfera___

# Asignando Variables
radio = float(input("RADIO DE LA ESFERA = "))
pi = 3.1416

# Algoritmo para hallar el Volumen
vol_esfera = round(((4/3)*pi*(radio**3)), 4)

# Imprimiendo el Volumen
print(f"VOLUMEN DE LA ESFERA = {vol_esfera} m3trs")