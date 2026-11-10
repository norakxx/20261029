#OTRA OPCION:cuentatras= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
Utilizar una rango de números que recorra del 10 hasta el -1 pues por defecto comienza en 0. 
Designo un número que responda y se asigne como "..." luego quiero saltar del 8 al 2, por tanto 
coloco una función que me diga cuando X es 2< x <8 y que continue (Así es como salta de números).
Por último queremos que cuando el numero sea 0 la cuenta atras acabe y haga kabom.

Ahora añadimos una def para "intentar desactivar la bomba. Ponemos una condición que el número sea par.
""" 
import time
import json
import random
with open ("color.json", "r") as archivo:
    data=json.load(archivo)


def intentar_desactivar():
    cable= input("Ingrese el color y cable que quieres cortar: ")

    if cable.lower()==random.choice(data["colores"]):
        print("Bomba desactivada suertudo")
        return True
    
    else:
        return False


for number in range(10,-1,-1):
    print(number)
    time.sleep(1)
 #Cuando sea un numero par, llamar a a funcion intentar desactivar y si devuevle True hago break
    if number==8 or number==2:
        if intentar_desactivar():
            break

    if number == 6:
        print("...")
    if number <8 and number >2:    
        continue
    if number==0:
        print("KABOM YA ESTA AQUÍ LA GUERRA")