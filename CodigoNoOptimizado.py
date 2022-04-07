import time
import random
nomen="Nomen"
usern="Usuario"
cambianombre=0
cambionombre=0
victoriasRPS=0
derrotasRPS=0
empatesRPS=0
victoriasPPTLS=0
derrotasPPTLS=0
empatesPPTLS=0
victoriasPrNn=0
derrotasPrNn=0

#Presentación, User selecciona nombre
def presentacion():
    time.sleep(1)
    print(f"¡Hola! Soy {nomen}. ¿Como te llamas?")
    usernombre()
def usernombre():
    global cambianombre
    global usern
    global victoriasRPS
    usern = input()
    if usern=="Skip":
        victoriasRPS=10
        menu()
    else:
        time.sleep(1.2)
        print(f"¿Quieres que me refiera a ti como {usern}? (Y/N)")
        ans = input()
        time.sleep(1.2)
        if ans=="Y" and cambianombre>0 or ans=="y" and cambianombre>0:
            print(f"Vale, ahora te llamaré {usern}")
        elif ans=="Y" and cambianombre==0 or ans=="y" and cambianombre==0:
            print(f"Encantado de conocerte, {usern}")
            cambianombre=cambianombre+1
            menu()
        else:
            print("Entonces, ¿cómo quieres que te llame?")
            usernombre()

#stats
def stats():
    global usern
    global cambionombre
    global victoriasRPS
    global empatesRPS
    global derrotasRPS
    global victoriasPPTLS
    global empatesPPTLS
    global derrotasPPTLS
    global victoriasPrNn
    global derrotasPrNn
    
    time.sleep(1)
    print("Estos son tus stats:")
    time.sleep(1)  
    print(usern)
    time.sleep(0.5)  
    print(f"Veces cambiadas de nombre: {cambionombre}")
    time.sleep(0.5)
    print("Piedra, Papel, Tijera:")
    time.sleep(0.5)
    print(f"Veces ganadas: {victoriasRPS}")
    time.sleep(0.5)
    print(f"Veces empatadas: {empatesRPS}")
    time.sleep(0.5)
    print(f"Veces perdidas: {derrotasRPS}")
    time.sleep(0.5)
    print("Piedra, Papel, Tijera, Lagarto, Spock:")
    time.sleep(0.5)
    print(f"Veces ganadas: {victoriasPPTLS}")
    time.sleep(0.5)
    print(f"Veces empatadas: {empatesPPTLS}")
    time.sleep(0.5)
    print(f"Veces perdidas: {derrotasPPTLS}")
    time.sleep(0.5)
    print("Pares o Nones:")
    time.sleep(0.5)
    print(f"Veces empatadas: {victoriasPrNn}")
    time.sleep(0.5)
    print(f"Veces perdidas: {derrotasPrNn}")
    menu()

#Menú principal
def menu():
    global victoriasRPS
    global cambionombre
    time.sleep(1.2)
    print(f"Vale, {usern}, ¿Qué hacemos ahora?")
    time.sleep(0.5)
    print("1. Jugar a algo")
    time.sleep(0.5)
    print("2. Ver mis Stats")
    time.sleep(0.5)
    print("3. Quiero cambiar mi nombre")
    opcion=input()
    if opcion=="1":
        if victoriasRPS>9:
            pptls="2. Piedra, Papel, Tijera, Lagarto, Spock"
        else:
            pptls="2. Bloqueado"
        time.sleep(1.2)
        print("¡Juegos! Me encantan. ¿A que jugamos?")
        time.sleep(0.5)
        print("1. Piedra, Papel, Tijera")
        time.sleep(0.5)
        print(pptls)
        time.sleep(0.5)
        print("3. Pares y Nones")
        juego=input()
        if juego=="1":
            RoPaSc()
        elif juego=="2":
            if pptls=="2. Bloqueado":
                print("¡Tienes que ganarme a piedra, papel tijera 10 veces antes de jugar a esto!")
                time.sleep(0.5)
                print(f"Por ahora me has ganado estas veces: {victoriasRPS}")
                menu()
            elif pptls=="2. Piedra, Papel, Tijera, Lagarto, Spock":
                RoPaScLiSp()
        elif juego=="3":
            ParesNones()
    elif opcion=="2":
        stats()
    elif opcion=="3":
        cambionombre=cambionombre+1
        time.sleep(1.2)
        print("¿Quieres cambiarte el nombre? ¿A cual?")
        usernombre()
        menu()

