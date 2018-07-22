# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label ejercicio_paralelo:
        
    menu:
        "Resolverlo yo.":
            jump ejercicio_paralelo_parte2_usuario
        
        "Dejar que el programa lo resuelva":
            jump ejercicio_paralelo_parte2_computadora
        
        "¿Desea resolver usted el problema o que este programa lo resuelva por usted?"
        
        
label ejercicio_paralelo_parte2_computadora:
     
    #$ e = a/(b*c)
    
    $ num = int(clientes)
    $ factorial = 1
    $ ffff = 0
    python: 
        for ffff in range(1,num + 1):
           factorial = factorial*ffff
    
    $ sumatoria = 0
    $ c = int(c)
    $ clientes = int(clientes)
    $ nnn = 0 
    python:
        for nnn in range(0,(c-1)+1):
            sumatoria = sumatoria+((e**clientes)/factorial)


    $ num = int(c)
    $ factorial = 1
    $ ffff = 0
    python: 
        for ffff in range(1,num + 1):
           factorial = factorial*ffff


    $ n = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
    
    $ num = int(c-1)
    $ factorial = 1
    $ ffff = 0
    python: 
        for ffff in range(1,num + 1):
           factorial = factorial*ffff
           
           
    $ l = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
    
    $ m = float(l + e)
    
    $ jx = float(l/a)
    
    $ k = float(jx+(1/b))
    
    scene modelo23fondo1 with dissolve
    hide fondo with dissolve

    if a != 0:
        $ cuadro1 = True
    else:
        $ cuadro1n = True
                
                
                
    if b != 0:
        $ cuadro2 = True
    else:
        $ cuadro2n = True
                

    if c != 0:
        $ cuadro3 = True
    else:
        $ cuadro3n = True
                
                
    if e != 0:
        $ cuadro5 = True
    else:
        $ cuadro5n = True
                    
                    
    if jx != 0:
        $ cuadro10 = True
    else:
        $ cuadro10n = True
                    
                    
          
                
    if k != 0:
        $ cuadro11 = True
    else:
        $ cuadro11n = True

            
            
    if l != 0:
        $ cuadro12 = True
    else:
        $ cuadro12n = True
                    
                    
                    
                    
    if m != 0:
        $ cuadro13 = True
    else:
        $ cuadro13n = True
                    
                    
                    
                    
    if n != 0:
        $ cuadro14 = True
    else:
        $ cuadro14n = True
        
        
        
        
    if clientes != 0:
        $ cuadro18 = True
    else:
        $ cuadro18 = False
                            
    
    "Aqui están los resultados."
    
    
    $ cuadro1 = False
    $ cuadro1n = False
    $ cuadro2 = False
    $ cuadro2n = False
    $ cuadro3 = False
    $ cuadro3n = False
    $ cuadro4 = False
    $ cuadro4n = False
    $ cuadro5 = False
    $ cuadro5n = False
    $ cuadro6 = False
    $ cuadro6n = False
    $ cuadro7 = False
    $ cuadro7n = False
    $ cuadro8 = False
    $ cuadro8n = False
    $ cuadro9 = False
    $ cuadro9n = False
    $ cuadro10 = False
    $ cuadro10n = False
    $ cuadro11 = False
    $ cuadro11n = False
    $ cuadro12 = False
    $ cuadro12n = False
    $ cuadro13 = False
    $ cuadro13n = False
    $ cuadro14 = False
    $ cuadro14n = False
    $ cuadro15 = False
    $ cuadro15n = False
    $ cuadro16 = False
    $ cuadro16n = False
    $ cuadro18 = False
    $ cuadro18n = False
    
    scene fondo with dissolve
    hide modelo23fondo1 with dissolve
                
    jump contador_de_ejercicios


label ejercicio_paralelo_parte2_usuario:
    
    $ puntuacion = long(20)
    $ tyrion = 0
    $ jon = 0
                
    "Resuelva el siguiente ejercicio, recuerde que solo puede escribir dos decimales."
    
    scene modelo23fondo2 with dissolve
    hide fondo with dissolve
                
    $ respuesta1 = ""
    $ respuesta2 = ""
    $ respuesta3 = ""
    $ respuesta4 = ""
    $ respuesta5 = ""
    $ respuesta6 = ""
    $ respuesta7 = ""
    $ respuesta8 = ""
    $ respuesta9 = ""
    $ respuesta10 = ""
    $ respuesta11 = ""
    $ respuesta12 = ""
    $ respuesta13 = ""
    $ respuesta14 = ""
                

    if a != 0:
        $ cuadro1 = True
    else:
        $ cuadro1n = True
                
                
                
    if b != 0:
        $ cuadro2 = True
    else:
        $ cuadro2n = True
                

    if c != 0:
        $ cuadro3 = True
    else:
        $ cuadro3n = True
                
                
    if e != 0:
        $ cuadro5 = True
    else:
        $ cuadro5n = True
                    

                    
    if jx != 0:
        $ cuadro10 = True
    else:
        $ cuadro10n = True
                    
                    
          
                
    if k != 0:
        $ cuadro11 = True
    else:
        $ cuadro11n = True

            
            
    if l != 0:
        $ cuadro12 = True
    else:
        $ cuadro12n = True
                    
                    
                    
                    
    if m != 0:
        $ cuadro13 = True
    else:
        $ cuadro13n = True
                    
                    
                    
                    
    if n != 0:
        $ cuadro14 = True
    else:
        $ cuadro14n = True
                            
            
    if clientes != 0:
        $ cuadro18 = True
    else:
        $ cuadro18 = False
        

