from os import system
system("cls")
lista = []
print ("NOTA: si no quieres añadir más números o nombres simplemente pulsa la tecla s")
nombre = "A"
while (nombre!="s"):
    nombre = input ("Dame el nombre de tu contacto : ")
    if (nombre!="s"):
        numtelefono = input ("Ahora dame el numero de teléfono de ese contacto : ")
        lista.append ([nombre,numtelefono])
print ("E aquí tu agenda de contactos : ")
for i in range (len (lista)):
    print ("NOMBRE --> ",lista[i][0]," NUM.TELEFONO --> ",lista[i][1])
