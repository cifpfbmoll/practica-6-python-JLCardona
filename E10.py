from os import system
system("cls")
lista1 = []
lista2 = []
print ("NOTA: si no quieres añadir más notas a X alumno escribe un numero fuera de 0-10, si no quieres añadir mas alumnos no escribas sus nombres")
nombre = input ("Dame el nombre del alumno : ")
while (nombre!=""):
    lista2.append (nombre)
    nota = float (input ("Dame la nota de dicho alumno : "))
    while (nota >= 0) and (nota <= 10):
        lista2.append (nota)
        nota = float (input ("Dame otra nota de dicho alumno: "))
    lista1.append (lista2)
    lista2 = []
    nombre = input ("Dame el nombre del alumno : ")
print ("E aquí las notas totales de los alumnos : ")
for i in range (len (lista1)):
    print (lista1[i][0],":", end = " ")
    for j in range (1,len (lista1[i])):
        print (" - ", lista1[i][j], end = " - ")
    print ("")