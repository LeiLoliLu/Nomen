mirar=["mirar","ver","observar","examinar"]
usar=["usar","utilizar"]
guardar=["guardar","coger","tomar"]
ir=["ir","salir","irse","volver","entrar"]
abrir=["abrir"]
dejar=["dejar", "tirar","soltar"]
accion=[]
inv=["Tarro"]
door="closed"
araña="si"
boton="no"

def Separar(cadena):
    global accion
    accion=cadena.split(" ",3)

def tirar(objeto):
    if objeto in inv:
        inv.remove(objeto)

def Start(): ##DormitorioAzul
    print("Has despertado en un cuarto. Las paredes son blancas, y los muebles están formados por una madera azulada.")
    print("Una cama, un armario, una cómoda y un escritorio se encuentran en esta habitación.")
    print("Puedes identificar un espejo colgado de una de las paredes. También hay una alfombra.")
    print("Por otra parte, la ventana frente al escritorio y la puerta en el lado contrario de la cama son de una madera azul más oscura.")
    DormiAzulAct()

def DormiAzulAct():
    global door
    global araña
    global boton
    Separar(input(">").lower())
    if accion[0]=="ayuda" or accion==[0]=="help":
        print("Mirar [objeto]: Mira alguna cosa.")
        print("Coger [objeto]: Añades un objeto a tu inventario.")
        print("Tirar [objeto]: Tiras un objeto de tu inventario.")
        print("Usar [objeto]: Usar un objeto de tu inventario. (o fuera de tu inventario, pero en la gran mayoria tienes que tenerlo)")
        print("Salir/Entrar : Sal del cuarto en el que estás, o entra a uno nuevo.")
        print("En vez de 'mirar' puedes escribir 'ver' o 'examinar'. Es decir, diferentes comandos también pueden utilizarse")
        print("Tambien puedes realizar diferentes acciones de varias formas, por ejemplo, quizas puedes mirar debajo de una alfombra.")
    ## mirar cosas
    if accion[0] in mirar:
        if accion[1]=="muebles" or accion[1]=="mueble":
            print("Hay una cama, un armario, una cómoda, y un escritorio en esta habitación. La madera es azul palida.")
            print("A pesar de no ser un mueble, hay una alfombra en el suelo.")
            DormiAzulAct()
        elif accion[1]=="tarro":
            print("¿De dónde has sacado ese tarro?") ##solo de betatester
        elif accion[1]=="inventario" or accion[1]=="inv":
            print("Este es tu inventario:")
            for x in inv:
                print(x)
            DormiAzulAct()
        elif accion[1]=="techo":
            print("Miras el techo. Es blanco. No hay lámpara.")
            DormiAzulAct()
        elif accion[1]=="suelo":
            print("Miras el suelo. Es de madera. Chirria un poco al caminar por él.")
            DormiAzulAct()
        elif accion[1]=="hora" or accion[1]=="reloj":
            print("Buscas tu reloj para mirar la hora. No lo tienes puesto.")
            print("No hay relojes en el cuarto.")
            print("No sabes qué hora es.")
            DormiAzulAct()
        elif accion[1]=="cuarto" or accion[1]=="habitación":
            print("Las paredes son blancas, y los muebles están formados por una madera azulada.")
            print("Una cama, un armario, una cómoda y un escritorio se encuentran en esta habitación.")
            print("Puedes identificar un espejo colgado de una de las paredes. También hay una alfombra.")
            print("Por otra parte, la ventana frente al escritorio y la puerta en el lado contrario de la cama son de una madera azul más oscura.")
            DormiAzulAct()
        elif accion[1]=="paredes" or accion[1]=="pared":
            print("Las paredes son blancas. Hay un espejo, una ventana y una puerta.")
            DormiAzulAct()
        elif accion[1]=="cama": 
            print("Miras la cama. Está algo desecha de haber dormido en ella. Las sábanas son azules, a juego con la madera más oscura de la habitación.")
            print("Parece que has dormido sobre las sábanas.")
            print("No recuerdas haberte acostado aquí.")
            DormiAzulAct()
        elif accion[1]=="sábanas":
            print("Miras por las sábanas. No hay nada.")
            DormiAzulAct()
        elif accion[1]=="debajo" and accion[2]=="cama": 
            print("Miras debajo de la cama. Hay una muñeca. Su pelo es azul y le falta un ojo botón. Es bastante antigua.")   
            print("Su vestido es del mismo color que la madera de la cama, y su unico botón es un turquesa intenso.")
            print("La dejas ahí.")
            DormiAzulAct()
        elif accion[1]=="muñeca":
            if boton=="no":
                print("Miras la muñeca. Su pelo es azul y le falta un ojo botón. Es bastante antigua.")   
                print("Su vestido es del mismo color que la madera de la cama, y su unico botón es un turquesa intenso.")
            else:
                print("Miras la muñeca. Su pelo es azul y tiene ojos botón turquesas. Es bastante antigua.")
                print("Te mira feliz. Parece que tiene ganas de jugar.")  
            DormiAzulAct()
        elif accion[1]=="armario": 
            print("Miras el armario. Su madera está algo deformada por los pomos. Abres una puerta.")
            print("Dentro no hay mucho, solo una bola de polvo y un libro de tapa azul.")
            print("Que armario tan aburrido.")
            DormiAzulAct()
        elif accion[1]=="polvo": 
            print("Miras al polvo. Hay bastante cantidad. Lo tocas, y un buen trozo se queda en tu dedo.")
            print("Lo sacudes.")
            print("Estornudas.")
            DormiAzulAct()
        elif accion[1]=="libro": 
            print("Miras el libro. Tu mano deja una huella limpiando el polvo cuando lo coges.")
            print("Las páginas están en blanco.")
            print("Vuelves a dejar el libro.")
            DormiAzulAct()
        elif accion[1]=="cómoda": 
            print("Miras la cómoda. Tiene varios cajones, y los abres. Una araña se ha adueñado de el primer cajón. Lo cierras enseguida.")
            print("En el segundo cajón solo hay polvo, y en el tercero hay un papel.")
            print("Curioso.")
            DormiAzulAct()
        elif accion[1]=="araña":
            print("Abres el primer cajón y miras a la araña.")
            print("Cierras el cajón.")
            print("No quieres mirar.")
            DormiAzulAct()
        elif accion[1]=="papel":
            print("Es una hoja de papel. Tiene dibujada una flor azul.")
            print("La flor está triste.")
            print("Dejas el papel.")
            DormiAzulAct()
        elif accion[1]=="escritorio": 
            print("Miras el escritorio. Hay cuatro agujeros frente a él. Abres sus cajones.")
            print("Encuentras un lapicero amarillo.")
            print("Tienes la sensación de que este no es su lugar.")
            DormiAzulAct()
        elif accion[1]=="agujeros":
            print("Son 4 agujeros puestos a la misma distancia cada uno, formando un cuadrado, como si los huecos fueran los vértices del mismo.")
            print("Te entran 3 dedos en cada uno.")
            DormiAzulAct()
        elif accion[1]=="lapicero": 
            print("El lapicero amarillo no tiene punta y esta mordido por la parte de atrás.")
            print("Te da un sentimiento de angustia.")
            DormiAzulAct()
        elif accion[1]=="espejo": 
            print("Miras el espejo. Te ves.")
            print("Tienes el pelo revuelto.")
            print("No llevas tu ropa.")
            DormiAzulAct()
        elif accion[1]=="detrás" and accion[2]=="espejo": 
            print("Miras detrás del espejo. No hay nada.")
            print("Que triste.")
            DormiAzulAct()
        elif accion[1]=="ropa": 
            print("Sin duda, esta ropa no es tuya. Te queda muy grande.")
            print("Esta camisa azul te queda demasiado grande, y los pantalones vaqueros se te caen.")
            print("Aprietas el cinturón a tu medida.")
            DormiAzulAct()
        elif accion[1]=="camisa":
            print("La camisa es azul, y te queda bastante grande.")
            print("Los botones de la camisa son turquesas.")
            print("Tienes uno algo suelto.")
            DormiAzulAct()
        elif accion[1]=="vaqueros" or accion[1]=="pantalones" or accion[1]=="pantalón":
            print("Los vaqueros te quedan grandes. Estan algo gastados.")
            print("No hay nada en los bolsillos.")
            DormiAzulAct()
        elif accion[1]=="botón":
            print("Un botón de tu camisa está apunto de descoserse.")
            DormiAzulAct()
        elif accion[1]=="alfombra": 
            print("Miras la alfombra. Hecha con tela azul, dibuja diversos patrones.")
            print("Hay un bulto debajo.")
            DormiAzulAct()
        elif accion[1]=="debajo" and accion[2]=="alfombra" or accion[0] in mirar and accion[1]=="bulto": 
            print("Apartas la alfombra. Encuentas una pelota.")
            DormiAzulAct()
        elif accion[1]=="pelota": 
            print("Miras la pelota. Es una pelota de goma verde.")
            print("Esto no deberia de estar aquí.")
            DormiAzulAct()
        elif accion[1]=="ventana" or accion[1]=="fuera": 
            print("Miras por la ventana. Está lloviendo fuera. Puedes distinguir un jardín.")
            print("No puedes abrir la ventana.")
            print("Si sales será mejor que encuentres un paraguas.")
            DormiAzulAct()
        elif accion[1]=="puerta": 
            print("Miras la puerta.")
            print("Es una buena puerta.")
            DormiAzulAct()
        elif accion[1]=="pomo" or accion[1]=="pomos":
            print("Los pomos del armario son de un metal azulado algo oxidado.")
            print("El pomo de la puerta es del mismo material.")
            DormiAzulAct()
        elif accion[1]=="aguja" or accion[1]=="hilo":
            print("Aguja e hilo, utilizados usualmente para coser.")
            print("Seguro que le encuentras un uso.")
        else:
            print("Estas intentando mirar a algo. Para mirar, escribe (¡Cuidado con los acentos!):")
            print("'Mirar alfombra'.")
            print("'Mirar detrás cuadro'.")
            print("Si aun así no puedes mirar a esa cosa, será que no es importante, o que no se encuentra en esta localización.")
            DormiAzulAct()
    ## guardar objetos
    if accion[0] in guardar:
        if accion[1]=="muñeca":
            if "Muñeca" not in inv:
                print("Guardas la muñeca en tu inventario.")
                inv.append("Muñeca")
                DormiAzulAct()
            else:
                print("Ya tienes la muñeca en tu inventario.")
                DormiAzulAct()
        elif accion[1]=="libro":
            if "Libro" not in inv:
                print("Guardas el libro en tu inventario.")
                inv.append("Libro")
                DormiAzulAct()
            else:
                print("Ya tienes el libro en tu inventario.")
                DormiAzulAct()
        elif accion[1]=="papel":
            if "Papel" not in inv:
                print("Guardas el papel en tu inventario.")
                inv.append("Papel")
                DormiAzulAct()
            else:
                print("Ya tienes el papel en tu inventario.")
                DormiAzulAct()
        elif accion[1]=="lapicero":
            if "Lapicero" not in inv:
                print("Guardas el lapicero en tu inventario.")
                inv.append("Lapicero")
                DormiAzulAct()
            else:
                print("Ya tienes el lapicero en tu inventario.")
                DormiAzulAct()
        elif accion[1]=="pelota":
            if "Pelota" not in inv:
                print("Guardas la pelota en tu inventario.")
                inv.append("Pelota")
                DormiAzulAct()
            else:
                print("Ya tienes la pelota en tu inventario.")
                DormiAzulAct()
        elif accion[1]=="botón":
            print("Arrancas el botón de tu camisa.")
            inv.append("Botón")
            DormiAzulAct()
        elif accion[1]=="aguja" or accion[1]=="hilo":
            if araña=="si":
                print("Estas intentando coger algo. Para coger, escribe (¡Cuidado con los acentos!):")
                print("'Coger piedra'.")
                print("Si aun así no puedes coger esa cosa, será que no es importante, no es posible guardarla en tu inventario, o que no se encuentra en esta localización.")
                DormiAzulAct()
            else:
                objeto=accion[1].capitalize()
                if objeto not in inv:
                    print("Guardas la aguja y el hijo en tu inventario.")
                    inv.append("Aguja")
                    inv.append("Hilo")
                    DormiAzulAct()
                else:
                    print("Ya tienes la aguja y el hilo en tu inventario.")
                    DormiAzulAct()
        else:
            print("Estas intentando coger algo. Para coger, escribe (¡Cuidado con los acentos!):")
            print("'Coger piedra'.")
            print("Si aun así no puedes coger esa cosa, será que no es importante, no es posible guardarla en tu inventario, o que no se encuentra en esta localización.")
            DormiAzulAct()
    ## tirar objetos
    if accion[0] in dejar:
        objeto=accion[1].capitalize()
        print(f"¿Seguro que quieres tirar '{objeto}'? (Y/N)")
        opt=input(">").upper()
        if opt=="Y":
            print(f"Has tirado tu {objeto}.")
            tirar(objeto)
            DormiAzulAct()
        else:
            DormiAzulAct()
    ##usar objetos
    if accion[0] in usar:
        if accion[1].capitalize() in inv:
            if accion[1]=="tarro": 
                print("Te acercas con el tarro al cajón de la cómoda y capturas la araña.")
                print("Hay algo entre las telas de la araña.")
                print("Aguja e Hilo.")
                inv.remove("Tarro")
                inv.append("Araña en tarro")
                araña="No"
                DormiAzulAct()
            elif accion[1]=="silla":
                inv.remove("Silla")
                print("Colocas la silla en los agujeros que están frente al escritorio. Encaja.")
                print("Escuchas un click.")
                print("La silla no sale de los agujeros.")
                door="open"
                DormiAzulAct()
            elif accion[1]=="aguja" and accion[1]=="hilo" and accion[1]=="botón":
                print("Coses el botón de tu camisa a la muñeca. Ahora la muñeca tiene ambos ojos.")
                print("Está contenta. Seguro que le gustaría salir a jugar al jardín.")
                boton="si"
                inv.remove("Aguja")
                inv.remove("Hilo")
                inv.remove("Botón")
                DormiAzulAct()
            else:
                objeto=accion[1]
                print(f"Miras tu {objeto}, y te das cuenta de que en realidad no tiene ningún uso actualmente.")
                DormiAzulAct()
        elif accion[1]=="puerta" or accion[1]=="salida":
            print("Sales del dormitorio azul.")
            Pasillo()
        elif accion[1]=="ventana":
            print("La ventana no se abre.")
            DormiAzulAct()
        else:
            print("Estas intentando usar algo. Para usar, escribe (¡Cuidado con los acentos!):")
            print("'Usar tijera'.")
            print("Si aun así no puedes usar esa cosa, comprueba que la tienes en el inventario, o puede que no tengas que utilizar eso.")
            DormiAzulAct()
    ##salir 
    if accion[0] in ir:
        print("Sales del dormitorio azul.")
        Pasillo()

def Pasillo():
    print("¡Pasillo! No hay nada más por aquí, asique voy a volver a meterte al dormitorio azul. Si ya has visto todo ahí dentro, te has ganado una magdalena.")
    DormiAzulAct()



Start()