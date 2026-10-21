import random


def calcular_resultados(aciertos: int, errores: int) -> tuple[int, int]:
    """
    Calcula las preguntas respondidas y la puntuación de la partida.
    :param aciertos: número de preguntas acertadas
    :param errores: número de preguntas falladas
    :return: tupla (preguntas respondidas, puntuación), en ese orden
    """
    preguntas_respondidas: int = aciertos + errores
    puntuacion: int = (aciertos * 3) - errores

    return preguntas_respondidas, puntuacion


def valorar_partida(puntuacion: int) -> int:
    """
    Devuelve la posición del mensaje de valoración:
    0 si la puntuación es inferior a 10,
    1 si está entre 10 y 19, ambos incluidos,
    2 si es de 20 o más.
    :param puntuacion: puntuación total de la partida
    :return: índice de la valoración (0, 1 o 2)
    """
    if puntuacion < 10:
        valoracion = 0
    elif puntuacion >= 20:
        valoracion = 2
    else:
        valoracion = 1

    return valoracion


def main():
    """
    Función principal.
    """
    # Entrada
    preguntas: int = 10
    aciertos: int = random.randint(0, preguntas)
    errores: int = random.randint(0, preguntas - aciertos)

    # Proceso
    resultado: tuple[int, int] = calcular_resultados(aciertos, errores)
    puntuacion: int = resultado[1]
    valoracion: int = valorar_partida(puntuacion)

    # Salida
    print(f"Preguntas respondidas: {resultado[0]}")
    print(f"Puntuación: {puntuacion}")

    if valoracion == 0:
        print("Sigue practicando")
    elif valoracion == 1:
        print("Buen resultado")
    else:
        print("Excelente")


if __name__ == "__main__":
    main()