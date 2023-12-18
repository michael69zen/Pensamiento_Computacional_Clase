#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:10___
#___Escriba_un_programa_que_permita_hallar_volumen_de_un_cono___

# Asignando Variables
pi = 3.1416
radio = float(input("RADIO DE LA BASE DEL CONO = "))
altura = float(input("ALTURA DEL CONO = "))

# Algoritmo para hallar el Volumen
volumen = round(((1/3)*pi*(radio**2)*altura), 4)

# Imprimiendo el Volumen
print(f"VOLUMEN DEL CONO = {volumen} m3trs")