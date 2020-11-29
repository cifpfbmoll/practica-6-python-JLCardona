from os import system
system("cls")
numero1 = int (input ("Dame un número : "))
numero2 = int (input ("Dame un número mayor que %d : " %(numero1)))
while (numero1 >= numero2):
    numero2 = int (input ("¡ERROR! : %d no es un número mayor que %d, dame de nuevo un número : " % (numero2, numero1)))
print ("E aquí tus números : El 1o --> ", numero1 ," y el 2o --> ", numero2)