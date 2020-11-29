from os import system
system("cls")
palabra = input ("Dame una palabra con la que empezar tú lista : ")
lista = []
print ("NOTA: si no quieres añadir más palabras simplemente dale al ENTER")
while (palabra!=""):
    lista.append (palabra)
    palabra = input ("Dame más palabras para añadir a tú lista : ")
print ("E aquí la lista con tus palabras : ", lista)