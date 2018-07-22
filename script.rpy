# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

image fondo = "screenshot00102.jpg"
image modelo1fondo1 = "modelo 1 resultados.jpg"
image modelo1fondo2 = "modelo 1 valores.jpg"
image modelo23fondo1 = "modelo 2 y 3 resultados.jpg"
image modelo23fondo2 = "modelo 2 y 3 valores.jpg"
image modelo4fondo1 = "modelo 4 resultados.jpg"
image modelo4fondo2 = "modelo 4 valores.jpg"

image esquema1 = "colas_esquema2.png" 
image esquema2 = "colas_esquema.png"
image esquema3 = "poisson_esquema.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define e = Character('Eileen', color="#c8ffc8")


init:
    $ cuadro1 = False

    python hide:
        def cuadro1_overlay():
            if cuadro1:
                ui.text("{size=-11}Tasa promedio de elementos en el sistema (λ) = [a] [q].{/size}",
                        xpos=4,
                        ypos=90,
                        xysize=(184, 73))

        config.overlay_functions.append(cuadro1_overlay)
        
        
init:
    $ cuadro1n = False

    python hide:
        def cuadro1n_overlay():
            if cuadro1n:
                ui.text("{size=-11}Tasa promedio de elementos en el sistema (λ) = ?.{/size}",
                        xpos=4,
                        ypos=90,
                        xysize=(184, 73))

        config.overlay_functions.append(cuadro1n_overlay)
        
        
init:
    $ cuadro2 = False

    python hide:
        def cuadro2_overlay():
            if cuadro2:
                ui.text("{size=-11}Tasa promedio de servicios (μ) = [b] [r].{/size}",
                        xpos=196,
                        ypos=88,
                        xysize=(219, 75))

        config.overlay_functions.append(cuadro2_overlay)
        
        
init:
    $ cuadro2n = False

    python hide:
        def cuadro2n_overlay():
            if cuadro2n:
                ui.text("{size=-11}Tasa promedio de servicios (μ) = ?.{/size}",
                        xpos=196,
                        ypos=88,
                        xysize=(219, 75))

        config.overlay_functions.append(cuadro2n_overlay)
        
        
init:
    $ cuadro3 = False

    python hide:
        def cuadro3_overlay():
            if cuadro3:
                ui.text("{size=-11}Numero de servidores (c) = [c].{/size}",
                        xpos=438,
                        ypos=87,
                        xysize=(177, 74))

        config.overlay_functions.append(cuadro3_overlay)
        
        
init:
    $ cuadro3n = False

    python hide:
        def cuadro3n_overlay():
            if cuadro3n:
                ui.text("{size=-11}Numero de servidores (c) = ?.{/size}",
                        xpos=438,
                        ypos=87,
                        xysize=(177, 74))

        config.overlay_functions.append(cuadro3n_overlay)
        

init:
    $ cuadro5 = False

    python hide:
        def cuadro5_overlay():
            if cuadro5:
                ui.text("{size=-11}Intensidad del trafico (ρ) = [e].{/size}",
                        xpos=622,
                        ypos=89,
                        xysize=(176, 72))

        config.overlay_functions.append(cuadro5_overlay)
        
        
        
init:
    $ cuadro5n = False

    python hide:
        def cuadro5n_overlay():
            if cuadro5n:
                ui.text("{size=-11}Intensidad del trafico (ρ) = ?.{/size}",
                        xpos=622,
                        ypos=89,
                        xysize=(176, 72))
                
        config.overlay_functions.append(cuadro5n_overlay)
        

init:
    $ cuadro10 = False

    python hide:
        def cuadro10_overlay():
            if cuadro10:
                ui.text("{size=-11}Tiempo promedio de un cliente en la cola (wq) = [jx].{/size}",
                        xpos=1,
                        ypos=184,
                        xysize=(186, 71))

        config.overlay_functions.append(cuadro10_overlay)
        
        
init:
    $ cuadro10n = False

    python hide:
        def cuadro10n_overlay():
            if cuadro10n:
                ui.text("{size=-11}Tiempo promedio de un cliente en la cola (wq) = ?.{/size}",
                        xpos=1,
                        ypos=184,
                        xysize=(186, 71))
       
        config.overlay_functions.append(cuadro10n_overlay)
        
        
        
init:
    $ cuadro11 = False

    python hide:
        def cuadro11_overlay():
            if cuadro11:
                ui.text("{size=-11}Tiempo promedio de un cliente en el sistema (ws) = [k].{/size}",
                        xpos=198,
                        ypos=181,
                        xysize=(219, 75))

        config.overlay_functions.append(cuadro11_overlay)
        
        
