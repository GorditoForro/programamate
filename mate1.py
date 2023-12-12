print("BIENVENIDO/A AL PROGRAMA DE PYTHON NUMERO 1 DE OSWALDO SANCHEZ")

"""Este programa tiene como objetivo enseñarnos a manipular el lenguaje de
programacion python y practicar el mismo, asi como desarrollar nuestro primer programa"""

#OPERACIONES BASICAS Y TIPOS DE DATOS
#SE PIDEN LOS DATOS

int1 = int(input("Ingresé un número entero: \n"))

int2 = int(input("Ingresé otro número entero \n"))

decimal1 = float(input("Ingresé un número con decimal: \n"))

decimal2 = float (input("Ingresé otro número con decimal: \n"))

int3 = int(input("Ingresé un nuevo número entero: \n"))

int4 = int(input("Ingresé otro número entero: \n"))

decimal3 = float(input("Ingresé un nuevo número con decimal: \n"))

decimal4 = float(input("Ingresé otro número con decimal: \n"))

#CALCULOS

suma = int1 + int2

resta = decimal1 - decimal2

multiplica = int3 * int4

division = decimal3 / decimal4

divient = decimal3 // decimal4

#MOSTRAMOS EN PANTALLA

print(f'''

La Suma de los números enteros {int1} y {int2} es igual a: {suma}

La Resta de los números con decimal {decimal1} y {decimal2} es igual a: {resta}

La multiplicacion con {int3} y {int4} es igual a: {multiplica} 

La division entre {decimal3} y {decimal4} es igual a: {division} y la division entera es {divient}

''')

#MANIPULACION DE CADENAS DE TEXTO

name = str(input("Ingresa tu nombre completo: "))

#Utilizamos la funcion len() para conseguir la longitud de los caracteres

longitud = len(name)

print(f"\nTu nombre es: {name} y tiene una longitud de caracteres de {longitud} ")

#Este tipo de manipulaciones de cadenas de texto son de gran ayuda para conocer la longitud de las variables de tipo string, y nos enseña mas sobre las funciones de python


'''Ejercicio 3: Conversión de Tipos de Datos'''

#Definimos los datos enteros y flotantes

entero1 = int(input("\nIngresa un numero entero para convertir a flotante: \n"))

enterotipo = type(entero1)

flotante1 = float(input("\nIngresa un numero flotante para convertirlo en entero: \n"))

flotatipo = type(flotante1)

#Utilizando las funciones int() y float() convertimos las variables

enteroconv = float(entero1)
enteroconvtipo = type(enteroconv)

flotanteconv = int(flotante1)
flotanteconvtipo = type(flotanteconv)

#Imprimimos en pantalla

print(f"\nEl numero entero {entero1} es de tipo {enterotipo} convertido a flotante es = {enteroconv} y de tipo {enteroconvtipo} \n")
print(f"\nEl numero decimal {flotante1} es de tipo {flotatipo} convertido a entero es = {flotanteconv} y de tipo {flotanteconvtipo} \n")
