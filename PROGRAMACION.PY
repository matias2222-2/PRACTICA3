import random

numero_secreto=random.randint(1,10)
intentos=0

numero=int(input("adivina el numero (entre 1 y 10)"))

while numero != numero_secreto:
    intentos+=1

if numero <numero_secreto:
    print(el numero es mayor)
else:
    print(el numero es menor)