#Piedra, Papel, Tijera
def RoPaSc():
    time.sleep(1)
    print("Piedra, papel o tijera. ¿Sabes Jugar? (Y/N)")
    answ=input()
    if answ=="Y" or answ=="y":
        time.sleep(1)
        print("¡Bien, pues empecemos!")
        time.sleep(0.5)
        print("¿Piedra, papel o tijera?")
        opcionRPS()
    elif answ=="N" or answ=="n":
        time.sleep(1)
        print("Es muy sencillo. Ambos elegimos piedra, papel o tijera a la vez")
        time.sleep(0.5)
        print("Y luego, funciona por las siguientes reglas:")
        time.sleep(0.5)
        print("Piedra aplasta a Tijera")
        time.sleep(0.5)
        print("Tijera corta a Papel")
        time.sleep(0.5)
        print("Papel tapa a Piedra")
        time.sleep(0.5) 
        print("¿Quieres jugar? (Y/N)")
        answe = input()
        if answe=="Y" or answe=="y":
            time.sleep(1)
            print("¡Bien, pues empecemos!")
            time.sleep(0.5)
            print("¿Piedra, papel o tijera?")
            opcionRPS()
        elif answe=="N" or answe=="n":
            menu()
def opcionRPS():
    inputRPS = input()
    choiceNomen=random.randint(0,2)
    if inputRPS=="Piedra" or inputRPS=="piedra":
        choiceUser="Piedra"
    elif inputRPS=="Papel" or inputRPS=="papel":
        choiceUser="Papel"
    elif inputRPS=="Tijera" or inputRPS=="tijera":
        choiceUser="Tijera"
    else:
        print("¡Esa no es una opción valida!")
        opcionRPS()
    #Empate Piedra
    global victoriasRPS
    global empatesRPS
    global derrotasRPS

    if choiceNomen==0 and choiceUser=="Piedra":
        empatesRPS=empatesRPS+1
        time.sleep(1)
        print("Has elegido piedra, y yo también. ¡Empate!")
        time.sleep(0.5)
        print("¿Quieres jugar otra vez? (Y/N)")
        restartgame1()
    #Piedra-Papel, gana user
    elif choiceNomen==0 and choiceUser=="Papel":
            victoriasRPS=victoriasRPS+1
            time.sleep(1)
            print("Has elegido papel, y yo piedra.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Piedra-Tijera, gana nomen
    elif choiceNomen==0 and choiceUser=="Tijera":
            derrotasRPS=derrotasRPS+1
            time.sleep(1)
            print("Has elegido tijera, y yo piedra.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Empate papel
    elif choiceNomen==1 and choiceUser=="Papel":
            empatesRPS=empatesRPS+1
            time.sleep(1)
            print("Has elegido papel, y yo también. ¡Empate!")
            time.sleep(0.5)
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Papel Tijera, gana user
    elif choiceNomen==1 and choiceUser=="Tijera":
            victoriasRPS=victoriasRPS+1
            time.sleep(1)
            print("Has elegido tijera, y yo papel.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Papel Piedra, gana nomen
    elif choiceNomen==1 and choiceUser=="Piedra":
            derrotasRPS=derrotasRPS+1
            time.sleep(1)
            print("Has elegido piedra, y yo papel.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Empate tijera
    elif choiceNomen==2 and choiceUser=="Tijera":
            empatesRPS=empatesRPS+1
            time.sleep(1)
            print("Has elegido tijera, y yo también. ¡Empate!")
            time.sleep(0.5)
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Tijera Piedra gana user
    elif choiceNomen==2 and choiceUser=="Piedra":
            victoriasRPS=victoriasRPS+1
            time.sleep(1)
            print("Has elegido piedra, y yo tijera.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Tijera Papel gana Nomen
    elif choiceNomen==2 and choiceUser=="Papel":
            derrotasRPS=derrotasRPS+1
            time.sleep(1)
            print("Has elegido papel, y yo tijera.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
def restartgame1():
    anss=input()
    if anss=="Y" or anss=="y":
        time.sleep(1)
        print("¡Bien! Vamos allá.")
        time.sleep(0.5)
        print("¿Piedra, papel o tijera?")
        opcionRPS()
    else:
        menu()
    
#Piedra, Papel, Tijera, Lagarto, Spock    
def RoPaScLiSp():
    time.sleep(1)
    print("Piedra, papel, tijera, lagarto, spock. ¿Sabes Jugar? (Y/N)")
    answ=input()
    if answ=="Y" or answ=="y":
        time.sleep(1)
        print("¡Bien, pues empecemos!")
        time.sleep(0.5)
        print("¿Piedra, papel, tijera, lagarto o spock?")
        opcionPPTLS()
    elif answ=="N" or answ=="n":
        time.sleep(1)
        print("Es muy sencillo. Ambos elegimos piedra, papel, tijera, lagarto o spock a la vez")
        time.sleep(0.5)
        print("Y luego, funciona por las siguientes reglas:")
        time.sleep(0.5)
        print("Tijera corta a Papel")
        time.sleep(0.5)
        print("Papel tapa a Piedra")
        time.sleep(0.5)
        print("Piedra aplasta a Lagarto")
        time.sleep(0.5)
        print("Lagarto envenena a Spock")
        time.sleep(0.5)
        print("Spock rompe a Tijera")
        time.sleep(0.5)
        print("Tijera decapita a Lagarto") 
        time.sleep(0.5)
        print("Lagarto devora a Papel")
        time.sleep(0.5)
        print("Papel desautoriza a Spock")
        time.sleep(0.5)
        print("Spock vaporiza a Piedra")
        time.sleep(0.5)
        print("Y como siempre, Piedra aplasta a Tijera")  
        time.sleep(0.5)  
        print("¿Quieres jugar?")
        answe = input()
        if answe=="Y" or answe=="y":
            time.sleep(1)
            print("¡Bien, pues empecemos!")
            time.sleep(0.5)
            print("¿Piedra, papel, tijera, lagarto o spock?")
            opcionPPTLS()
        elif answe=="N" or answe=="n":
            menu()
def opcionPPTLS():
    inputPPTLS = input()
    choiceNomen=random.randint(0,4)
    if inputPPTLS=="Piedra" or inputPPTLS=="piedra":
        choiceUser="Piedra"
    elif inputPPTLS=="Papel" or inputPPTLS=="papel":
        choiceUser="Papel"
    elif inputPPTLS=="Tijera" or inputPPTLS=="tijera":
        choiceUser="Tijera"
    elif inputPPTLS=="Lagarto" or inputPPTLS=="lagarto":
        choiceUser="Lagarto"
    elif inputPPTLS=="Spock" or inputPPTLS=="spock":
        choiceUser="Spock"
    else:
        print("¡Esa no es una opción valida!")
        opcionPPTLS()
    
    global victoriasPPTLS
    global empatesPPTLS
    global derrotasPPTLS
    
        #Empate Piedra
    if choiceNomen==0 and choiceUser=="Piedra":
        empatesPPTLS=empatesPPTLS+1
        time.sleep(1)
        print("Has elegido piedra, y yo también. ¡Empate!")
        time.sleep(0.5)
        print("¿Quieres jugar otra vez? (Y/N)")
        restartgame2()
        #Piedra-Papel, gana user
    elif choiceNomen==0 and choiceUser=="Papel":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido papel, y yo piedra.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
        #Piedra-Tijera, gana nomen
    elif choiceNomen==0 and choiceUser=="Tijera":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido tijera, y yo piedra.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
        #Piedra-Lagarto, gana Nomen
    elif choiceNomen==0 and choiceUser=="Lagarto":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido lagarto, y yo piedra.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
        #Piedra-Spock, gana User
    elif choiceNomen==0 and choiceUser=="Spock":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido spock, y yo piedra.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    
    #Empate papel
    elif choiceNomen==1 and choiceUser=="Papel":
            empatesPPTLS=empatesPPTLS+1
            time.sleep(1)
            print("Has elegido papel, y yo también. ¡Empate!")
            time.sleep(0.5)
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Papel Tijera, gana user
    elif choiceNomen==1 and choiceUser=="Tijera":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido tijera, y yo papel.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Papel Piedra, gana nomen
    elif choiceNomen==1 and choiceUser=="Piedra":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido piedra, y yo papel.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Papel lagarto, gana user
    elif choiceNomen==1 and choiceUser=="Lagarto":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido lagarto, y yo papel.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()    
    #Papel Spock, gana nomen
    elif choiceNomen==1 and choiceUser=="Spock":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido spock, y yo papel.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    
    #Empate tijera
    elif choiceNomen==2 and choiceUser=="Tijera":
            empatesPPTLS=empatesPPTLS+1
            time.sleep(1)
            print("Has elegido tijera, y yo también. ¡Empate!")
            time.sleep(0.5)
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Tijera Piedra gana user
    elif choiceNomen==2 and choiceUser=="Piedra":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido piedra, y yo tijera.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Tijera Papel gana Nomen
    elif choiceNomen==2 and choiceUser=="Papel":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido papel, y yo tijera.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Tijera lagarto, gana nomen
    elif choiceNomen==2 and choiceUser=="Lagarto":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido lagarto, y yo tijera.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Tijera spock, gana user
    elif choiceNomen==2 and choiceUser=="Spock":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido spock, y yo tijera.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    
    #Empate Lagarto
    elif choiceNomen==3 and choiceUser=="Lagarto":
            empatesPPTLS=empatesPPTLS+1
            time.sleep(1)
            print("Has elegido lagarto, y yo también. ¡Empate!")
            time.sleep(0.5)
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Lagarto Piedra, gana user
    elif choiceNomen==3 and choiceUser=="Piedra":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido piedra, y yo lagarto.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Lagarto papel, gana nomen
    elif choiceNomen==3 and choiceUser=="Papel":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido papel, y yo lagarto.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Lagarto tijera, gana user
    elif choiceNomen==3 and choiceUser=="Tijera":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido tijera, y yo lagarto.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Lagarto spock, gana nomen
    elif choiceNomen==3 and choiceUser=="Spock":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido spock, y yo lagarto.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()

    #Empate Spock
    elif choiceNomen==4 and choiceUser=="Spock":
            empatesPPTLS=empatesPPTLS+1
            time.sleep(1)
            print("Has elegido spock, y yo también. ¡Empate!")
            time.sleep(0.5)
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Spock piedra, gana nomen
    elif choiceNomen==4 and choiceUser=="Piedra":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido piedra, y yo spock.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Spock papel, gana user
    elif choiceNomen==4 and choiceUser=="Papel":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido papel, y yo spock.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Spock tijera, gana nomen
    elif choiceNomen==4 and choiceUser=="Tijera":
            derrotasPPTLS=derrotasPPTLS+1
            time.sleep(1)
            print("Has elegido tijera, y yo spock.")
            time.sleep(0.5)
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
    #Spock lagarto, gana user
    elif choiceNomen==4 and choiceUser=="Lagarto":
            victoriasPPTLS=victoriasPPTLS+1
            time.sleep(1)
            print("Has elegido lagarto, y yo spock.")
            time.sleep(0.5)
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame2()
def restartgame2():
    anss=input()
    if anss=="Y" or anss=="y":
        time.sleep(1)
        print("¡Bien! Vamos allá.")
        time.sleep(0.5)
        print("¿Piedra, papel, tijera, lagarto o spock?")
        opcionPPTLS()
    else:
        menu()

#Pares+Nones
def ParesNones():
    time.sleep(1)
    print("Pares o Nones. ¿Sabes Jugar? (Y/N)")
    answ=input()
    if answ=="Y" or answ=="y":
        time.sleep(1)
        print("¡Bien, pues empecemos!")
        time.sleep(0.5)
        print("Elige: Pares o Nones")
        PrNn()
    elif answ=="N" or answ=="n":
        time.sleep(1)
        print("Es muy sencillo. Primero se elige a que se va a ir, a pares o a nones.")
        time.sleep(0.5)
        print("A continuación cada uno elegimos un número, del 0 al 5, ambos incluidos")
        time.sleep(0.5)
        print("Sumaremos ambos números. Si el numero final es par, gana el que se quedó con los pares.")
        time.sleep(0.5)
        print("Si es impar, gana el que escogió los nones.")
        time.sleep(0.5)
        print("¿Jugamos? (Y/N)")
        answe=input()
        if answe=="Y" or answe=="y":
            time.sleep(1)
            print("¡Bien, pues empecemos!")
            time.sleep(0.5)
            print("¿Pares o Nones?")
            PrNn()
        elif answe=="N" or answe=="n":
            menu()
def PrNn():
    global derrotasPrNn
    global victoriasPrNn
    ChoiceUser=input()
    if ChoiceUser=="Pares" or ChoiceUser=="pares":
        time.sleep(1)
        print("Has elegido Pares. Ahora, ¿qué número quieres jugar?")
        numuser=int(input())
        numnomen=random.randint(0,5)
        resultado=numuser+numnomen
        time.sleep(1)
        print(f"Has elegido {numuser}. ¡Yo he elegido {numnomen}!")
        time.sleep(0.5)
        print(f"{numuser}+{numnomen} es {resultado}")
        if resultado%2==0:
            victoriasPrNn=victoriasPrNn+1
            time.sleep(0.5)
            print(f"{resultado} es par. ¡Has ganado!")
            restartgame3()
        else:
            derrotasPrNn=derrotasPrNn+1
            time.sleep(0.5)
            print(f"{resultado} es impar. ¡He ganado!")
            restartgame3()
    elif ChoiceUser=="Nones" or ChoiceUser=="nones":
        time.sleep(1)
        print("Has elegido Nones. Ahora, ¿qué número quieres jugar?")
        numuser=int(input())
        numnomen=random.randint(0,5)
        resultado=numuser+numnomen
        time.sleep(0.5)
        print(f"Has elegido {numuser}. ¡Yo he elegido {numnomen}!")
        time.sleep(0.5)
        print(f"{numuser}+{numnomen} es {resultado}")
        if resultado%2==0:
            derrotasPrNn=derrotasPrNn+1
            time.sleep(0.5)
            print(f"{resultado} es par. ¡He ganado!")
            restartgame3()
        else:
            victoriasPrNn=victoriasPrNn+1
            time.sleep(0.5)
            print(f"{resultado} es impar. ¡Has ganado!")
            restartgame3()
def restartgame3():
    time.sleep(0.5)
    print("¿Quieres volver a jugar? (Y/N)")
    anss=input()
    if anss=="Y" or anss=="y":
        time.sleep(1)
        print("¡Bien! Vamos allá.")
        time.sleep(0.5)
        print("¿Pares o Nones?")
        PrNn()
    else:
        menu()


#Script
presentacion()



