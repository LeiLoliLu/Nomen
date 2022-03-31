import time
nomen="Nomen"

def usernombre():
    user = input()
    time.sleep(1.2)
    print(f"¿Quieres que me refiera a ti como {user}? (Y/N)")
    ans = input()
    time.sleep(1.2)
    if ans=="Y":
        print(f"Encantado de conocerte, {user}")
    else:
        print("Entonces, ¿cómo quieres que te llame?")
        usernombre()

def presentacion():
    time.sleep(1)
    print(f"¡Hola! Soy {nomen}. ¿Como te llamas?")
    usernombre()

presentacion()