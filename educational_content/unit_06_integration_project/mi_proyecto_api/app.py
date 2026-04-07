"""API FastAPI para ...."""
from fastapi import FastAPI, HTTPException
from schemas import InputData, PredictionResult
from model_loader import load_model

app = FastAPI(
    lifespan=lifespan,
    title="...",
    description="...",
    version="1.0.0",
)


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Patron correcto para FastAPI >= 0.93 (reemplaza @app.on_event deprecated)
    load_model()  # startup: pre-carga el modelo una sola vez
    yield
    # shutdown: libera recursos si necesario


@app.get("/health")
def health():
    """Verifica que el servicio esta operativo."""
    return {"status": "ok", "servicio": "..."}


@app.post("/predict", response_model=PredictionResult)
def predict(data: InputData):
    """Realiza una prediccion con los datos de entrada."""
    model = load_model()
    try:
        # [ESTUDIANTE: extrae los features de `data` en el orden que espera tu modelo]
        features = []
        # Ej: features = [data.tamano_nm, data.zeta_potential]

        resultado = model.predict([features])[0]

        # [ESTUDIANTE: construye el PredictionResult con tu output real]
        return PredictionResult(
            modelo_version="1.0.0"
            # Ej: band_gap_ev=float(resultado),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
