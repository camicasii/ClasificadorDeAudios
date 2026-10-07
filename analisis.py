import os
from pathlib import Path

from src import Analizador, Extractor


def main():
    raiz_proyecto = Path(__file__).resolve().parent
    carpeta_femenina = raiz_proyecto / "data" / "feminine"
    carpeta_masculina = raiz_proyecto / "data" / "masculine"

    for carpeta in (carpeta_femenina, carpeta_masculina):
        if not carpeta.is_dir():
            raise FileNotFoundError(f"No se encontró la carpeta: {carpeta}")

        if not any(archivo.suffix.lower() == ".wav" for archivo in carpeta.iterdir()):
            raise ValueError(f"La carpeta no contiene archivos WAV: {carpeta}")

    extractor = Extractor()
    modelo = Analizador.analizaYGuarda(
        str(carpeta_femenina) + os.sep,
        str(carpeta_masculina) + os.sep,
        extractor,
    )

    ruta_modelo = raiz_proyecto / "modelo" / "modelo.json"
    print(f"Análisis completado. Modelo guardado en: {ruta_modelo}")
    return modelo


if __name__ == "__main__":
    main()
