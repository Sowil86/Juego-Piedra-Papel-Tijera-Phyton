
nombre1 = input("¿Cómo te llamas jugador n°1? ")
nombre2 = input("¿Cómo te llamas jugador n°2? ")


nombre1 = input("¿Qué elijes?¿Piedra, Papel o Tijera?: ")
nombre2 = input("¿Qué elijes?¿Piedra, Papel o Tijera?: ")

condicion1 = nombre1 == "piedra" and nombre2 == "tijeras"
condicion2 = nombre1 == "papel" and nombre2 == "piedra"
condicion3 = nombre1 == "tijeras" and nombre2 == "papel"

if nombre1 == nombre2:
    print ("¡Ha sido un empate!")
elif  condicion1 or condicion2 or condicion3:
    print ("¡Felicidades! Ha ganado: ", nombre1)
else:
    print ("¡Felicidades! Ha ganado: ", nombre2)
