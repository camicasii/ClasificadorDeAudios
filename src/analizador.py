import numpy as np
import json
import os

class Analizador:
    def __init__(self):
        pass

    @classmethod
    def analizaCarpeta(cls, carpeta, extractor):
        import os
        from lector import Lector
        archivos = [f for f in os.listdir(carpeta) if f.endswith('.wav')]
        freqAutoC = np.zeros(len(archivos))
        freqPCol = np.zeros(len(archivos))
        i = 0
        for archivo in archivos:            
            
            ruta = carpeta + archivo
            sennal, sr = Lector.lee(ruta)
            freqAutoC[i], freqPCol[i] = extractor.extrae(sennal, sr)
            i+=1
            
        fmedAC = freqAutoC.mean()
        desvAC = freqAutoC.std()
        fmedPC = freqPCol.mean()
        desvPC = freqPCol.std()
        return [fmedAC,desvAC,fmedPC,desvPC,i]

    @classmethod
    def analizaYGuarda(cls, carpetaFeme, carpetaMasc, extractor, nombreArchivo="modelo.json"):
        datosFeme = cls.analizaCarpeta(carpetaFeme, extractor)
        datosMasc = cls.analizaCarpeta(carpetaMasc, extractor)

        fmedACFeme, desvACFeme, fmedPCFeme, desvPCFeme, nFeme = datosFeme
        fmedACMasc, desvACMasc, fmedPCMasc, desvPCMasc, nMasc = datosMasc

        modelo = {
            "fmedACFeme": float(fmedACFeme),
            "desvAcFeme": float(desvACFeme),
            "fmedPCFeme": float(fmedPCFeme),
            "desvPCFeme": float(desvPCFeme),
            "nFemeAC": int(nFeme),
            "nFemePC": int(nFeme),

            "fmedACMasc": float(fmedACMasc),
            "desvAcMasc": float(desvACMasc),
            "fmedPCMasc": float(fmedPCMasc),
            "desvPCMasc": float(desvPCMasc),
            "nMascAC": int(nMasc),
            "nMascPC": int(nMasc),
        }

        # Carpeta "modelo" al mismo nivel que "data" y "src"
        carpetaModelo = os.path.join(os.path.dirname(__file__), "..", "modelo")
        carpetaModelo = os.path.abspath(carpetaModelo)
        os.makedirs(carpetaModelo, exist_ok=True)

        rutaArchivo = os.path.join(carpetaModelo, nombreArchivo)
        with open(rutaArchivo, "w", encoding="utf-8") as archivo:
            json.dump(modelo, archivo, indent=4)

        return modelo
            
