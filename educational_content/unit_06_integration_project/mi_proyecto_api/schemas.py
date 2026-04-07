"""Schemas Pydantic para ...."""
from pydantic import BaseModel


class InputData(BaseModel):
    # [ESTUDIANTE: adapta los tipos a los datos reales de tu modelo]
        # [ESTUDIANTE: define los campos de entrada]
    pass  # Elimina este pass cuando agregues campos


class PredictionResult(BaseModel):
        # [ESTUDIANTE: define los campos de salida]
    modelo_version: str
    pass  # Elimina este pass cuando agregues campos
