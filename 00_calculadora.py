#_________PENSAMIENTO___COMPUTACIONAL_________
#___Ing._ACEITUNO_ROJO_Miguel_Romilio___
#___Est._JALLO_PAREDES_Cristhian_Michael___
#___Codigo:_236543___
#___Nro:_Ejercicio_Realizado_en_clase___
#___Escriba_un_programa_que_permita_ingresar_2_numeros_muestra_Suma||Resta||Multiplicación||División||Residuo___

# Asignando variables
a = float(input("INGRESE 1er NÚMERO: "))
b = float(input("INGRESE 2do NÚMERO: "))

#bucle while para que siempre se ejecute el codigo, solo hasta que nosotros deseamos salir.
while True:
    
    #una entrada para que elijamos que operación realizar
    opcion = input("¿Qué desea realizar?, (S)umar, (R)estar, (M)ultiplicación, (D)ivisión, r(E)siduo, (C)lose para salir :  ")
    opcion = opcion.upper()
    
    #condiciones para que ejecute la operacion, segun la opcion y operacion que queremos realizar
    if opcion == "S":
        suma = a + b
        print(f"LA SUMA ES: {suma}")
    elif opcion == "R":
        resta = a - b
        print(f"LA DIFERENCIA ES: {resta}")
    elif opcion == "M":
        mult = a * b 
        print(f"LA MULTIPLICACIÓN ES: {mult}")
    elif opcion == "D":
        div = a / b 
        print(f"LA DIVISIÓN ES: {div}")
    elif opcion == "E":
        resto = a % b
        print(f"EL RESTO ES: {resto}")
        
    # break para que el codigo deje de ejecutarse, ya que el bucle es infinito por qué: while => True
    elif opcion == "C":
        break
    
    