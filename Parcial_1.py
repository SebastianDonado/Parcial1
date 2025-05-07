## Parcial 1
##Cree un algoritmo que lea 5 números enteros uno por uno e identifique cuáles son 
# positivos y pares. Al final, debe mostrar la suma total de esos números.

#Definimos una función para cada variable para definir si cada variable es positiva y par
def variable(a):
    if a%2 == 0 and a>= 0:
        return a
    else:
        return 0

def variable_b(b):
    if b%2 == 0 and b>= 0:
        return b
    else:
        return 0

def variable_c(c):
    if c%2 == 0 and c>= 0:
        return c
    else:
        return 0

def variable_d(d):
    if d%2 == 0 and d>= 0:
        return d
    else:
        return 0

def variable_e(e):
    if e%2 == 0 and e>= 0:
        return e
    else:
        return 0
## En esta función suma sumamos todas las funciones anteriores que cumplen el papel de que si el número
# es par positivo devuelve el valor ingresado si no lo es devuelve 0 asi realizando la suma solo suma 
# los números pares positivos 
def suma(a,b,c,d,e):
    sum = variable(a) + variable_b(b) + variable_c(c) + variable_d(d) + variable_e(e)
    print(f"La suma de los número pares psitivos es {sum}")

## Ejercicio 3
#Para cada vocal defino una función que lleve el conteo de cuantas veces esta la vocal en la palabra
#esto lo hago mediante un for donde hago que pase por cada letra de a palabra y con un if digo que cada
#vez que la variable iterativa pertenezca a la variable vocal donde esta cada vocal mayúscula y minúscula
#Entonces le suma uno al conteo

def contar_a(palabra):
    vocal = "aA"
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador += 1
    return contador

def contar_e(palabra):
    vocal = "eE"
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador += 1
    return contador

def contar_i(palabra):
    vocal = "iI"
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador+= 1
    return contador

def contar_o(palabra):
    vocal = "oO"
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador += 1
    return contador

def contar_u(palabra):
    vocal = "uU"
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador += 1
    return contador

#Defino la función que va a realizar la tabla donde se ubique cuantas veces esta cada vocal en la
#ingresada
def tabla(pal):
    print(f"A= {contar_a(pal)}")
    print(f"E= {contar_e(pal)}")
    print(f"I= {contar_i(pal)}")
    print(f"O= {contar_o(pal)}")
    print(f"U= {contar_u(pal)}")
    return pal
##Diseñe un programa que lea la edad de una persona y muestre un mensaje según el siguiente criterio:
# Menor de 13 años → “Niño”
#Entre 13 y 17 años → “Adolescente”
#Entre 18 y 59 años → “Adulto”
#60 años o más → “Adulto mayor”

#Creo una función para almacenar la edad y realice una serie de operaciones
def edad(edad):
## Con el while nos encargamos de que el usuario ingrese un número entero postivo

    while edad<0:
        print("Error ingreso una edad negativa")
        edad= int(input("intente nuevamente \n"))
## Luego de que el usuario ingreso un númer entero positivo el if no ayuda para comparar la edad
# y saber en que intervalo esta ubicada para asi mostrar el mensaje correcto
    if edad < 13:
        print("Niño")
    elif 13<= edad <= 17:
        print("Adolecente")
    elif 18<= edad <= 59:
        print("Adulto")
    elif edad>= 60:
        print("Adulto mayor")



## Brevemente creo un menu, a cada ejercicio le doy un numero por ejemplo para el ejercicio uno debe 
#ingresar el numero 1 y asi con los otro dos, esto meidante el if
menu=int(input("Que ejercicio desea realizar \n"))
if menu == 1:
    suma(int(input("Ingrese un número entero \n")),int(input("Ingrese un número entero \n")),int(input("Ingrese un número entero \n")),int(input("Ingrese un número entero \n")),int(input("Ingrese un número entero \n")))

elif menu == 2:
    edad(int(input("Ingrese su edad \n")))
elif menu == 3:
    tabla(input("Ingrese una palabra\n"))
else:
    print("Elijio una opción incorrecta")