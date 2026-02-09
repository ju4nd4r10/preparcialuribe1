# Algoritmo 2: Rutina para login de usuario con correo y contraseña, se permiten hasta 3 intentos

# Variables de datos almacenados en DB
correoBD="correo@gmail.com"
contraseñaBD="admin123"



intentosPermitidos=3
contadorIntentos=0


# Ciclo para controlar el numero de intentos
while contadorIntentos<intentosPermitidos:
    
    # Varialbe que digita el usuario
    correoDigitado=input("Digita tu correo: ")
    contraseñaDigitada=input("Digita tu contraseña: ")

    
    # Evaluaar si el ciclo es efectivo
    if correoDigitado==correoBD and contraseñaDigitada==contraseñaBD:
        print("Login correcto. Bienvenido.")
        break
    else:
        contadorIntentos+=1
        intentosRestantes = intentosPermitidos - contadorIntentos
        print("Datos incorrectos")
        print(f"Intento {contadorIntentos} de {intentosPermitidos}")
        
        if intentosRestantes > 0:
            print(f"Te quedan {intentosRestantes} intentos\n")
        else:
            print("Usuario bloqueado. Superaste el número de intentos.")

        #Se necesita mensajes que indiquen el numero que llevo y cuantos me quedan  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        