init:
    $ cuadro11n = False

    python hide:
        def cuadro11n_overlay():
            if cuadro11n:
                ui.text("{size=-11}Tiempo promedio de un cliente en el sistema (ws) = ?.{/size}",
                        xpos=198,
                        ypos=181,
                        xysize=(219, 75))

        config.overlay_functions.append(cuadro11n_overlay)
        
        
init:
    $ cuadro12 = False

    python hide:
        def cuadro12_overlay():
            if cuadro12:
                ui.text("{size=-11}Numero promedio de clientes en la cola (lq) = [l].{/size}",
                        xpos=436,
                        ypos=183,
                        xysize=(176, 71))

        config.overlay_functions.append(cuadro12_overlay)
        
        
init:
    $ cuadro12n = False

    python hide:
        def cuadro12n_overlay():
            if cuadro12n:
                ui.text("{size=-11}Numero promedio de clientes en la cola (lq) = ?.{/size}",
                        xpos=436,
                        ypos=183,
                        xysize=(176, 71))

        config.overlay_functions.append(cuadro12n_overlay)
        
        
        
init:
    $ cuadro13 = False

    python hide:
        def cuadro13_overlay():
            if cuadro13:
                ui.text("{size=-11}Numero promedio de clientes en el sistema (ls) = [m].{/size}",
                        xpos=621,
                        ypos=182,
                        xysize=(178, 73))

        config.overlay_functions.append(cuadro13_overlay)
        
        
init:
    $ cuadro13n = False

    python hide:
        def cuadro13n_overlay():
            if cuadro13n:
                ui.text("{size=-11}Numero promedio de clientes en el sistema (ls) = ?.{/size}",
                        xpos=621,
                        ypos=182,
                        xysize=(178, 73))

        config.overlay_functions.append(cuadro13n_overlay)
        
        
        
init:
    $ cuadro14 = False

    python hide:
        def cuadro14_overlay():
            if cuadro14:
                ui.text("{size=-11}Probabilidad de que el sistema este vacio (po) = [n].{/size}",
                        xpos=1,
                        ypos=305,
                        xysize=(184, 74))

        config.overlay_functions.append(cuadro14_overlay)
        
        
init:
    $ cuadro14n = False

    python hide:
        def cuadro14n_overlay():
            if cuadro14n:
                ui.text("{size=-11}Probabilidad de que el sistema este vacio (po) = ?.{/size}",
                        xpos=1,
                        ypos=305,
                        xysize=(184, 74))

        config.overlay_functions.append(cuadro14n_overlay)
        
        
init:
    $ cuadro16 = False

    python hide:
        def cuadro16_overlay():
            if cuadro16:
                ui.text("{size=-11}Capacidad maxima del sistema (N) = [p].{/size}",
                        xpos=196,
                        ypos=305,
                        xysize=(221, 75))

        config.overlay_functions.append(cuadro16_overlay)
        
        
init:
    $ cuadro16n = False

    python hide:
        def cuadro16n_overlay():
            if cuadro16n:
                ui.text("{size=-11}Capacidad maxima del sistema (N) = ?.{/size}",
                        xpos=196,
                        ypos=305,
                        xysize=(221, 75))

        config.overlay_functions.append(cuadro16n_overlay)
        
        
init:
    $ cuadro17 = False

    python hide:
        def cuadro17_overlay():
            if cuadro17:
                ui.text("{size=-11}Numero de personas en el sistema (n) = [clientes].{/size}",
                        xpos=436,
                        ypos=307,
                        xysize=(179, 74))

        config.overlay_functions.append(cuadro17_overlay)
        
        
init:
    $ cuadro17n = False

    python hide:
        def cuadro17n_overlay():
            if cuadro17n:
                ui.text("{size=-11}Numero de personas en el sistema (n) = ?.{/size}",
                        xpos=196,
                        ypos=305,
                        xysize=(221, 75))

        config.overlay_functions.append(cuadro17n_overlay)   
        
        
init:
    $ cuadro18 = False

    python hide:
        def cuadro18_overlay():
            if cuadro18:
                ui.text("{size=-11}Numero de personas en el sistema (n) = [clientes].{/size}",
                        xpos=196,
                        ypos=305,
                        xysize=(221, 75))

        config.overlay_functions.append(cuadro18_overlay)
        
        
