#####                                       DICCIONARIOS

#Escribir un programa que almacene el 
# diccionario con los créditos de las
# asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# y después muestre por pantalla los créditos de cada asignatura
# en el formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, y <créditos> 
# son sus créditos. Al final debe mostrar también el número total de créditos del curso
print("///////////////////////EJERCICIO de diccionario://///////////////////////////////")

curso= {'- Matemáticas':6 , '- Física': 4, '- Química': 5}
total_creditos=0
for asignatura,credito in curso.items():
    print(asignatura, 'tiene', credito, 'creditos.')
    total_creditos+=credito
print('- Número total de creditos del curso: ', total_creditos)


#####                                       LISTAS

#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.
print("///////////////////////EJERCICIO 1://///////////////////////////////")

asignaturas=["Matematicas","Fisica","Química","Historia","Lengua"]
print(asignaturas)

#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada 
# asignatura, y después las muestre por pantalla con el mensaje 
# En <asignatura> has sacado <nota> donde <asignatura> es cada una
# des las asignaturas de la lista y <nota> cada una de las correspondientes 
# notas introducidas por el usuario.
print("///////////////////////EJERCICIO 2://///////////////////////////////")

asignaturas= ["Matematicas","Fisica","Química","Historia","Lengua"]
for asignatura in asignaturas:
    print("Yo estudio: "+asignatura)

#Escribir un programa que almacene las asignaturas de 
# un curso (por ejemplo Matemáticas, Física, Química, 
# Historia y Lengua) en una lista, pregunte al usuario
# la nota que ha sacado en cada asignatura, y después las muestre 
# por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista y <nota> 
# cada una de las correspondientes 
# notas introducidas por el usuario.
print("///////////////////////EJERCICIO 3://///////////////////////////////")

asignaturas= ["Matematicas","Fisica","Química","Historia","Lengua"]
notas=[]
print(notas)

for asignatura in asignaturas:
    nota= input("¿Qué nota has sacado en "+asignatura+"?:  ") #20
    notas.append(nota)
    
for i in range(len(asignaturas)):
    print("En la asignatura "+ asignaturas[i]+"has sacado : "+notas[i])