#______________________________________________________________________________________________________________________________________________

    
    
    $ num = int(clientes)
    $ factorial = 1
    $ ffff = 0
    python: 
        for ffff in range(1,num + 1):
           factorial = factorial*ffff
    
    $ sumatoria = 0
    $ c = int(c)
    $ clientes = int(clientes)
    $ nnn = 0 
    python:
        for nnn in range(0,(c-1)+1):
            sumatoria = sumatoria+((e**clientes)/factorial)


    $ num = int(c)
    $ factorial = 1
    $ ffff = 0
    python: 
        for ffff in range(1,num + 1):
           factorial = factorial*ffff
    
    
    
    $ errores = 0                
    $ respuesta5 = renpy.input("¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
    $ j = float(respuesta5)
    $ j = round(j,2)
    $ gah = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta5]."
        $ jon = jon + 1
        $ n = j
        $ cuadro14n = False
        $ cuadro14 = True
                
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta5]."
            $ jon = jon + 1
            $ n = j
            $ cuadro14n = False
            $ cuadro14 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta5 = ""
                if errores == 1:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                if errores == 2:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                elif errores == 3:
                    $ respuesta5 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Recuerde la formula {image=modelo3/po.png}", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                elif errores == 4:
                    $ j = gah 
                    $ n = round(j,2)
                    "la respuesta era [n]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro14n = False
                    $ cuadro14 = True
                
    else:
        while j != gah:
            $ errores += 1
            $ respuesta5 = ""
            if errores == 1:
                $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta5)
                $ j = round(j,2)
                $ gah = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta5]."
                    $ jon = jon + 1
                    $ n = j
                    $ cuadro14n = False
                    $ cuadro14 = True
            if errores == 2:
                $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta5)
                $ j = round(j,2)
                $ gah = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta5]."
                    $ jon = jon + 1
                    $ n = j
                    $ cuadro14n = False
                    $ cuadro14 = True
            elif errores == 3:
                $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Recuerde la formula {image=modelo3/po.png}", allow="0123456789-.")
                while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta5)
                $ j = round(j,2)
                $ gah = float((sumatoria+((e**c)/(factorial*(1-(e/c)))))**(-1))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta5]."
                    $ jon = jon + 1
                    $ n = j
                    $ cuadro14n = False
                    $ cuadro14 = True
            elif errores == 4:
                $ j = gah 
                $ n = round(j,2)
                "la respuesta era [n]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro14n = False
                $ cuadro14 = True

    
    
    
    
    $ num = int(c-1)
    $ factorial = 1
    $ ffff = 0
    python: 
        for ffff in range(1,num + 1):
           factorial = factorial*ffff

    
    $ errores = 0    
    $ respuesta3 = renpy.input("¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
    $ j = float(respuesta3)
    $ j = round(j,2)
    $ gah = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta3]."
        $ jon = jon + 1
        $ l = j
        $ cuadro12n = False
        $ cuadro12 = True
                
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta3]."
            $ jon = jon + 1
            $ l = j
            $ cuadro12n = False
            $ cuadro12 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta3 = ""
                if errores == 1:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                if errores == 2:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                elif errores == 3:
                    $ respuesta3 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del numero promedio de clientes en la cola (lq)? Recuerde la formula {image=modelo3/lq.png}", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                elif errores == 4:
                    $ j = gah 
                    $ l = round(j,2)
                    "la respuesta era [l]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro12n = False
                    $ cuadro12 = True
    else:
        while j != gah:
            $ errores += 1
            $ respuesta3 = ""
            if errores == 1:
                $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta3)
                $ j = round(j,2)
                $ gah = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta3]."
                    $ jon = jon + 1
                    $ l = j
                    $ cuadro12n = False
                    $ cuadro12 = True
            if errores == 2:
                $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta3)
                $ j = round(j,2)
                $ gah = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta3]."
                    $ jon = jon + 1
                    $ l = j
                    $ cuadro12n = False
                    $ cuadro12 = True
            elif errores == 3:
                $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Recuerde la formula {image=modelo3/lq.png}", allow="0123456789-.")
                while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta3)
                $ j = round(j,2)
                $ gah = float(((e**(c+1))/(factorial*((c-e)**2)))*n)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta3]."
                    $ jon = jon + 1
                    $ l = j
                    $ cuadro12n = False
                    $ cuadro12 = True
            elif errores == 4:
                $ j = gah 
                $ l = round(j,2)
                "la respuesta era [l]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro12n = False
                $ cuadro12 = True

    
    
    
    
    $ errores = 0    
    $ respuesta4 = renpy.input("¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
    $ j = float(respuesta4)
    $ j = round(j,2)
    $ gah = float(l + e)
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta4]."
        $ jon = jon + 1
        $ m = j
        $ cuadro13n = False
        $ cuadro13 = True
                
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta3]."
            $ jon = jon + 1
            $ m = j
            $ cuadro13n = False
            $ cuadro13 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta4 = ""
                if errores == 1:
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta4)
                    $ j = round(j,2)
                    $ gah = float(l + e)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta4]."
                        $ jon = jon + 1
                        $ m = j
                        $ cuadro13n = False
                        $ cuadro13 = True
                if errores == 2:
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta4)
                    $ j = round(j,2)
                    $ gah = float(l + e)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta4]."
                        $ jon = jon + 1
                        $ m = j
                        $ cuadro13n = False
                        $ cuadro13 = True
                elif errores == 3:
                    $ respuesta4 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Recuerde la formula {image=modelo3/ls.png}", allow="0123456789-.")
                    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta4)
                    $ j = round(j,2)
                    $ gah = float(l + e)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta4]."
                        $ jon = jon + 1
                        $ m = j
                        $ cuadro13n = False
                        $ cuadro13 = True
                elif errores == 4:
                    $ j = gah 
                    $ m = round(j,2)
                    "la respuesta era [m]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro13n = False
                    $ cuadro13 = True
                
    else:
        while j != gah:
            $ errores += 1
            $ respuesta4 = ""
            if errores == 1:
                $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta4)
                $ j = round(j,2)
                $ gah = float(l + e)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta4]."
                    $ jon = jon + 1
                    $ m = j
                    $ cuadro13n = False
                    $ cuadro13 = True
            if errores == 2:
                $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta4)
                $ j = round(j,2)
                $ gah = float(l + e)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta4]."
                    $ jon = jon + 1
                    $ m = j
                    $ cuadro13n = False
                    $ cuadro13 = True
            elif errores == 3:
                $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Recuerde la formula {image=modelo3/ls.png}", allow="0123456789-.")
                while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta4)
                $ j = round(j,2)
                $ gah = float(l + e)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta4]."
                    $ jon = jon + 1
                    $ m = j
                    $ cuadro13n = False
                    $ cuadro13 = True
            elif errores == 4:
                $ j = gah 
                $ m = round(j,2)
                "la respuesta era [m]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro13n = False
                $ cuadro13 = True
            



    
    $ errores = 0    
    $ respuesta1 = renpy.input("¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
    $ j = float(respuesta1)
    $ j = round(j,2)
    $ gah = float(l/a)
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta1]."
        $ jon = jon + 1
        $ jx = j
        $ cuadro10n = False
        $ cuadro10 = True
                    
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta1]."
            $ jon = jon + 1
            $ jx = j
            $ cuadro10n = False
            $ cuadro10 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta1 = ""
                if errores == 1:
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta1)
                    $ j = round(j,2)
                    $ gah = float(l/a)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta1]."
                        $ jon = jon + 1
                        $ jx = j
                        $ cuadro10n = False
                        $ cuadro10 = True
                if errores == 2:
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta1)
                    $ j = round(j,2)
                    $ gah = float(l/a)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta1]."
                        $ jon = jon + 1
                        $ jx = j
                        $ cuadro10n = False
                        $ cuadro10 = True
                elif errores == 3:
                    $ respuesta1 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Recuerde la formula {image=modelo3/wq.png}", allow="0123456789-.")
                    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta1)
                    $ j = round(j,2)
                    $ gah = float(l/a)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta1]."
                        $ jon = jon + 1
                        $ jx = j
                        $ cuadro10n = False
                        $ cuadro10 = True
                elif errores == 4:
                    $ j = gah 
                    $ jx = round(j,2)
                    "la respuesta era [jx]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro10n = False
                    $ cuadro10 = True

    else:
        while j != gah:
            $ errores += 1
            $ respuesta1 = ""
            if errores == 1:
                $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta1)
                $ j = round(j,2)
                $ gah = float(l/a)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta1]."
                    $ jon = jon + 1
                    $ jx = j
                    $ cuadro10n = False
                    $ cuadro10 = True
            if errores == 2:
                $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta1)
                $ j = round(j,2)
                $ gah = float(l/a)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta1]."
                    $ jon = jon + 1
                    $ jx = j
                    $ cuadro10n = False
                    $ cuadro10 = True
            elif errores == 3:
                $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Recuerde la formula {image=modelo3/wq.png}", allow="0123456789-.")
                while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta1)
                $ j = round(j,2)
                $ gah = float(l/a)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta1]."
                    $ jon = jon + 1
                    $ jx = j
                    $ cuadro10n = False
                    $ cuadro10 = True
            elif errores == 4:
                $ j = gah 
                $ jx = round(j,2)
                "la respuesta era [jx]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro10n = False
                $ cuadro10 = True
                
            
            
            
    $ errores = 0    
    $ respuesta2 = renpy.input("¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
    $ j = float(respuesta2)
    $ j = round(j,2)
    $ gah = float(jx+(1/b))
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta2]."
        $ jon = jon + 1
        $ k = j
        $ cuadro11n = False
        $ cuadro11 = True
                
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta2]."
            $ jon = jon + 1
            $ k = j
            $ cuadro11n = False
            $ cuadro11 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta2 = ""
                if errores == 1:
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)??", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta2)
                    $ j = round(j,2)
                    $ gah = float(jx+(1/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta2]."
                        $ jon = jon + 1
                        $ k = j
                        $ cuadro11n = False
                        $ cuadro11 = True
                if errores == 2:
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta2)
                    $ j = round(j,2)
                    $ gah = float(jx+(1/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta2]."
                        $ jon = jon + 1
                        $ k = j
                        $ cuadro11n = False
                        $ cuadro11 = True
                elif errores == 3:
                    $ respuesta2 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Recuerde la formula {image=modelo3/ws.png}", allow="0123456789-.")
                    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta2)
                    $ j = round(j,2)
                    $ gah = float(jx+(1/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta2]."
                        $ jon = jon + 1
                        $ k = j
                        $ cuadro11n = False
                        $ cuadro11 = True
                elif errores == 4:
                    $ j = gah 
                    $ k = round(j,2)
                    "la respuesta era [k]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro11n = False
                    $ cuadro11 = True
                
    else: 
        while j != gah:
            $ errores += 1
            $ respuesta2 = ""
            if errores == 1:
                $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta2)
                $ j = round(j,2)
                $ gah = float(jx+(1/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta2]."
                    $ jon = jon + 1
                    $ k = j
                    $ cuadro11n = False
                    $ cuadro11 = True
            if errores == 2:
                $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta2)
                $ j = round(j,2)
                $ gah = float(jx+(1/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta2]."
                    $ jon = jon + 1
                    $ k = j
                    $ cuadro11n = False
                    $ cuadro11 = True
            elif errores == 3:
                $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Recuerde la formula {image=modelo3/ws.png}", allow="0123456789-.")
                while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta2)
                $ j = round(j,2)
                $ gah = float(jx+(1/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta2]."
                    $ jon = jon + 1
                    $ k = j
                    $ cuadro11n = False
                    $ cuadro11 = True
            elif errores == 4:
                $ j = gah 
                $ k = round(j,2)
                "la respuesta era [k]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro11n = False
                $ cuadro11 = True


    $ puntuacion = round(puntuacion,2)
    
    if puntuacion == 20:
        "ha resuelto todos los ejercicios... ¡¡¡felicidades!!!"
    
    elif puntuacion == 0:
        "No ha logrado resolver ningun ejercicio... reprueba la materia."
        
    elif puntuacion < 20 and puntuacion > 0:
        "Se ha terminado el ejercicio. Su puntuación fue [puntuacion]"
        
    
    if tyrion == 1 and jon == 1:
        "Usted se equivocó [tyrion] vez y resolvió [jon] problema de los 5 que hay en este ejercicio."
    elif tyrion == 1:
        "Usted se equivocó [tyrion] vez y resolvió [jon] problemas de los 5 que hay en este ejercicio."
    elif jon == 1:
        "Usted se equivocó [tyrion] veces y resolvió [jon] problema de los 5 que hay en este ejercicio."
    else:
        "Usted se equivocó [tyrion] veces y resolvió [jon] problemas de los 5 que hay en este ejercicio."


            

    $ cuadro1 = False
    $ cuadro1n = False
    $ cuadro2 = False
    $ cuadro2n = False
    $ cuadro3 = False
    $ cuadro3n = False
    $ cuadro4 = False
    $ cuadro4n = False
    $ cuadro5 = False
    $ cuadro5n = False
    $ cuadro6 = False
    $ cuadro6n = False
    $ cuadro7 = False
    $ cuadro7n = False
    $ cuadro8 = False
    $ cuadro8n = False
    $ cuadro9 = False
    $ cuadro9n = False
    $ cuadro10 = False
    $ cuadro10n = False
    $ cuadro11 = False
    $ cuadro11n = False
    $ cuadro12 = False
    $ cuadro12n = False
    $ cuadro13 = False
    $ cuadro13n = False
    $ cuadro14 = False
    $ cuadro14n = False
    $ cuadro15 = False
    $ cuadro15n = False
    $ cuadro16 = False
    $ cuadro16n = False
    $ cuadro18 = False
    $ cuadro18n = False
    
    scene fondo with dissolve
    hide modelo23fondo2 with dissolve
                
    jump contador_de_ejercicios
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
label ejercicio_paralelo2:

    menu:
        "Resolverlo yo.":
            jump ejercicio_paralelo2_parte2_usuario
        
        "Dejar que el programa lo resuelva":
            jump ejercicio_paralelo2_parte2_computadora
        
        "¿Desea resolver usted el problema o que este programa lo resuelva por usted?"

                
label ejercicio_paralelo2_parte2_computadora:
    
    #$ e = a/(b*c)

    if (e/c) != 1:
        
        $ num = int(clientes)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ sumatoria = 0
        $ c = int(c)
        $ nnn = 0
        python:
            for nnn in range(0,(c-1)+1):
                sumatoria = sumatoria+((e**clientes)/factorial)
                
        $ num = int(c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
                       
        
        $ n = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
        
    elif (e/c) == 1:
        
        $ num = int(clientes)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ sumatoria = 0
        $ c = int(c)
        $ nnn = 0
        python:
            for nnn in range(0,(c-1)+1):
                sumatoria = sumatoria+((e**clientes)/factorial)

                
        $ num = int(c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ n = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
        
        
        
#___________________________________________________________________________________________________________
    
    
    if c >= clientes and clientes >= 0:
        
        $ num = int(clientes)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ gintoki = float((((e**clientes)/factorial))*n)
        
        
        
        
    
    elif p >= clientes and clientes >= c:
        
        $ num = int(c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
               
        $ gintoki = float(((e**clientes)/(factorial*(c**(clientes-c))))*n)
        

    $ takasugi = float(a*(1-gintoki))
        
    
#___________________________________________________________________________________________________________________
    
    
    if (e/c) != 1:
        
        $ num = int(c-1)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
               
        
        $ l = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
        
               
    elif (e/c) == 1:
        
        $ num = int(2*c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ l = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))

    $ m = float(l + (takasugi/b))
    
    $ jx = float((m/takasugi)-(1/b))
    
    $ k = float(m/takasugi)
    
    scene modelo4fondo1 with dissolve
    hide fondo with dissolve
                

    if a != 0:
        $ cuadro1 = True
    else:
        $ cuadro1n = True
                
                
                
    if b != 0:
        $ cuadro2 = True
    else:
        $ cuadro2n = True
                

    if c != 0:
        $ cuadro3 = True
    else:
        $ cuadro3n = True
                
                
    if e != 0:
        $ cuadro5 = True
    else:
        $ cuadro5n = True
                    
                    
    if jx != 0:
        $ cuadro10 = True
    else:
        $ cuadro10n = True
                    
                    
          
                
    if k != 0:
        $ cuadro11 = True
    else:
        $ cuadro11n = True

            
            
    if l != 0:
        $ cuadro12 = True
    else:
        $ cuadro12n = True
                    
                    
                    
                    
    if m != 0:
        $ cuadro13 = True
    else:
        $ cuadro13n = True
                    
                    
                    
                    
    if n != 0:
        $ cuadro14 = True
    else:
        $ cuadro14n = True
                    
       
                                    
    if p != 0:
        $ cuadro16 = True
    else:
        $ cuadro16n = True
        
        
        
        
            
    if clientes != 0:
        $ cuadro17 = True
    else:
        $ cuadro17 = False
        
        
        
        
    "Aquí están los resultados."
    
    $ cuadro1 = False
    $ cuadro1n = False
    $ cuadro2 = False
    $ cuadro2n = False
    $ cuadro3 = False
    $ cuadro3n = False
    $ cuadro4 = False
    $ cuadro4n = False
    $ cuadro5 = False
    $ cuadro5n = False
    $ cuadro6 = False
    $ cuadro6n = False
    $ cuadro7 = False
    $ cuadro7n = False
    $ cuadro8 = False
    $ cuadro8n = False
    $ cuadro9 = False
    $ cuadro9n = False
    $ cuadro10 = False
    $ cuadro10n = False
    $ cuadro11 = False
    $ cuadro11n = False
    $ cuadro12 = False
    $ cuadro12n = False
    $ cuadro13 = False
    $ cuadro13n = False
    $ cuadro14 = False
    $ cuadro14n = False
    $ cuadro15 = False
    $ cuadro15n = False
    $ cuadro16 = False
    $ cuadro16n = False
    $ cuadro17 = False
    $ cuadro17n = False
    
    scene fondo with dissolve
    hide modelo4fondo1 with dissolve
                
    jump contador_de_ejercicios

    
    
label ejercicio_paralelo2_parte2_usuario:
    
    $ puntuacion = long(20)
    $ tyrion = 0
    $ jon = 0
    
    "Resuelva el siguiente ejercicio, recuerde que solo puede escribir dos decimales."
    
    scene modelo4fondo2 with dissolve
    hide fondo with dissolve
                
    $ respuesta1 = ""
    $ respuesta2 = ""
    $ respuesta3 = ""
    $ respuesta4 = ""
    $ respuesta5 = ""
    $ respuesta6 = ""
    $ respuesta7 = ""
    $ respuesta8 = ""
    $ respuesta9 = ""
    $ respuesta10 = ""
    $ respuesta11 = ""
    $ respuesta12 = ""
    $ respuesta13 = ""
    $ respuesta14 = ""
                

    if a != 0:
        $ cuadro1 = True
    else:
        $ cuadro1n = True
                
                
                
    if b != 0:
        $ cuadro2 = True
    else:
        $ cuadro2n = True
                

    if c != 0:
        $ cuadro3 = True
    else:
        $ cuadro3n = True
                
                
    if e != 0:
        $ cuadro5 = True
    else:
        $ cuadro5n = True
                    
                    
    if jx != 0:
        $ cuadro10 = True
    else:
        $ cuadro10n = True
                    
                    
          
                
    if k != 0:
        $ cuadro11 = True
    else:
        $ cuadro11n = True

            
            
    if l != 0:
        $ cuadro12 = True
    else:
        $ cuadro12n = True
                    
                    
                    
                    
    if m != 0:
        $ cuadro13 = True
    else:
        $ cuadro13n = True
                    
                    
                    
                    
    if n != 0:
        $ cuadro14 = True
    else:
        $ cuadro14n = True
                    
    
                                    
    if p != 0:
        $ cuadro16 = True
    else:
        $ cuadro16n = True
        
        
        
        
            
    if clientes != 0:
        $ cuadro17 = True
    else:
        $ cuadro17 = False
        

#______________________________________________________________________________________________________________________________________________



    if (e/c) != 1:
        
        $ num = int(clientes)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ sumatoria = 0
        $ c = int(c)
        $ nnn = 0
        python:
            for nnn in range(0,(c-1)+1):
                sumatoria = sumatoria+((e**clientes)/factorial)
                
        $ num = int(c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        $ errores = 0    
        $ respuesta5 = renpy.input("¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
        $ j = float(respuesta5)
        $ j = round(j,2)
        $ gah = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
        $ gah = round(gah,2)
        "[gah]"
        if j == gah:
            "Correcto, la respuesta es [respuesta5]."
            $ jon = jon + 1
            $ n = j
            $ cuadro14n = False
            $ cuadro14 = True
                    
        elif gah <= 0:
            if j == gah:
                "Correcto, la respuesta es [respuesta5]."
                $ jon = jon + 1
                $ n = j
                $ cuadro14n = False
                $ cuadro14 = True
            else:
                while j != gah:
                    $ errores += 1
                    $ respuesta5 = ""
                    if errores == 1:
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta5)
                        $ j = round(j,2)
                        $ gah = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta5]."
                            $ jon = jon + 1
                            $ n = j
                            $ cuadro14n = False
                            $ cuadro14 = True
                    if errores == 2:
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta5)
                        $ j = round(j,2)
                        $ gah = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta5]."
                            $ jon = jon + 1
                            $ n = j
                            $ cuadro14n = False
                            $ cuadro14 = True
                    elif errores == 3:
                        $ respuesta5 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Recuerde la formula {image=modelo4/po.png}", allow="0123456789-.")
                        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta5)
                        $ j = round(j,2)
                        $ gah = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta5]."
                            $ jon = jon + 1
                            $ n = j
                            $ cuadro14n = False
                            $ cuadro14 = True
                    elif errores == 4:
                        $ j = gah 
                        $ n = round(j,2)
                        "la respuesta era [n]"
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ cuadro14n = False
                        $ cuadro14 = True
                    
        else:
            while j != gah:
                $ errores += 1
                $ respuesta5 = ""
                if errores == 1:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                if errores == 2:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                elif errores == 3:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Recuerde la formula {image=modelo4/po.png}", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+(((e**c)*(1-((e/c)**(p-c+1))))/(factorial*(1-(e/c)))))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                elif errores == 4:
                    $ j = gah 
                    $ n = round(j,2)
                    "la respuesta era [n]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro14n = False
                    $ cuadro14 = True
    elif (e/c) == 1:
        
        $ num = int(clientes)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ sumatoria = 0
        $ c = int(c)
        $ nnn = 0
        python:
            for nnn in range(0,(c-1)+1):
                sumatoria = sumatoria+((e**clientes)/factorial)

                
        $ num = int(c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        $ errores = 0    
        $ respuesta5 = renpy.input("¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
        $ j = float(respuesta5)
        $ j = round(j,2)
        $ gah = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
        $ gah = round(gah,2)
        "[gah]"
        if j == gah:
            "Correcto, la respuesta es [respuesta5]."
            $ jon = jon + 1
            $ n = j
            $ cuadro14n = False
            $ cuadro14 = True
                    
        elif gah <= 0:
            if j == gah:
                "Correcto, la respuesta es [respuesta5]."
                $ jon = jon + 1
                $ n = j
                $ cuadro14n = False
                $ cuadro14 = True
            else:
                while j != gah:
                    $ errores += 1
                    $ respuesta5 = ""
                    if errores == 1:
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta5)
                        $ j = round(j,2)
                        $ gah = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta5]."
                            $ jon = jon + 1
                            $ n = j
                            $ cuadro14n = False
                            $ cuadro14 = True
                    if errores == 2:
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta5)
                        $ j = round(j,2)
                        $ gah = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta5]."
                            $ jon = jon + 1
                            $ n = j
                            $ cuadro14n = False
                            $ cuadro14 = True
                    elif errores == 3:
                        $ respuesta5 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Recuerde la formula {image=modelo4/po.png}", allow="0123456789-.")
                        while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                            $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta5)
                        $ j = round(j,2)
                        $ gah = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta5]."
                            $ jon = jon + 1
                            $ n = j
                            $ cuadro14n = False
                            $ cuadro14 = True
                    elif errores == 4:
                        $ j = gah 
                        $ n = round(j,2)
                        "la respuesta era [n]"
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ cuadro14n = False
                        $ cuadro14 = True
                    
        else:
            while j != gah:
                $ errores += 1
                $ respuesta5 = ""
                if errores == 1:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                if errores == 2:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                elif errores == 3:
                    $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)? Recuerde la formula {image=modelo4/po.png}", allow="0123456789-.")
                    while respuesta5 == "" or respuesta5 == "." or respuesta5 == "-":
                        $ respuesta5 = renpy.input("Respuesta incorrecta ¿cual es el valor de la probabilidad de que el sistema este vacio (po)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta5)
                    $ j = round(j,2)
                    $ gah = float((sumatoria+(((e**c)/factorial)*(p-c+1)))**(-1))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta5]."
                        $ jon = jon + 1
                        $ n = j
                        $ cuadro14n = False
                        $ cuadro14 = True
                elif errores == 4:
                    $ j = gah 
                    $ n = round(j,2)
                    "la respuesta era [n]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro14n = False
                    $ cuadro14 = True
               
               
            

