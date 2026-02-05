# =========================
# IMPORTS
# =========================

import random                     # Genera números aleatorios (simula el azar del juego)
import numpy as np                # Operaciones numéricas eficientes (promedios, arrays)
import matplotlib.pyplot as plt   # Gráficas
from multiprocessing import Pool, cpu_count
# Pool: crea un grupo de procesos en paralelo
# cpu_count(): devuelve el número de núcleos disponibles en tu CPU


# =========================
# PARÁMETROS DEL JUEGO
# =========================

COSTO = 1                         # Costo fijo por cada jugada
prizes = [5, 10, 15, 20, 20, 30, 30, 100]
# Lista de premios posibles según la posición ganadora


# =========================
# PARÁMETROS MONTE CARLO
# =========================

MAX_N = 100                       # Número máximo de jugadas por experimento
REPETICIONES = 5000               # Número de experimentos Monte Carlo independientes


# =========================
# FUNCIÓN DE JUEGO
# =========================

def jugar(posicionElegida):
    # Genera un número aleatorio entre 0 y 7 (posición ganadora), puede que la maquina en si no 
    # genere numeros aleatorios si no que la funcion dependa de otros valores como el numero de monedas que ya tiene dentro o el tiempo que lleva  un premio sin ser ganado 
    # pero para este caso es suficiente
    resultado = random.randint(0, 7)

    # Si el resultado coincide con la posición elegida, se gana el premio
    # Si no, el premio es 0
    premio = prizes[resultado] if resultado == posicionElegida else 0

    # Retorna la ganancia neta: premio menos el costo de jugar
    return premio - COSTO


# =========================
# UNA SIMULACIÓN COMPLETA
# =========================

def simulacion(_):
    # Lista donde se guardará:
    # (N, ganancia_promedio) para cada N
    resultados = []

    # Se prueba cada N desde 1 hasta MAX_N
    for N in range(1, MAX_N + 1):

        # Se juega N veces y se guardan las ganancias individuales
        ganancias = [jugar(posicionUsuario) for _ in range(N)]

        # Se calcula la ganancia promedio para ese N
        promedio = np.mean(ganancias)

        # Se guarda el par (N, promedio)
        resultados.append((N, promedio))

    # Se busca el N que maximiza la ganancia promedio
    mejorN, mejorGanancia = max(resultados, key=lambda x: x[1])

    # Se devuelve el mejor N y su ganancia asociada
    return mejorN, mejorGanancia


# =========================
# MAIN (PUNTO DE ENTRADA)
# =========================

if __name__ == "__main__":
    # Esta condición es OBLIGATORIA cuando se usa multiprocessing
    # Evita que los procesos hijos vuelvan a ejecutar el script completo


    # =========================
    # INPUT DEL USUARIO
    # =========================

    posicionUsuario = int(input(
        "Elige la posición a apostar:\n"
        "1 ($5)\n"
        "2 ($10)\n"
        "3 ($15)\n"
        "4 ($20)\n"
        "5 ($20)\n"
        "6 ($30)\n"
        "7 ($30)\n"
        "8 ($100)\n> "
    )) - 1
    # Se resta 1 para pasar de índices humanos (1–8) a índices Python (0–7)


    # =========================
    # MULTIPROCESSING
    # =========================

    nProcesos = cpu_count()
    # Detecta automáticamente cuántos núcleos tiene la CPU

    print(f"Usando {nProcesos} procesos")

    # Se crea un pool de procesos (uno por núcleo)
    with Pool(processes=nProcesos) as pool:

        # pool.map:
        # - Ejecuta 'simulacion' en paralelo
        # - Cada llamada es un experimento Monte Carlo independiente
        # - range(REPETICIONES) solo sirve para repetir la función
        resultados = pool.map(simulacion, range(REPETICIONES))


    # =========================
    # POSTPROCESAMIENTO
    # =========================

    # Se separan los resultados:
    # mejoresN = todos los N óptimos
    # mejoresGanancias = todas las ganancias óptimas
    mejoresN, mejoresGanancias = zip(*resultados)

    # Se convierten a arrays de NumPy para análisis estadístico
    mejoresN = np.array(mejoresN)
    mejoresGanancias = np.array(mejoresGanancias)


    # =========================
    # RESULTADOS NUMÉRICOS
    # =========================

    print("Número promedio de iteraciones óptimas:", np.mean(mejoresN))
    print("Ganancia promedio en el óptimo:", np.mean(mejoresGanancias))


    # =========================
    # VISUALIZACIÓN
    # =========================

    plt.figure(figsize=(10, 6))  # Tamaño de la figura

    # Scatter plot:
    # - Eje X: N óptimo
    # - Eje Y: ganancia promedio
    # - Color depende de la ganancia
    sc = plt.scatter(
        mejoresN,
        mejoresGanancias,
        c=mejoresGanancias,
        cmap="RdYlGn",
        alpha=0.7
    )

    # Línea horizontal en ganancia = 0 (punto de equilibrio)
    plt.axhline(0, linestyle='--', linewidth=2, color='black')

    # Etiquetas
    plt.xlabel("Número de iteraciones con mejor ganancia (N*)")
    plt.ylabel("Ganancia promedio máxima")
    plt.title("Distribución de N óptimo y su ganancia promedio")

    # Barra de color
    cbar = plt.colorbar(sc)
    cbar.set_label("Ganancia promedio")

    plt.grid(True)
    plt.show()
