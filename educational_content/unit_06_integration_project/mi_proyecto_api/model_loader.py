"""Carga el modelo entrenado desde disco."""
import pickle
from pathlib import Path

_model = None


def load_model():
    """Carga el modelo una sola vez (singleton)."""
    global _model
    if _model is None:
        # [ESTUDIANTE: ajusta la ruta a tu modelo guardado]
        model_path = Path("model.pkl")
        if model_path.exists():
            with open(model_path, "rb") as f:
                _model = pickle.load(f)
        else:
            # Modelo simulado para desarrollo — reemplaza con el tuyo
            class _DummyModel:
                def predict(self, features):
                    return [0.0]
            _model = _DummyModel()
    return _model
