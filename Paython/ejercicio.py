##                                                            BUCLES   


###### FOR, WHILE, DO-WHILE

#CONDICIONALES
###### IF, SWITCH

######            EJERCICIO 1           ########
print("                 EJERCICIO 1                 ")
#1-10
for i in range(1,11):
    print(i)

#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta 
# ese número separados por comas.  #20

n= int(input("Introduce un número entero positivo: "))  
for i in range(1,n+1,2):
    print(i, end=",")


######            EJERCICIO 2           ########
#Escribir un programa que pida al usuario un 
#número entero y muestre por pantalla un triángulo
#rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
#20

print("                 EJERCICIO 2                 ")
n= int(input("Introduce la altura del triángulo (entero positivo): ")) 
for i in range(1,n+1,2):   #1  3  5  7
    for j in range(i,0,-2):
        print(j, end=" ")
        
    print("")


######            EJERCICIO  3          ########
print("                 EJERCICIO 3                 ")
palabra= input("Introduce una palabra: ") #Brinner
vocales=['a','e','i','o','u']
for vocal in vocales:
    repeticiones=0
    for letra in palabra:
        if letra==vocal:
            repeticiones+=1
        
    print("La vocal "+vocal+" aparece: "+str(repeticiones)+"veces")

######            EJERCICIO  4          ########
#Escribir un programa que muestre el eco de todo lo que 
#el usuario introduzca hasta que el usuario escriba “salir” que terminará.
print("                 EJERCICIO 4                 ")

while True:
    frase= input("Introduce el texto/palabra: ") #JUAN
    if frase=="salir":
        break
    print(frase)

######            EJERCICIO  5          ########
#Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.
print("                 EJERCICIO 5                 ")

frase= input("Introduce una frase: ") #Hola amigos
letra= input("Introduce una letra: ") #a 
contador=0

fraseMinuscula= frase.lower()
print(contador)

for i in frase:  #H
    if i==letra:
        contador+=1
print("la letra",letra,"aparece", contador, "en la frase: ",frase)
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra,contador,frase))

print(contador)


