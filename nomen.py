nomen="Nomen"

def usernombre():
    user = input()
    print(f"¿Quieres que me refiera a ti como {user}? (Y/N)")
    ans = input()
    if ans=="Y":
        print(f"Encantado de conocerte, {user}")
    else:
        print("Entonces, ¿cómo quieres que te llame?")
        usernombre()

def presentacion():
    print(f"¡Hola! Soy {nomen}. ¿Como te llamas?")
    usernombre()

presentacion()