#___________________________________________________________________________________________________________
    
    
    if c >= clientes and clientes >= 0:
        
        $ num = int(clientes)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        
        $ gintoki = float((((e**clientes)/factorial))*n)
        
    
    elif p >= clientes and clientes >= c:
        
        $ num = int(c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
               
        $ gintoki = float((((e**clientes)/(factorial*(c**(clientes-c)))))*n)
            
    
    
    
    $ takasugi = float(a*(1-gintoki))
        
    
#___________________________________________________________________________________________________________________





    if (e/c) != 1:
        
        $ num = int(c-1)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        $ errores = 0    
        $ respuesta3 = renpy.input("¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
        $ j = float(respuesta3)
        $ j = round(j,2)
        $ gah = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
        $ gah = round(gah,2)
        "[gah]"
        if j == gah:
            "Correcto, la respuesta es [respuesta3]."
            $ jon = jon + 1
            $ l = j
            $ cuadro12n = False
            $ cuadro12 = True
                    
        elif gah <= 0:
            if j == gah:
                "Correcto, la respuesta es [respuesta3]."
                $ jon = jon + 1
                $ l = j
                $ cuadro12n = False
                $ cuadro12 = True
            else:
                while j != gah:
                    $ errores += 1
                    $ respuesta3 = ""
                    if errores == 1:
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta3)
                        $ j = round(j,2)
                        $ gah = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta3]."
                            $ jon = jon + 1
                            $ l = j
                            $ cuadro12n = False
                            $ cuadro12 = True
                    if errores == 2:
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta3)
                        $ j = round(j,2)
                        $ gah = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta3]."
                            $ jon = jon + 1
                            $ l = j
                            $ cuadro12n = False
                            $ cuadro12 = True
                    elif errores == 3:
                        $ respuesta3 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del numero promedio de clientes en la cola (lq)? Recuerde la formula {image=modelo4/lq.png}", allow="0123456789-.")
                        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta3)
                        $ j = round(j,2)
                        $ gah = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta3]."
                            $ jon = jon + 1
                            $ l = j
                            $ cuadro12n = False
                            $ cuadro12 = True
                    elif errores == 4:
                        $ j = gah 
                        $ l = round(j,2)
                        "la respuesta era [l]"
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ cuadro12n = False
                        $ cuadro12 = True

                    
        else:
            while j != gah:
                $ errores += 1
                $ respuesta3 = ""
                if errores == 1:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                if errores == 2:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                elif errores == 3:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Recuerde la formula {image=modelo4/lq.png}", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float((n*((e**(c+1))/factorial*((c-e)**2)))*(1-((e/c)**(p-c))-((p-c)*((e/c)**(p-c)))*(1-(e/c))))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                elif errores == 4:
                    $ j = gah 
                    $ l = round(j,2)
                    "la respuesta era [l]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro12n = False
                    $ cuadro12 = True
    elif (e/c) == 1:
        
        $ num = int(2*c)
        $ factorial = 1
        $ ffff = 0
        python: 
            for ffff in range(1,num + 1):
               factorial = factorial*ffff
        $ errores = 0    
        $ respuesta3 = renpy.input("¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
        $ j = float(respuesta3)
        $ j = round(j,2)
        $ gah = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))
        $ gah = round(gah,2)
        "[gah]"
        if j == gah:
            "Correcto, la respuesta es [respuesta3]."
            $ jon = jon + 1
            $ l = j
            $ cuadro12n = False
            $ cuadro12 = True
                    
        elif gah <= 0:
            if j == gah:
                "Correcto, la respuesta es [respuesta3]."
                $ jon = jon + 1
                $ l = j
                $ cuadro12n = False
                $ cuadro12 = True
            else:
                while j != gah:
                    $ errores += 1
                    $ respuesta3 = ""
                    if errores == 1:
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta3)
                        $ j = round(j,2)
                        $ gah = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta3]."
                            $ jon = jon + 1
                            $ l = j
                            $ cuadro12n = False
                            $ cuadro12 = True
                    if errores == 2:
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta3)
                        $ j = round(j,2)
                        $ gah = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta3]."
                            $ jon = jon + 1
                            $ l = j
                            $ cuadro12n = False
                            $ cuadro12 = True
                    elif errores == 3:
                        $ respuesta3 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del numero promedio de clientes en la cola (lq)? Recuerde la formula {image=modelo4/lq.png}", allow="0123456789-.")
                        while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                            $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ tyrion = tyrion + 1
                        $ j = float(respuesta3)
                        $ j = round(j,2)
                        $ gah = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))
                        $ gah = round(gah,2)
                        if j == gah:
                            "Correcto, la respuesta es [respuesta3]."
                            $ jon = jon + 1
                            $ l = j
                            $ cuadro12n = False
                            $ cuadro12 = True
                    elif errores == 4:
                        $ j = gah 
                        $ l = round(j,2)
                        "la respuesta era [l]"
                        $ puntuacion -= long(1.6666666666666666666666666666667)
                        $ cuadro12n = False
                        $ cuadro12 = True

                    
        else:
            while j != gah:
                $ errores += 1
                $ respuesta3 = ""
                if errores == 1:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                if errores == 2:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                elif errores == 3:
                    $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)? Recuerde la formula {image=modelo4/lq.png}", allow="0123456789-.")
                    while respuesta3 == "" or respuesta3 == "." or respuesta3 == "-":
                        $ respuesta3 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en la cola (lq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta3)
                    $ j = round(j,2)
                    $ gah = float(n*(((e**c)*(p-c)*(p-c+1))/factorial))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ l = j
                        $ cuadro12n = False
                        $ cuadro12 = True
                elif errores == 4:
                    $ j = gah 
                    $ l = round(j,2)
                    "la respuesta era [l]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro12n = False
                    $ cuadro12 = True




    $ errores = 0    
    $ respuesta4 = renpy.input("¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
    $ j = float(respuesta4)
    $ j = round(j,2)
    $ gah = float(l + (takasugi/b))
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta4]."
        $ jon = jon + 1
        $ m = j
        $ cuadro13n = False
        $ cuadro13 = True
                
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta3]."
            $ jon = jon + 1
            $ m = j
            $ cuadro13n = False
            $ cuadro13 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta4 = ""
                if errores == 1:
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta4)
                    $ j = round(j,2)
                    $ gah = float(l + (takasugi/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ m = j
                        $ cuadro13n = False
                        $ cuadro13 = True
                if errores == 2:
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta4)
                    $ j = round(j,2)
                    $ gah = float(l + (takasugi/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ m = j
                        $ cuadro13n = False
                        $ cuadro13 = True
                elif errores == 3:
                    $ respuesta4 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Recuerde la formula {image=modelo4/ls.png}", allow="0123456789-.")
                    while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                        $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta4)
                    $ j = round(j,2)
                    $ gah = float(l + (takasugi/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta3]."
                        $ jon = jon + 1
                        $ m = j
                        $ cuadro13n = False
                        $ cuadro13 = True
                elif errores == 4:
                    $ j = gah 
                    $ m = round(j,2)
                    "la respuesta era [m]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro13n = False
                    $ cuadro13 = True

                
    else:
        while j != gah:
            $ errores += 1
            $ respuesta4 = ""
            if errores == 1:
                $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta4)
                $ j = round(j,2)
                $ gah = float(l + (takasugi/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta3]."
                    $ jon = jon + 1
                    $ m = j
                    $ cuadro13n = False
                    $ cuadro13 = True
            if errores == 2:
                $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta4)
                $ j = round(j,2)
                $ gah = float(l + (takasugi/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta3]."
                    $ jon = jon + 1
                    $ m = j
                    $ cuadro13n = False
                    $ cuadro13 = True
            elif errores == 3:
                $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)? Recuerde la formula {image=modelo4/ls.png}", allow="0123456789-.")
                while respuesta4 == "" or respuesta4 == "." or respuesta4 == "-":
                    $ respuesta4 = renpy.input("Respuesta incorrecta ¿cual es el valor del numero promedio de clientes en el sistema (ls)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta4)
                $ j = round(j,2)
                $ gah = float(l + (takasugi/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta3]."
                    $ jon = jon + 1
                    $ m = j
                    $ cuadro13n = False
                    $ cuadro13 = True
            elif errores == 4:
                $ j = gah 
                $ m = round(j,2)
                "la respuesta era [m]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro13n = False
                $ cuadro13 = True

            




    $ errores = 0    
    $ respuesta1 = renpy.input("¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
    $ j = float(respuesta1)
    $ j = round(j,2)
    $ gah = float((m/takasugi)-(1/b))
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta1]."
        $ jon = jon + 1
        $ jx = j
        $ cuadro10n = False
        $ cuadro10 = True
                    
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta1]."
            $ jon = jon + 1
            $ jx = j
            $ cuadro10n = False
            $ cuadro10 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta1 = ""
                if errores == 1:
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta1)
                    $ j = round(j,2)
                    $ gah = float((m/takasugi)-(1/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta1]."
                        $ jon = jon + 1
                        $ jx = j
                        $ cuadro10n = False
                        $ cuadro10 = True
                if errores == 2:
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta1)
                    $ j = round(j,2)
                    $ gah = float((m/takasugi)-(1/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta1]."
                        $ jon = jon + 1
                        $ jx = j
                        $ cuadro10n = False
                        $ cuadro10 = True
                elif errores == 3:
                    $ respuesta1 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Recuerde la formula {image=modelo4/wq.png}", allow="0123456789-.")
                    while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                        $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta1)
                    $ j = round(j,2)
                    $ gah = float((m/takasugi)-(1/b))
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta1]."
                        $ jon = jon + 1
                        $ jx = j
                        $ cuadro10n = False
                        $ cuadro10 = True
                elif errores == 4:
                    $ j = gah 
                    $ jx = round(j,2)
                    "la respuesta era [jx]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro10n = False
                    $ cuadro10 = True

    else:
        while j != gah:
            $ errores += 1
            $ respuesta1 = ""
            if errores == 1:
                $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta1)
                $ j = round(j,2)
                $ gah = float((m/takasugi)-(1/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta1]."
                    $ jon = jon + 1
                    $ jx = j
                    $ cuadro10n = False
                    $ cuadro10 = True
            if errores == 2:
                $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta1)
                $ j = round(j,2)
                $ gah = float((m/takasugi)-(1/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta1]."
                    $ jon = jon + 1
                    $ jx = j
                    $ cuadro10n = False
                    $ cuadro10 = True
            elif errores == 3:
                $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)? Recuerde la formula {image=modelo4/wq.png}", allow="0123456789-.")
                while respuesta1 == "" or respuesta1 == "." or respuesta1 == "-":
                    $ respuesta1 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en la cola (wq)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta1)
                $ j = round(j,2)
                $ gah = float((m/takasugi)-(1/b))
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta1]."
                    $ jon = jon + 1
                    $ jx = j
                    $ cuadro10n = False
                    $ cuadro10 = True
            elif errores == 4:
                $ j = gah 
                $ jx = round(j,2)
                "la respuesta era [jx]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro10n = False
                $ cuadro10 = True
                
            
            
            
    $ errores = 0       
    $ respuesta2 = renpy.input("¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
    $ j = float(respuesta2)
    $ j = round(j,2)
    $ gah = float(m/takasugi)
    $ gah = round(gah,2)
    "[gah]"
    if j == gah:
        "Correcto, la respuesta es [respuesta2]."
        $ jon = jon + 1
        $ k = j
        $ cuadro11n = False
        $ cuadro11 = True
                
    elif gah <= 0:
        if j == gah:
            "Correcto, la respuesta es [respuesta2]."
            $ jon = jon + 1
            $ k = j
            $ cuadro11n = False
            $ cuadro11 = True
        else:
            while j != gah:
                $ errores += 1
                $ respuesta2 = ""
                if errores == 1:
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)??", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta2)
                    $ j = round(j,2)
                    $ gah = float(m/takasugi)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta2]."
                        $ jon = jon + 1
                        $ k = j
                        $ cuadro11n = False
                        $ cuadro11 = True
                if errores == 2:
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta2)
                    $ j = round(j,2)
                    $ gah = float(m/takasugi)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta2]."
                        $ jon = jon + 1
                        $ k = j
                        $ cuadro11n = False
                        $ cuadro11 = True
                elif errores == 3:
                    $ respuesta2 = renpy.input("Respuesta incorrecta, ultimo intento ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Recuerde la formula {image=modelo4/ws.png}", allow="0123456789-.")
                    while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                        $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ tyrion = tyrion + 1
                    $ j = float(respuesta2)
                    $ j = round(j,2)
                    $ gah = float(m/takasugi)
                    $ gah = round(gah,2)
                    if j == gah:
                        "Correcto, la respuesta es [respuesta2]."
                        $ jon = jon + 1
                        $ k = j
                        $ cuadro11n = False
                        $ cuadro11 = True
                elif errores == 4:
                    $ j = gah 
                    $ k = round(j,2)
                    "la respuesta era [k]"
                    $ puntuacion -= long(1.6666666666666666666666666666667)
                    $ cuadro11n = False
                    $ cuadro11 = True
                
    else: 
        while j != gah:
            $ errores += 1
            $ respuesta2 = ""
            if errores == 1:
                $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallo de tres.", allow="0123456789-.")
                while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta2)
                $ j = round(j,2)
                $ gah = float(m/takasugi)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta2]."
                    $ jon = jon + 1
                    $ k = j
                    $ cuadro11n = False
                    $ cuadro11 = True
            if errores == 2:
                $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Tiene [errores] fallos de tres.", allow="0123456789-.")
                while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta2)
                $ j = round(j,2)
                $ gah = float(m/takasugi)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta2]."
                    $ jon = jon + 1
                    $ k = j
                    $ cuadro11n = False
                    $ cuadro11 = True
            elif errores == 3:
                $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)? Recuerde la formula {image=modelo4/ws.png}", allow="0123456789-.")
                while respuesta2 == "" or respuesta2 == "." or respuesta2 == "-":
                    $ respuesta2 = renpy.input("Respuesta incorrecta ¿cual es el valor del tiempo promedio de un cliente en el sistema (ws)?", allow="0123456789-.")
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ tyrion = tyrion + 1
                $ j = float(respuesta2)
                $ j = round(j,2)
                $ gah = float(m/takasugi)
                $ gah = round(gah,2)
                if j == gah:
                    "Correcto, la respuesta es [respuesta2]."
                    $ jon = jon + 1
                    $ k = j
                    $ cuadro11n = False
                    $ cuadro11 = True
            elif errores == 4:
                $ j = gah 
                $ k = round(j,2)
                "la respuesta era [k]"
                $ puntuacion -= long(1.6666666666666666666666666666667)
                $ cuadro11n = False
                $ cuadro11 = True


            
            
            
    $ puntuacion = round(puntuacion,2)
    
    if puntuacion == 20:
        "ha resuelto todos los ejercicios... ¡¡¡felicidades!!!"
    
    elif puntuacion == 0:
        "No ha logrado resolver ningun ejercicio... reprueba la materia."
        
    elif puntuacion < 20 and puntuacion > 0:
        "Se ha terminado el ejercicio. Su puntuación fue [puntuacion]"
        
    
    if tyrion == 1 and jon == 1:
        "Usted se equivocó [tyrion] vez y resolvió [jon] problema de los 5 que hay en este ejercicio."
    elif tyrion == 1:
        "Usted se equivocó [tyrion] vez y resolvió [jon] problemas de los 5 que hay en este ejercicio."
    elif jon == 1:
        "Usted se equivocó [tyrion] veces y resolvió [jon] problema de los 5 que hay en este ejercicio."
    else:
        "Usted se equivocó [tyrion] veces y resolvió [jon] problemas de los 5 que hay en este ejercicio."
    
          

    $ cuadro1 = False
    $ cuadro1n = False
    $ cuadro2 = False
    $ cuadro2n = False
    $ cuadro3 = False
    $ cuadro3n = False
    $ cuadro4 = False
    $ cuadro4n = False
    $ cuadro5 = False
    $ cuadro5n = False
    $ cuadro6 = False
    $ cuadro6n = False
    $ cuadro7 = False
    $ cuadro7n = False
    $ cuadro8 = False
    $ cuadro8n = False
    $ cuadro9 = False
    $ cuadro9n = False
    $ cuadro10 = False
    $ cuadro10n = False
    $ cuadro11 = False
    $ cuadro11n = False
    $ cuadro12 = False
    $ cuadro12n = False
    $ cuadro13 = False
    $ cuadro13n = False
    $ cuadro14 = False
    $ cuadro14n = False
    $ cuadro15 = False
    $ cuadro15n = False
    $ cuadro16 = False
    $ cuadro16n = False
    $ cuadro17 = False
    $ cuadro17n = False
    
    scene fondo with dissolve
    hide modelo4fondo2 with dissolve
                
    jump contador_de_ejercicios

    return 
    
    