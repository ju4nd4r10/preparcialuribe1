import random
import string

#Algoritmo 1: Crea ubna lista de 5 ingenieros (Un ingeniero es un diccionario)
 #crear la lista
lista=[]
for _ in range (1,6):

#crear el diccionario
    diccionario={}
      # id entero aleatorio no negativo
    diccionario["id_num"] = random.randint(0, 9999)
    
     # id alfanumérico
    diccionario["id_codigo"] = ''.join(
        random.choices(string.ascii_letters + string.digits, k=8)
    )
    
    #poblando el diccionario (Se necesita que el id sea un entero generado por pýthon de forma aleatori no negativo) (Se necesita que el id sea una cadena alfanumerica)
    diccionario["nombres"]=(input("Digita los nombre del empleado: "))
    diccionario["documento"]=(input("Digita el documento: "))
    diccionario["correo"]=(input("Digita el correo: "))
    diccionario["contraseña"]=(input("Digita la contraseña: "))
    
    
    
    # agregar el diccionario a la lista
    lista.append(diccionario)

print(lista)


  

  
