import time
nomen="Nomen"
usern="Usuario"
cambianombre=0
def usernombre():
    global cambianombre
    global usern
    usern = input()
    time.sleep(1.2)
    print(f"¿Quieres que me refiera a ti como {usern}? (Y/N)")
    ans = input()
    time.sleep(1.2)
    if ans=="Y" and cambianombre>0 or ans=="y" and cambianombre>0:
        print(f"Vale, ahora te llamaré {usern}")
    elif ans=="Y" and cambianombre==0 or ans=="y" and cambianombre==0:
        print(f"Encantado de conocerte, {usern}")
        cambianombre=cambianombre+1
    else:
        print("Entonces, ¿cómo quieres que te llame?")
        usernombre()

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
    if opcion=="3":
        time.sleep(1.2)
        print("¿Quieres cambiarte el nombre? ¿A cual?")
        usernombre()
        menu()



presentacion()
time.sleep(2.5)
menu()
time.sleep(10)
exit()