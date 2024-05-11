                                #EJERCICIOS DE PYTHON
#                                      SEMANA 1
import math
#1. Escribe un programa que solicite al usuario dos números y muestre su
#   suma, resta, multiplicación, división, división entera y residuo (módulo).
#### RESOLUCION ####
print("///////////////////////EJERCICIO 1://///////////////////////////////")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese el segundo numero: "))
#La suma seria:
suma = num1 + num2
print("-La suma seria: ", suma)
#La resta seria:
resta = num1 - num2
print("-La resta seria: ", resta)
#La multiplicacion seria:
multiplicacion = num1 * num2
print("-La multiplicacion seria: ", multiplicacion)
#La division seria:
division = num1/num2
print("-La division seria: ", division)
#la diivision Entera seria:
diventera = num1//num2
print("-La division entera seria: ", diventera)
#El residuo seria:
residuo = num1%num2
print("-El residuo seria: ", residuo)
print("\n")

#2. Escribe un programa que solicite al usuario un número entero y calcule
#su cuadrado y su cubo.
print("///////////////////////EJERCICIO 2://///////////////////////////////")
num3 = int(input("Ingrese un numero: "))
#Al cuadrado:
potencia1 = math.pow(num3,2) 
#Al cubo:
potencia2 = math.pow(num3,3) 
print("-El numero ingresado al cuadrado seria: ", potencia1)
print("-El numero ingresado al cubo seria: ", potencia2)
print("\n")

#3. Escribe un programa que lea un número entero y determine si es
#positivo, negativo o cero.
print("///////////////////////EJERCICIO 3://///////////////////////////////")
num4 = int(input("Ingrese un numero: "))

if num4>0:
    print("-El numero es positivo: ")
elif num4<0:
    print("-El numero es negativo: ")
else:
    print("-El numero es cero: ")
print("\n")

#4. Escribe un programa que solicite al usuario un número entero y calcule
#si es divisible por 3 y por 5.
print("///////////////////////EJERCICIO 4://///////////////////////////////")
numero9 = int(input("Ingrese un numero: "))
numero10 = 3
numero11 = 5
division = numero9//numero10
print("-La division entre:",numero9 ,"y 3 es: ",division)
division2 = numero9//numero11
print("-La division entre:",numero9,"y 5 es: ",division2)
print("\n")

#5. Escribe un programa que tome una calificación numérica de un
#estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
#- 90-100: A
#- 80-89: B
#- 70-79: C
#- 60-69: D
#- Menos de 60: F
####  RESOLUCION  ####
print("///////////////////////EJERCICIO 5://///////////////////////////////")
nota = float(input("Ingrese una nota de calificacion entre 0 a 100: "))
if nota>=90 and nota<=100:
    print("La calificacion es: A")
elif nota>=80:
    print("-La calificacion es: B")
elif nota>=70:
    print("-La calificacion es: C")
elif nota>=60:
    print("-La calificacion es: D")
elif nota>=50:
    print("-La calificacion es: E")
else:
    print("-La calificacion es: F")
print("\n")

#6. Escribe un programa que solicite al usuario tres números y determine
#cuál de ellos es el mayor.
print("///////////////////////EJERCICIO 6://///////////////////////////////")
num6 =int(input("Ingrese un numero: "))
num7 =int(input("Ingrese un numero: "))
num8 =int(input("Ingrese un numero: "))

if num7<num6>num8:
    print("-El numero Mayor es: ",num6)
elif num6<num7>num8:
    print("-El numero Mayor es: ",num7)
elif num6<num8>num7:
    print("-El numero Mayor es: ",num8)
print("\n")

#7. Escribe un programa que solicite al usuario un número entero y
#determine si es par o impar.
print("///////////////////////EJERCICIO 7://///////////////////////////////")
numero12 =int(input("Ingrese un nuevo numero: "))
if numero12%2== 0:
    print("-El numero que a ingresado es PAR.")
else:
    print("-El numero que a ingresado es IMPAR.")
print("\n")