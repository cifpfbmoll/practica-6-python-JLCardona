from os import system
system("cls")
import random
MIN = int (input ("Dame el valor mínimo para empezar :"))
MAX = int (input ("Dame el valor máximo para empezar :"))
while (MAX <= MIN):
    MAX = int (input ("%d es inferior o identico a %d, deberias probar con otro numero : "%(MAX,MIN)))
adivinanza = random.randint(MIN,MAX)
print ("Escoge un número entero entre ", MIN ," y ", MAX ," y sin decirmelo intentare adivinarlo jeje")
respuesta = input ("Mmm... ¿Es %d tu numero? : "% (adivinanza))
while (respuesta!="si"):
    while (respuesta == "superior"):
        MIN = adivinanza
        adivinanza = random.randint(MIN,MAX)
        respuesta = input ("Mmm... ¿Es %d tu numero? : "% (adivinanza))
    while (respuesta == "inferior"):
        MAX = adivinanza
        adivinanza = random.randint(MIN,MAX)
        respuesta = input ("Mmm... ¿Es %d tu numero? : "% (adivinanza))
    while (respuesta!="superior") and (respuesta!="inferior") and (respuesta!="si"):
        respuesta = input ("¡¿Ehh?! ¿es inferior o superior? : ")
    if(MAX - MIN == 1) or (MAX == MIN):
        print ("¡OYE! ¡ESTAS HACIENDO TRAMPAS! Paso de jugar contigo.")
        respuesta = "si"
print ("Juego Finalizado")