from os import system
system("cls")
limite = int (input ("Dame el límite : "))
valor=int (input ("Ahora dame un valor para empezar la lista : "))
lista = []
lista.append (valor)
suma = valor
while (suma!=limite):
    if (suma < limite):
        valor = int (input ("Ahora dame otro valor : "))
        suma = suma + valor
        lista.append (valor)
    elif (suma > limite):
        lista.remove (valor)
        suma = suma - valor
        valor = int (input ("¡ERROR! %d es demasiado grande, dame otro valor : "%(valor)))
        suma = suma + valor
        lista.append (valor)
string = str (lista[0])
for i in range (1,len(lista)):
    string += ", " + str (lista[i])
print ("El limite es ",limite,"y la lista mediante tus valores es la siguiente --> ",string)