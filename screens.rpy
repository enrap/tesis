# Este archivo se encuentra en el dominio público. Puede ser modificado
# libremente como base para tus propias pantallas.

# Muchas de estas pantallas pueden recibir argumentos adicionales en el
# futuro. El uso de **kwargs el la lista de parámetros asegura que tu código
# funcionará en el futuro.

##############################################################################
# Diálogo
#
# Pantalla utilizada para presentar el diálogo en modo adv.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Opta entre las variantes de una o dos ventanas.
    if not two_window:

        # Una ventana.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Dos ventanas.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Si hay una imagen lateral, la presenta sobre el texto.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Usa el menú de acceso rápido.
    use quick_menu


##############################################################################
# Elecciones
#
# Pantalla utilizada para presentar los menus dentro del juego.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 8

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Entrada
#
# Pantalla utilizada para presentar renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Pantalla utilizada para el diálogo y los menús en modo nvl.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Presenta el diálogo.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Presenta un menú, si lo hay.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Menú principal
#
# Pantalla utilizada para presentar el menú principal, cuando Ren'Py arranca
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu
    
    # Fondo del menú principal.
    imagemap:

        ground "screenshot0009.jpg"

        hover "screenshot00092.png"

    # Botones del menú principal.
        hotspot (300, 379, 224, 81) action Start()
        hotspot (302, 468, 223, 87) action Quit()
        

init -2:

    # Ajusta todos los botones del menú principal al mismo tamaño.
    style mm_button:
        size_group "mm"



##############################################################################
# Navegación
#
# Pantalla incluida en otras pantallas para presentar las opciones de
# navegación y el fondo en los menús del juego.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    ## The various buttons.
    imagemap:
        ground "jotarokujo.jpg"
        
        hover "jotarokujo_hover.png"
       
        hotspot (266, 235, 275, 102) action MainMenu()
        hotspot (272, 468, 265, 93) action Return()
    

##############################################################################
# Guardar, Cargar
#
# Pantallas que permiten al usuario guardar y cargar las partidas.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ya que guardar y cargar son muy similares, se combinan en una sola
# pantalla, selector de archivo ('file_picker'). Esa se usa desde
# simples pantallas de guardado y carga.

screen file_picker():

    frame:
        style "file_picker_frame"

        label "Creado por Enrique Acosta"


screen save():

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    use navigation
    use file_picker

screen load():

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Opciones
#
# Pantalla que permite al usuario cambiar las opciones.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Incluye la navegación.
    use navigation

    # Coloca las columnas de navegación en una cuadrícula de tres columnas.
    grid 3 1:
        style_group "prefs"
        xfill True

        # Columna izquierda.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"
            frame:
                style_group "pref"
                has vbox

                label _("Lenguaje")
                textbutton "Español" action Language(None)
                textbutton "English" action Language("english")

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Pregunta Sí/No
#
# Pantalla que pregunta al usuario una pregunta Sí/No.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    if message == layout.ARE_YOU_SURE:
        window:
            style "gm_root"

        frame:
            style_group "yesno"

            xfill True
            xmargin .05
            ypos .1
            yanchor 0
            ypadding .05

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            label _("¿Seguro que quieres hacer eso?"):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
        
    elif message == layout.DELETE_SAVE:
        window:
            style "gm_root"

        frame:
            style_group "yesno"

            xfill True
            xmargin .05
            ypos .1
            yanchor 0
            ypadding .05

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            label _("Do you really wanna Delete this Save?"):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
        
        
    elif message == layout.OVERWRITE_SAVE:
        window:
            style "gm_root"

        frame:
            style_group "yesno"

            xfill True
            xmargin .05
            ypos .1
            yanchor 0
            ypadding .05

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            label _("Are you absolutely sure you wanna Overwrite this Save?"):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
        
        
    elif message == layout.LOADING:
        window:
            style "gm_root"

        frame:
            style_group "yesno"

            xfill True
            xmargin .05
            ypos .1
            yanchor 0
            ypadding .05

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            label _("¿Seguro que quieres continuar (¿y como encontraste esta pantalla?)?"):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
        
        
    elif message == layout.QUIT:
        window:
            style "gm_root"

        frame:
            style_group "yesno"

            xfill True
            xmargin .05
            ypos .1
            yanchor 0
            ypadding .05

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            label _("¿Seguro que desea salir?"):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
        
        
    elif message == layout.MAIN_MENU:
        window:
            style "gm_root"

        frame:
            style_group "yesno"

            xfill True
            xmargin .05
            ypos .1
            yanchor 0
            ypadding .05

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            label _("¿Seguro que desea volver al principio?"):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
        


##############################################################################
# Menú de acceso rápido
#
# Pantalla incluida por defecto en la pantalla de diálogo, que añade acceso
# rápido a una serie de funciones útiles.
screen quick_menu():

    # Añade un menú de acceso rápido interno al juego.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Volver al princípio") action MainMenu()
        textbutton _("Salír") action Quit()
        textbutton _("REGRESAR") action Rollback()

init -2:
    style quick_button:
        is default
        background None
        xpadding 10

    style quick_button_text:
        is default
        size 17
        idle_color "#000000"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
                          
return
                                    