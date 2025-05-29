import random
import random
import string
print("Un día cualquiera, tu y tus 3 amigos estáis caminando por el San Francisto y decidís ir a ver el HUCA antiguo, pues nunca lo habiais visto por dentro. Saltais la valla de atrás y os colais al terreno.")
print("Vais todos juntos y, de la nada, caeís en un pozo, cubierto por muchas hojas; una trampa. Despertais todos en distintas habitaciones, puedes observar alrededor y ves un libro.")
print("Derrepente, una voz suena: Cada uno de vosotros está en una distinta habitación, la habitación cada segundo se va a ir estrechando, teneís 10 minutos.")
print("Después del pánico, decidis intentar resolverlo. ")
import random

# Diccionario de colores por nombre
colores_por_nombre = {
    "rojo": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF",
    "amarillo": "#FFFF00",
    "negro": "#000000",
    "blanco": "#FFFFFF",
    "naranja": "#FFA500",
    "morado": "#800080",
    "rosa": "#FFC0CB",
    "gris": "#808080"
}
# Elegir 4 colores aleatorios (solo nombres, no hex)

colores_aleatorios = random.sample(list(colores_por_nombre.keys()), 4)

print(f"Tu amiga tiene 4 colores en su puerta: {colores_aleatorios}")

# Elegir 4 números aleatorios del 1 al 10

numeros_aleatorios = [random.randint(1, 10) for _ in range(4)]

print(f"Tu otro amigo tiene 4 números: {numeros_aleatorios}")

# Elegir 4 letras aleatorias

letras_aleatorias = random.choices(string.ascii_uppercase, k=4)

print(f"Otro amigo comenta que tiene 4 letras: {letras_aleatorias}")

# Generar 4 códigos únicos combinando un color, un número y una letra

combinaciones = list(zip(colores_aleatorios, numeros_aleatorios, letras_aleatorias))

random.shuffle(combinaciones)

codigos = [f"{color}-{numero}-{letra}" for color, numero, letra in combinaciones]

# Elegir uno correcto al azar

codigo_correcto = random.choice(codigos)

print("\nTú tienes un libro con 4 posibles códigos para abrir la puerta:")

for i, codigo in enumerate(codigos, 1):
    print(f"Código {i}: {codigo}")

# Intentos del jugador

intentos = 3

while intentos > 0:

    eleccion = input("\nIntroduce el número del código que crees que es correcto (1-4): ")

    if not eleccion.isdigit() or int(eleccion) not in range(1, 5):
        print("Por favor, introduce un número válido entre 1 y 4.")

        continue

    elegido = codigos[int(eleccion) - 1]

    if elegido == codigo_correcto:

        print("¡Correcto! Has desbloqueado la puerta.")

        break

    else:

        intentos -= 1

        if intentos > 0:

            print(f"Incorrecto. Te quedan {intentos} intento(s).")

        else:

            print("\nGAME OVER")

print("Has conseguido abrir la primera puerta de todos vosotros, felicitaciones. Al entrar en la siguiente sala, te das cuenta")
print("Que ya no puedes hablar con tus amigos, la habitación esta insonorizada. Ves en frente tuya un robot, dispuesto al lado")
print("De una pizarra, con ganas de jugar al tres en raya. La voz misteriosa vuelve a alzarse; 'Impide que gane, o muere', dice.")
import random

def mostrar_tablero(tablero):
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

def jugada_ia(tablero):
    opciones = [i for i in range(9) if tablero[i] == ' ']
    return random.choice(opciones)

def jugar_tres_en_raya():
    tablero = [' ' for _ in range(9)]  # Tablero vacío
    jugador_actual = 'X'  # El jugador humano es X
    turno = 0

    while turno < 9:
        mostrar_tablero(tablero)

        if jugador_actual == 'X':
            print(f"Tu turno, jugador {jugador_actual} (Tú):")
            try:
                jugada = int(input("Ingresa un número del 1 al 9 para colocar tu marca: ")) - 1
                if tablero[jugada] != ' ':
                    print("Esa casilla ya está ocupada. Intenta de nuevo.")
                    continue
            except (ValueError, IndexError):
                print("Entrada inválida. Debes ingresar un número entre 1 y 9.")
                continue
        else:
            print("Turno de la IA (O)...")
            jugada = jugada_ia(tablero)

        # Colocar la marca en el tablero
        tablero[jugada] = jugador_actual

        # Verificar si hay un ganador
        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            if jugador_actual == 'X':
                print("¡Ganaste! ¡Eres el mejor!")
            else:
                print("La IA ha ganado... ¡Y ahora tú... mueres!")
                break

        # Cambiar de turno
        jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        turno += 1

    if turno == 9 and not verificar_ganador(tablero, 'X') and not verificar_ganador(tablero, 'O'):
        mostrar_tablero(tablero)
        print("¡Empate! Nadie muere... por ahora.")
