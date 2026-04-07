# ...

API de prediccion generada por el Proyecto Integrador del curso Nanotecnologia + IA.

## Ejecutar localmente

```bash
pip install -r requirements.txt
python app.py
```

Visita http://localhost:8000/docs para la documentacion interactiva.

## Ejecutar con Docker

```bash
docker build -t ... .
docker run -p 8000:8000 ...
```

## Endpoints

- `GET /health` — Estado del servicio
- `POST /predict` — Prediccion (ver /docs para el schema)
