from pathlib import Path

from src import predictor


def main():
    ruta_modelo = Path(__file__).resolve().parent / "modelo" / "modelo.json"
    clasificador = predictor(str(ruta_modelo))
    return clasificador.decideYPregunta()


if __name__ == "__main__":
    main()