init:
    $ cuadro18n = False

    python hide:
        def cuadro18n_overlay():
            if cuadro18n:
                ui.text("{size=-11}Numero de personas en el sistema (n) = ?.{/size}",
                        xpos=196,
                        ypos=305,
                        xysize=(221, 75))

        config.overlay_functions.append(cuadro18n_overlay)  
        
        
        
# The game starts here.
# - El juego comienza aquí.
label start:
    
    scene fondo with dissolve
    
    "Bienvenido al programa que simula y le permite resolver un ejercicio de la teoria de colas. Presione en la pantalla o pulse \"enter\" para continuar."
        
    menu:
        "Si":
            
            show esquema1 at truecenter with dissolve
            
            "La teoría de colas no es más que el estudio matemático de las colas o líneas de espera dentro de un sistema. La teoría de colas es el estudio matemático del comportamiento de líneas de espera." 
            "Esta se presenta, cuando los \"clientes\" llegan a un \"lugar\" demandando un servicio a un \"servidor\", el cual tiene una cierta capacidad de atención." 
            
            show esquema2 at truecenter with dissolve
            hide esquema1 with dissolve
            
            "Si el servidor no está disponible inmediatamente y el cliente decide esperar, entonces se forma la línea de espera."
            
            show esquema3 at truecenter with dissolve
            hide esquema2 with dissolve
            
            "Mientras tanto, el modelo de colas general de Possion, asume que tanto las tasas de entrada como de salida dependen del estado."
            "Esto significa que dependen de la cantidad de clientes en la instalación de servicio."
            
            hide esquema3 with dissolve
            
            "Y esa fue una breve explicación, continuemos con el programa..."
        
        "No":
            "Entonces continuemos con el programa..."
            #relleno.
            
        "¿Desea leer de que trata la teoria de colas y el modelo de colas general de Poisson?"
    
    $ i = 0
    
    $ zawarudo = 0
    
    menu:
        

        "{size=-5}1 - Modelo Poisson, con un servidor, disciplina general, capacidad del sistema infinita y población infinita. {vspace=1}(M/M/1):(DG/∞/∞){/size}":
            
            $ zawarudo = 1
            jump contador_de_ejercicios
            
        "{size=-5}2 - Modelo Poisson, con un servidor, disciplina general, capacidad del sistema limitado y población infinita. {vspace=1}(M/M/1):(DG/N/∞){/size}":
            
            $ zawarudo = 2
            jump contador_de_ejercicios
            
        "{size=-5}3 - Modelo Poisson, con distintos servidores, disciplina general, capacidad del sistema infinita y población infinita. {vspace=1}(M/M/C):(DG/∞/∞){/size}":
            
            $ zawarudo = 3
            jump contador_de_ejercicios
            
        "{size=-5}4 - Modelo Poisson, con distintos servidores, disciplina general, capacidad del sistema limitado y población infinita. {vspace=1}(M/M/C):(DG/N/∞){/size}":
            
            $ zawarudo = 4
            jump contador_de_ejercicios
                    
        "¿Que tipo de ejercicio desea realizar?"
        
        
label contador_de_ejercicios:
    
    $ i += 1
                
    "Ejercicio [i]"
    
    jump lambda_y_niu
    
