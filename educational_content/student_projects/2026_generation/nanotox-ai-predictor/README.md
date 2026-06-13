# NanoTox AI Predictor

**Autor**: Natalia Bermejo Soto ([@Natalia31-code](https://github.com/Natalia31-code))  
**Curso**: IA Aplicada a Nanotecnología - Generación 2026  
**Instructor**: Mtro. Luis José Yudico Anaya  
**Fecha**: Junio 2026  
**Proyecto Integrador Unidad 6**

---

## 📝 Descripción

Este proyecto desarrolla un **Sistema de Predicción de Nanotoxicidad** automatizado impulsado por un sistema multi-agente con LangGraph y modelos de Machine Learning. El objetivo es determinar si una nanopartícula metálica específica resultará tóxica para las células en función de sus propiedades fisicoquímicas, ahorrando tiempo y costos frente a los ensayos tradicionales in vitro e in vivo.

El enfoque propuesto integra la ingesta automática de datos (desde Zenodo y la API de Materials Project), el entrenamiento y evaluación paralela de tres modelos clásicos (Random Forest, SVM y Multilayer Perceptron), y la exposición de los resultados a través de un panel de control interactivo premium diseñado en HTML5/CSS3/JS, servido por una API FastAPI.

---

## 🎯 Objetivos

- [x] **Paso 1**: Definir la pregunta de investigación y estructurar la propuesta.
- [x] **Paso 2**: Seleccionar herramientas e instrumentar el inventario tecnológico.
- [x] **Paso 3**: Implementar el pipeline de datos y entrenar modelos de clasificación (Random Forest, SVM, MLP).
- [x] **Paso 4**: Crear y desplegar la API REST con FastAPI.
- [x] **Paso 5**: Crear un dashboard interactivo premium con animaciones moleculares y buscador inteligente.
- [x] **Paso 6**: Completar el mapa de habilidades y la autoevaluación académica.

---

## 🚀 Características Principales

- ✅ **Buscador con autocompletado inteligente:** Permite ingresar nanopartículas comunes (ZnO, Ag, TiO₂...) autocompletando sus propiedades típicas de manera instantánea.
- ✅ **Modo Personalizado Dinámico:** Permite ingresar cualquier nanopartícula personalizada, configurar sus deslizadores manualmente y estimar su toxicidad en base al modelo de Machine Learning.
- ✅ **Indicador de Riesgo y Colores:** Visualiza el resultado mediante un medidor circular animado y colores semáforo según el nivel de riesgo (Bajo = Verde, Moderado = Amarillo, Alto = Rojo).
- ✅ **Aplicaciones Estimadas:** Indica dinámicamente para qué sirve la nanopartícula analizada y cuáles son sus aplicaciones más probables (ej. biomedicina, catálisis, sensores) según sus características.
- ✅ **Historial de Consultas:** Guarda en memoria local las últimas 5 búsquedas realizadas para una navegación ágil.

---

## 🛠️ Stack Tecnológico

### Core & IA
- **Python**: 3.11
- **Machine Learning**: scikit-learn (Random Forest, SVM, MLP Classifier), NumPy, Pandas
- **Orquestación**: LangGraph StateGraph (Sistema de 9 agentes integrados)
- **Trazabilidad**: LangSmith

### Scientific APIs
- **Zenodo API**: Repositorio de datos HaHa-Manual.csv (nanotoxicidad curada de literatura).
- **Materials Project API**: Recuperación de propiedades cristalinas y fisicoquímicas complementarias.

### Deployment & Frontend
- **API**: FastAPI + Uvicorn
- **Base de datos**: Neo4j AuraDB (Memoria persistente) + ChromaDB (Memoria semántica)
- **Frontend**: Dashboard web integrado (HTML5, CSS3 Glassmorphism, Vanilla JS)
- **Hosting**: Render (Despliegue público en la nube)

---

## 📦 Instalación y Uso Local

### Prerrequisitos
- Python 3.11
- Entorno Conda (`ia_nano`)

### Paso a Paso

1. **Clonar tu Fork del repositorio**:
   ```bash
   git clone https://github.com/Natalia31-code/Antigravity-Nano-Research-Multiagentic-Core.git
   cd Antigravity-Nano-Research-Multiagentic-Core/educational_content/student_projects/2026_generation/nanotox-ai-predictor
   ```

2. **Activar el entorno del curso**:
   ```bash
   conda activate ia_nano
   ```

3. **Iniciar el servidor local**:
   Puedes iniciar el servidor web ejecutando el archivo `.bat` (haciendo doble clic o desde terminal):
   ```bash
   INICIAR_NANOTOX.bat
   ```
   O manualmente ejecutando:
   ```bash
   cd nanotox_api
   python app.py
   ```

4. **Probar en tu navegador**:
   Abre [http://localhost:8000](http://localhost:8000) en cualquier navegador web.

---

## 🌐 Enlace de Despliegue en la Nube
El proyecto está desplegado permanentemente y listo para ser probado en línea por el profesor en:
👉 **[https://nanotox-ai.onrender.com](https://nanotox-ai.onrender.com)**
