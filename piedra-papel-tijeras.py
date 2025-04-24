nombre1 = input("¿Cómo te llamas jugador n°1? ")
nombre2 = input("¿Cómo te llamas jugador n°2? ")

eleccion1 = input(f"{nombre1}¿Qué elijes?,¿Piedra, Papel o Tijera?: ").lower()
eleccion2 = input(f"{nombre2}¿Qué elijes?, ¿Piedra, Papel o Tijera?: ").lower()

condicion1 = eleccion1 == "piedra" and eleccion2 == "tijera"
condicion2 = eleccion1 == "papel" and eleccion2 == "piedra"
condicion3 = eleccion1 == "tijera" and eleccion2 == "papel"

if eleccion1 == eleccion2:
    print ("¡Ha sido un empate!")
elif  condicion1 or condicion2 or condicion3:
    print (f"{nombre1},¡Felicidades! Ha ganado")
else:
    print (f"{nombre2},¡Felicidades! Ha ganado")

