from os import system
system("cls")
limite = int (input ("Dame el límite : "))
valor = int (input ("Ahora dame un valor : "))
lista = []
lista.append (valor)
suma = valor
while (suma < limite):
    valor = int (input ("Ahora dame otro valor : "))
    lista.append (valor)
    suma = suma + valor
string = str (lista[0])
for i in range (1,len(lista)):
    string += ", " + str (lista[i])
print("El límite es ",limite,"y la lista de números es la siguiente --> ",string," \n\
El programa ha finalizado, la suma de todos los números de la lista supera el límite --> ",suma,".")