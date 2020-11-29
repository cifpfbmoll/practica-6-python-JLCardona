from os import system
system("cls")
numero1 = int (input ("Dame un número para empezar tú lista: "))
lista = []
print ("NOTA: si no quieres añadir más números simplemente escribe uno inferior al anterior")
lista.append (numero1)
numero2 = int (input ("Ahora dame un número mayor que %d : " %(numero1)))
while (numero1 < numero2):
    lista.append (numero2)
    numero1 = numero2
    numero2 = int (input ("Ahora dame un número mayor que %d : " %(numero1)))
string = str (lista[0])
for i in range (1,len(lista)):
    string = string + ", " + str (lista[i])
print ("E aquí la lista con tus números : ", string)