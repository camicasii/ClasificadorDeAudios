import time
from pathlib import Path

from src import predictor


def main():
    ruta_modelo = Path(__file__).resolve().parent / "modelo" / "modelo.json"
    clasificador = predictor(str(ruta_modelo))

    for segundos in range(3, 0, -1):
        print(f"La grabación comenzará en {segundos}...")
        time.sleep(1)

    return clasificador.decideYPregunta()


if __name__ == "__main__":
    main()
