import random

#Algoritmo 3: Algoritmo para recorrer una lista y un promedio numerico

#generar una lista aleatoria de 20 datos que esten entre dos valores (0,450)
lista=[120,250,340,500,301,300,40,87,500]
for _ in range(20):
    lista.append(random.randint(0, 450))

numerosDeElementosDeLaLista=len(lista) #tamaño de lsita
suma=0

# UN foreach es un for adaptado que perminte ir elemento por elemento en una lista
for elemento in lista:
    suma+=elemento #sumar todos los elementos de una lista de nuemros
    
    promedio=suma/numerosDeElementosDeLaLista
    print("El pormedio es: ", promedio)
    
    #Clasificar al promedio de los datos
    if promedio>0 and promedio<=250:
        print("Operacio0n detenida por falta de agua")
    elif promedio>250 and promedio <=400:
        print("Operando con normalidad")
    else:
        print("Deben abrirse las compuertas de la represa")
        
        