label lambda_y_niu:
    
    #tasa promedio de elementos en el sistema (λ)
    $ scruffy = renpy.input("Introduzca el valor para la tasa promedio de elementos en el sistema (λ), introduzcalo en minutos.", allow="0123456789-.")
    while scruffy == "" or scruffy == "." or scruffy == "-":
        $ scruffy = renpy.input("No se admiten espacios en blanco, introduzca el valor la tasa promedio de elementos en el sistema (λ)", allow="0123456789-.")
    $ a = float(scruffy)
    while a < 0.01:
        $ scruffy = renpy.input("No puede ser menor de cero o negativo, introduzca el valor para la tasa promedio de elementos en el sistema (λ)", allow="0123456789-.")
        while scruffy == "" or scruffy == "." or scruffy == "-":
            $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el valor la tasa promedio de elementos en el sistema (λ)", allow="0123456789-.")
        $ a = float(scruffy)
    $ a = float(scruffy)

    #tiempo de λ
    $ q = "minutos"
    


    #tasa promedio de servicios (μ)
    $ scruffy = renpy.input("Introduzca el valor para la tasa promedio de servicios (μ)", allow="0123456789-.")
    while scruffy == "" or scruffy == "." or scruffy == "-":
        $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el valor para la tasa promedio de servicios (μ), introduzcalo en minutos.", allow="0123456789-.")
    $ b = float(scruffy)
    while b < 0.01:
        $ scruffy = renpy.input("No puede ser menor de cero o negativo, introduzca el valor para la tasa promedio de servicios (μ)", allow="0123456789-.")
        while scruffy == "" or scruffy == "." or scruffy == "-":
            $ scruffy = renpy.input("No se puede dejar el valor en blanco, el valor para la tasa promedio de servicios (μ)", allow="0123456789-.")
        $ b = float(scruffy)
    $ b = float(scruffy)
                    
    #tiempo de μ
    $ r = "minutos"

                    
    
    #numero de servidores (s)
    if zawarudo <= 2:
        $ c = 1    
    else:        
        $ scruffy = renpy.input("Introduzca el numero de servidores.", allow="0123456789-.")
        while scruffy == "" or scruffy == "." or scruffy == "-":
            $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el numero de servidores.", allow="0123456789-.")
        $ c = float(scruffy)
        while c <= 1:
            $ scruffy = renpy.input("No puede ser menor o igual a uno, o negativo. Introduzca el numero de servidores.", allow="0123456789-.")
            while scruffy == "" or scruffy == "." or scruffy == "-":
                $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el numero de servidores.", allow="0123456789-.")
            $ c = float(scruffy)
        $ c = float(scruffy)
        
        
    jump conteo
    
    
label conteo:

                
    # N
    if (zawarudo == 2) or (zawarudo == 4):
        $ scruffy = renpy.input("Introduzca la capacidad maxima del sistema (N).", allow="0123456789-.")
        while scruffy == "" or scruffy == "." or scruffy == "-":
            $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca la capacidad maxima del sistema (N).", allow="0123456789-.")
        $ p = float(scruffy)
        while p <= 0:
            $ scruffy = renpy.input("No puede ser cero o negativo.", allow="0123456789-.")
            while scruffy == "" or scruffy == "." or scruffy == "-":
                $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca la capacidad maxima del sistema (N)", allow="0123456789-.")
            $ p = float(scruffy)
        $ p = float(scruffy)
    
    
    
    
    
    # n
    if (zawarudo == 3) or (zawarudo == 4):
        $ scruffy = renpy.input("Introduzca el numero de personas en el sistema (n).", allow="0123456789-.")
        while scruffy == "" or scruffy == "." or scruffy == "-":
            $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el numero de personas en el sistema (n).", allow="0123456789-.")
        $ clientes = float(scruffy)
        while clientes <= 0:
            $ scruffy = renpy.input("No puede ser cero o negativo.", allow="0123456789-.")
            while scruffy == "" or scruffy == "." or scruffy == "-":
                $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el numero de personas en el sistema (n)", allow="0123456789-.")
            $ clientes = float(scruffy)
        $ clientes = float(scruffy)
        
        
    if zawarudo == 4:
        while clientes > p:
            $ scruffy = renpy.input("El numero de personas en el sistema (n) no puede ser mayor que el numero maximo de clientes (N)", allow="0123456789-.")
            while scruffy == "" or scruffy == "." or scruffy == "-":
                $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el numero de personas en el sistema (n).", allow="0123456789-.")
            $ clientes = float(scruffy)
            while clientes <= 0:
                $ scruffy = renpy.input("No puede ser cero o negativo.", allow="0123456789-.")
                while scruffy == "" or scruffy == "." or scruffy == "-":
                    $ scruffy = renpy.input("No se puede dejar el valor en blanco, introduzca el numero de personas en el sistema (n)", allow="0123456789-.")
                $ clientes = float(scruffy)
            $ clientes = float(scruffy)
            
            
            
    #P
    $ scruffy = a/b  
    $ e = float(scruffy)
    if (zawarudo == 1):
        if e >= 1:
            "ρ da un numero mayor o igual a uno, por favor introduzca otros valores para λ y μ."
            jump lambda_y_niu
    elif (zawarudo == 3):
        if e/c >= 1:
            "ρ/c da un numero mayor o igual a uno, por favor introduzca otros valores para λ y μ."
            jump lambda_y_niu

    
    
    $ m = 0
    $ n = 0
    $ k = 0
    $ jx = 0
    $ l = 0
        
        
    
    if zawarudo == 1:
        jump ejercicio_poisson
        
    elif zawarudo == 2:
        jump ejercicio_poisson2
        
    elif zawarudo == 3:
        jump ejercicio_paralelo
        
    elif zawarudo == 4:
        jump ejercicio_paralelo2


    return 
    