from os import system
system("cls")
print ("NOTA: si no quieres añadir más números simplemente escribe uno que no esté comprendido entre los dos valores iniciales")
MIN = int (input ("Dame un número para empezar tú lista : "))
MAX = int (input ("Ahora dame un número mayor que %d : " %(MIN)))
lista = []
while (MAX < MIN):
    MAX = int (input ("¡ERROR! %d es mayor que %d, dame un número MAYOR al anterior : " %(MIN,MAX)))
numero = int (input ("Ahora dame un número entre %d y %d : " %(MIN,MAX)))
while (numero < MAX) and (numero > MIN):
    lista.append (numero)
    numero = int (input ("Ahora dame otro número entre %d y %d : "%(MIN,MAX)))
string = str (lista[0])
for i in range (1,len(lista)):
    string += ", " + str (lista[i])
print ("La lista de números que hay entre ",MIN," y ",MAX," son los siguientes --> ",string)
