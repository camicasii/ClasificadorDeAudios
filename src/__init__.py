"""API pública del paquete de clasificación de voces."""

from .analizador import Analizador
from .extractor import Extractor
from .grabador import grabador
from .lector import Lector
from .predictor import predictor

__all__ = [
    "Analizador",
    "Extractor",
    "grabador",
    "Lector",
    "predictor",
]
