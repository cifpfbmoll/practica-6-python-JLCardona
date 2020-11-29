from os import system
system("cls")
import random
MIN = int (input ("Dame el valor mínimo para comenzar :"))
MAX = int (input ("Dame el valor máximo para comenzar :"))
intentos = 0
adivinanza = random.randint(MIN,MAX)
print("¿Podras adivinar el numero que he escogido entre ", MIN ," y ", MAX ," ?")
numero = int (input ("Dame tu respuesta : "))
while (numero!=adivinanza):
    while (numero < adivinanza):
        numero = int (input ("Nonono, ese numero es inferior, deberias probar con otro numero jajaja : "))
        intentos += 1
    while (numero > adivinanza):
        numero = int (input ("Mmmmm no, ese numero es supeior, prueba con otro mejor haha : "))
        intentos += 1
print ("¡LO ADIVINASTE IMPOSIBLE! Bueno has tardado lo tuyo, lo has intentado nada mas ni nada menos que ", intentos ," veces.")