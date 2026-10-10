import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def curva_gaussiana(x, media, desviacion):
    return np.exp(-0.5 * ((x - media) / desviacion) ** 2) / (
        desviacion * np.sqrt(2 * np.pi)
    )


def grafica_caracteristica(eje, modelo, sufijo, titulo):
    media_femenina = modelo[f"fmed{sufijo}Feme"]
    media_masculina = modelo[f"fmed{sufijo}Masc"]
    prefijo_desviacion = "desvAc" if sufijo == "AC" else "desvPC"
    desviacion_femenina = modelo[f"{prefijo_desviacion}Feme"]
    desviacion_masculina = modelo[f"{prefijo_desviacion}Masc"]

    if desviacion_femenina <= 0 or desviacion_masculina <= 0:
        raise ValueError(
            f"Las desviaciones estándar deben ser mayores que cero para graficar {titulo}."
        )

    minimo = min(
        media_femenina - 4 * desviacion_femenina,
        media_masculina - 4 * desviacion_masculina,
    )
    maximo = max(
        media_femenina + 4 * desviacion_femenina,
        media_masculina + 4 * desviacion_masculina,
    )
    frecuencias = np.linspace(minimo, maximo, 500)

    eje.plot(
        frecuencias,
        curva_gaussiana(frecuencias, media_femenina, desviacion_femenina),
        label="Femenino",
    )
    eje.plot(
        frecuencias,
        curva_gaussiana(frecuencias, media_masculina, desviacion_masculina),
        label="Masculino",
    )
    eje.set_title(titulo)
    eje.set_xlabel("Frecuencia (Hz)")
    eje.set_ylabel("Densidad de probabilidad")
    eje.grid(True, alpha=0.3)
    eje.legend()


def main():
    ruta_modelo = Path(__file__).resolve().parent / "modelo" / "modelo.json"
    with ruta_modelo.open("r", encoding="utf-8") as archivo:
        modelo = json.load(archivo)

    figura, ejes = plt.subplots(1, 2, figsize=(12, 5))
    grafica_caracteristica(ejes[0], modelo, "AC", "Autocorrelación")
    grafica_caracteristica(ejes[1], modelo, "PC", "Primera colina")
    figura.suptitle("Distribuciones de frecuencia por género")
    figura.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