jugar_tres_en_raya()
import random
print("Has ganado al robot, felicitaciones. Se abre una puerta y pasas a la siguiente sala. ")
print("En esta sala ves 5 objetos, al mirar los objetos ves que en cada uno hay un número.")
print("Resuelve el acertijo con la ayuda de estos numeros.")
#Funcion que genera el siguiente numero en la secuela de cuadrados perfectos
def generar_siguiente_cuadrado(n):
    return (n+1)**2

# Generar los primeros 5 cuadrados perfectos
objetos=[1,4,9,16,25] # Cuadrados perfectos de 1,2,3,4,5
# El siguiente numero que falta en la secuencia sera el cuadrado de 6 (36)
respuesta_correcta=generar_siguiente_cuadrado(5)

#Desordenamos la lista de objetos para simular que no estan en orden
#Asegurandonos de no incluir el numero faltante en la secuencia mostrada
objetos_mezclados=objetos #No incluir la respuesta correcta en los objetos iniciales
random.shuffle(objetos_mezclados)

#Mostrar los objetos con sus numeros(sin revelar cual es el que falta)
print("Objetos en la habitacion:")
for i,objeto in enumerate(objetos_mezclados):
  print(f"Objeto { i + 1}: {objeto}")

# El jugador tiene que adivinar el siguiente numero en la secuencia
adivinanza= int(input("\n¿Que numero debe seguir en la secuencia de cuadrados perfectos?"))

# Verificar si la respuesta es correcta
if adivinanza == respuesta_correcta:
   print("\n¡Correcto! El siguiente numero es:" , respuesta_correcta)
else:
     print("\nIncorrecto. El numero correcto es:" , respuesta_correcta)
import random

# Función para calcular el tiempo usando la fórmula t = d / v
def calcular_tiempo(distancia, velocidad):
    # Calculamos el tiempo
    tiempo = distancia / velocidad
    return tiempo

# Historia del Escape room
print(" ¡ Te encuentras atrapado en una habitación oscura y silenciosa! ")
print(" Enfrente de ti , hay una puerta cerrada .")
print(" En la pantalla de la cerradura aparece el siguiente mensaje: ")
print("\"Para abrir la puerta y escapar , debes el tiempo exacto ")


# Función para calcular el tiempo usando la fórmula t = d / v
def calcular_tiempo(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo


# Historia final del Escape Room
print("\nHas superado todas las pruebas anteriores, cada una más difícil que la anterior.")
print("Ahora te encuentras frente a la última puerta, más antigua que el resto, con inscripciones talladas a mano.")
print("En la parte superior, una frase dice: ‘El tiempo es la clave de la libertad’.")
print("Debajo, un panel se ilumina con un nuevo acertijo.")

print("\nUna voz mecánica resuena por última vez en la sala:")
print("“Este es tu último desafío. Si fallas, la sala se cerrará para siempre.”")
print("“Debes calcular cuánto tiempo tardarías en cruzar el pasillo final.”")

print("\nEncuentras una nota junto al marco de la puerta:")
print("d = Distancia (en metros)")
print("v = Velocidad (en metros por segundo)")
print("t = Tiempo (en segundos)")

# Datos finales
distancia = 120  # metros
velocidad = 30  # m/s

# Información para el jugador
print(f"\nLa distancia del pasillo es de {distancia} metros.")
print(f"La velocidad a la que puedes cruzarlo es de {velocidad} metros por segundo.")

# Entrada del jugador
respuesta = float(input("\n¿Cuánto tiempo (en segundos) tardarías en cruzarlo? "))

# Cálculo correcto
tiempo_correcto = calcular_tiempo(distancia, velocidad)

# Resultado final
if respuesta == tiempo_correcto:
    print("\n¡Correcto! La puerta emite un clic suave y se abre lentamente.")
    print("Luz natural inunda la sala. Has salido del escape room.")
    print("¡Felicidades! Has demostrado inteligencia, lógica y valor.")
else:
    print("\nLa cerradura emite un pitido agudo. La puerta no se mueve.")
    print("Respuesta incorrecta. Aún no puedes escapar. Intenta de nuevo.")

print("Finalmente, después de horas de desesperación, lograste encontrar la salida pero al salir, te encontraste con un silencio inquietante.")
print("La realidad te golpeó: tú eras el último en salir, pero tambien el único que quedó vivo de tus amigos.")
print("A pesar de que sobreviviste, el mundo no es el mismo")

