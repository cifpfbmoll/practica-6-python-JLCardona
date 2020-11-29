from os import system
system("cls")
numero = int (input ("Dame un número para empezar tú lista : "))
lista = []
print ("NOTA: si no quieres añadir más números simplemente escribe SALIR")
while (numero!="SALIR"):
    numero = int (numero)
    lista.append (numero)
    numero = input ("Dame más números para añadir a tú lista : ")
print ("E aquí la lista con tus números : ", lista)