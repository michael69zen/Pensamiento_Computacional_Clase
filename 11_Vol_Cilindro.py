#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:11___
#___Escriba_un_programa_que_permita_hallar_volumen_de_un_Cilindro___

# Asignando Variables
pi = 3.1416
radio = float(input("RADIO DE LA BASE DEL CILINDRO = "))
altura = float(input("ALTURA DEL CILINDRO: "))

# Algoritmo para hallar el Volumen
volumen = round(((pi*(radio**2))*altura), 4)

# Imprimiendo el Volumen
print(f"VOLUMEN DEL CILINDRO = {volumen} m3trs")