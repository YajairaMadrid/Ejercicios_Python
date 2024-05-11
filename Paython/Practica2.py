#                               PRÁCTICA DIRIGIDA

#1.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
#sexo y el nombre. El grupo A esta formado por las mujeres con un nombre
#anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
#resto. Escribir un programa que pregunte al usuario su nombre y sexo, y
#muestre por pantalla el grupo que le corresponde.
print("///////////////////////EJERCICIO 1://///////////////////////////////")
nom=input("Ingrese su Nombre: ")
sex=input("Ingrese su sexo (F o M):")
if (sex== "F" and nom.lower()<"m") or (sex=="MCalos" and nom.lower()>"N"):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es:", grupo)

#2.- Para tributar un determinado impuesto se debe ser mayor de 16 años y
#tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un
#programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
#por pantalla si el usuario tiene que tributar o no.
print("///////////////////////EJERCICIO 2://///////////////////////////////")
edad= int(input("¿Cuál es tu edad?"))
ingresos= float(input("¿Cuál es tu ingreso mensual?"))
if edad >16 and ingresos>= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")

#3.- Escribir un programa para una empresa que tiene salas de juegos para
#todas las edades y quiere calcular de forma automática el precio que debe
#cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
#del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años
#puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de
#18 años, 10€.
print("///////////////////////EJERCICIO 3://///////////////////////////////")
edad= int(input("¿Cuál es tu edad?"))
if edad < 4:
    print("Su entrada es gratuita")
elif edad >= 4 and edad <= 18:
    print("El precio de su entrada es de 5€")
else:
    print("El precio de su entrada es de 10€")

#4.- Escribir un programa que almacene la cadena de caracteres contraseña en
#una variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable
#sin tener en cuenta mayúsculas y minúsculas.
print("///////////////////////EJERCICIO 4://///////////////////////////////")
cont = "yajaira"
password= input("Ingrese la contraseña:")
if cont == password.lower():
    print("La ontraseña correcta")
else:
    print("La contraseña es incorrecta")





    