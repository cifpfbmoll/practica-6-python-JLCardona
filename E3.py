from os import system
system("cls")
nota = float (input ("Dame una nota con la que empezar tú lista : "))
lista = []
print ("NOTA: si no quieres añadir más notas simplemente escribe una que no esté entre 0 y 10")
while (nota <= 10) and (nota >= 0):
    lista.append (nota)
    nota = float (input ("Dame más notas para añadir a tú lista : "))
print("E aquí la lista con tus notas : ", lista)
