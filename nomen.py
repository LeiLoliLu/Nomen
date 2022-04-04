import time
import random
nomen="Nomen"
usern="Usuario"
cambianombre=0
victoriasRPS=0

def usernombre():
    global cambianombre
    global usern
    usern = input()
    if usern=="Skip":
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

def opcionRPS():
    choiceUser = input()
    choiceNomen=random.randint(0,3)
    if choiceUser=="Piedra" or choiceUser=="piedra":
        choiceUser="Piedra"
    elif choiceUser=="Papel" or choiceUser=="papel":
        choiceUser="Papel"
    elif choiceUser=="Tijera" or choiceUser=="tijera":
        choiceUser="Tijera"
    else:
        print("¡Esa no es una opción valida!")
        opcionRPS()
    #Empate Piedra
    global victoriasRPS
    if choiceNomen==0 and choiceUser=="Piedra":
        print("Has elegido piedra, y yo también. ¡Empate!")
        print("¿Quieres jugar otra vez? (Y/N)")
        restartgame1()
        #Piedra-Papel, gana user
    elif choiceNomen==0 and choiceUser=="Papel":
            victoriasRPS=victoriasRPS+1
            print("Has elegido papel, y yo piedra.")
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
        #Piedra-Tijera, gana nomen
    elif choiceNomen==0 and choiceUser=="Tijera":
            print("Has elegido tijera, y yo piedra.")
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Empate papel
    elif choiceNomen==1 and choiceUser=="Papel":
            print("Has elegido papel, y yo también. ¡Empate!")
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Papel Tijera, gana user
    elif choiceNomen==1 and choiceUser=="Tijera":
            victoriasRPS=victoriasRPS+1
            print("Has elegido tijera, y yo papel.")
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Papel Piedra, gana nomen
    elif choiceNomen==1 and choiceUser=="Piedra":
            print("Has elegido piedra, y yo papel.")
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Empate tijera
    elif choiceNomen==2 and choiceUser=="Tijera":
            print("Has elegido tijera, y yo también. ¡Empate!")
            print("¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Tijera Piedra gana user
    elif choiceNomen==2 and choiceUser=="Piedra":
            victoriasRPS=victoriasRPS+1
            print("Has elegido piedra, y yo tijera.")
            print("¡Has ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()
    #Tijera Papel gana Nomen
    elif choiceNomen==2 and choiceUser=="Papel":
            print("Has elegido papel, y yo tijera.")
            print("¡He ganado! ¿Quieres jugar otra vez? (Y/N)")
            restartgame1()

def restartgame1():
    ans=input()
    if ans=="Y" or ans=="y":
        print("¡Bien! Vamos allá.")
        print("¿Piedra, papel o tijera?")
        opcionRPS()
    else:
        menu()
    
def RoPaSc():
    print("Piedra, papel o tijera. ¿Sabes Jugar? (Y/N)")
    ans=input()
    if ans=="Y" or ans=="y":
        print("¡Bien, pues empecemos!")
        print("¿Piedra, papel o tijera?")
        opcionRPS()

def presentacion():
    time.sleep(1)
    print(f"¡Hola! Soy {nomen}. ¿Como te llamas?")
    usernombre()

def menu():
    time.sleep(1.2)
    print(f"Vale, {usern}, ¿Qué hacemos ahora?")
    time.sleep(0.5)
    print("1. Jugar a algo")
    time.sleep(0.5)
    print("2. Necesito una calculadora")
    time.sleep(0.5)
    print("3. Quiero cambiar mi nombre")
    opcion=input()
    if opcion=="1":
        time.sleep(1.2)
        print("¡Juegos! Me encantan. ¿A que jugamos?")
        time.sleep(0.5)
        print("1. Piedra, Papel, Tijera")
        time.sleep(0.5)
        print("2. Bloqueado")
        juego=input()
        if juego=="1":
            RoPaSc()
        
    elif opcion=="3":
        time.sleep(1.2)
        print("¿Quieres cambiarte el nombre? ¿A cual?")
        usernombre()
        menu()

presentacion()
