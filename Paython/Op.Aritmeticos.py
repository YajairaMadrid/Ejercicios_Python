#OPERACIONES
import math
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))
#Operacion de Suma
suma = num1+num2
#Operacion de Resta
resta = num1-num2
#Operacion de Multiplicacion
Multiplicacion = num1*num2
#Operacion de Division
Division = num1/num2
#Operacion de Residuo
residuo = num1%num2
#Operacion
Operacion = (num1+num2-suma)*Multiplicacion
#Operacion para poder redondear un numero
#Colocamos en numero que queremos redondear en este caso num3
# y despues de la coma la cantidad de decimales que queremos.
num3 = 4.4365
num3Re = round(num3,2)
#OPERACION DE POTENCIA
#Forma sencilla
potencia = num1**3 
#Forma pro,primero va la base que en este caso seria num1 y luego de la coma el exponente que seria 3.
potencia2 = math.pow(num1,3) 
#Operacion de Raiz
raiz = math.sqrt(num1)  
#Resultados en Consola:
print("La suma es:" ,suma)
print("La resta es: ",resta)
print("La Multiplicacion es: ",Multiplicacion)
print("La Division es: ",Division)
print("El residuo es: ",residuo)
print("La Operacion seria: ",Operacion)
print("El resultado seria: ",num3Re)
print("La potencia sin Math seria: ",potencia)
print("La potencia con Math seria: ",potencia2)
print("la raiz cuadrada es: ",raiz)

numero12 =int(input("Ingrese un nuevo numero: "))
if numero12%2== 0:
    print("El numero que a ingresado es PAR.")
else:
    print("El numero que a ingresado es IMPAR.")