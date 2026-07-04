# Educational Content - Antigravity Nano Research

Esta sección contiene material educativo estructurado para aprender **IA aplicada a Nanotecnología** usando el sistema multi-agente.

---

## 📚 Unidades Disponibles

### ✅ Unidad 1: Modelado a Nanoescala
**Ruta**: [`unit_01_nanoscale_modeling/`](unit_01_nanoscale_modeling/)

**Contenido**:
- Fundamentos de simulación molecular
- Atomic Simulation Environment (ASE)
- Optimización de estructuras
- Análisis de nanopartículas de oro
- Visualización 3D con NGLView

**Nivel**: Licenciatura - Posgrado  
**Duración estimada**: 4-6 horas  
**Prerrequisitos**: Python básico, conceptos de química general

[📓 Ir a la Unidad 1](unit_01_nanoscale_modeling/)

---

### ✅ Unidad 2: Simulación Molecular Avanzada
**Ruta**: [`unit_02_molecular_simulation/`](unit_02_molecular_simulation/)

**Contenido** (2 notebooks):
- **Parte 1**: Dinámica Molecular (MD)
  - Potenciales interatómicos (Lennard-Jones, EAM, Tersoff)
  - Ensembles termodinámicos (NVE, NVT, NPT)
  - Análisis de trayectorias y propiedades de transporte
- **Parte 2**: DFT y Nanofabricación
  - Teoría del Funcional de la Densidad (DFT)
  - Optimización de estructuras
  - Cálculo de propiedades electrónicas
  - Diseño de nanoestructuras

**Nivel**: Licenciatura avanzada - Posgrado  
**Duración estimada**: 7-9 horas (ambas partes)  
**Prerrequisitos**: Unidad 1, mecánica cuántica básica, termodinámica estadística (recomendado)

[📓 Ir a la Unidad 2](unit_02_molecular_simulation/)

---

### ✅ Unidad 3: Machine Learning para Nanomateriales
**Ruta**: [`unit_03_ml_nanomaterials/`](unit_03_ml_nanomaterials/)

**Contenido** (2 notebooks):
- **Parte 1**: Fundamentos de ML
  - Algoritmos clásicos (Random Forest, SVM, regresión)
  - Feature engineering y descriptores moleculares
  - Validación cruzada y métricas científicas
- **Parte 2**: Redes Neuronales
  - Arquitecturas DNN para predicción de propiedades
  - Graph Neural Networks (GNN) para moléculas
  - Interpretabilidad con SHAP values

**Nivel**: Licenciatura avanzada - Posgrado  
**Duración estimada**: 9-11 horas (ambas partes)  
**Prerrequisitos**: Unidades 1 y 2, álgebra lineal, Python intermedio

[📓 Ir a la Unidad 3](unit_03_ml_nanomaterials/)

---

### ✅ Unidad 4: IA Aplicada a Nanotecnología y Datos Experimentales
**Ruta**: [`unit_04_applied_ai/`](unit_04_applied_ai/)

**Contenido** (2 notebooks):
- **Parte 1**: IA Aplicada a Propiedades de Materiales
  - Neural Network Potentials (NNP) con funciones de simetría SOAP
  - Predicción de bandgap con Random Forest y Gradient Boosting
  - Optimización Bayesiana y Algoritmos Genéticos
  - Modelos Generativos (VAE y GANs)
- **Parte 2**: Análisis de Datos Experimentales
  - Procesamiento de imágenes SEM/TEM (Watershed, Otsu, U-Net)
  - Clasificación de espectros UV-Vis de nanopartículas (Au, Ag, Cu)
  - PCA, t-SNE y detección de anomalías con Isolation Forest

**Nivel**: Licenciatura avanzada — Posgrado
**Duración estimada**: 9-13 horas (ambas partes)
**Prerrequisitos**: Unidades 1, 2 y 3

[📓 Ir a la Unidad 4](unit_04_applied_ai/)

---

### ✅ Unidad 5: Sistemas Multi-Agente e IA Generativa
**Ruta**: [`unit_05_multi_agent_sys/`](unit_05_multi_agent_sys/)

**Contenido** (10 notebooks):
- Fundamentos de agentes modernos
- Orquestación avanzada (LangGraph, CrewAI, Google ADK)
- Memoria avanzada (RAG, Graph RAG)
- Agentes multimodales y producción

**Nivel**: Posgrado / Especialización  
**Duración estimada**: 12-16 horas  
**Prerrequisitos**: Unidades 1 a 4

[📓 Ir a la Unidad 5](unit_05_multi_agent_sys/)

---

### ✅ Unidad 6: Proyecto de Integración
**Ruta**: [`unit_06_integration_project/`](unit_06_integration_project/)

**Contenido** (6 notebooks):
- Propuesta de proyecto y catalogación de herramientas
- Scaffold de implementación adaptable (Nano + IA)
- Despliegue y reporte de evaluación
- Meta-reflexión final

**Nivel**: Posgrado / Especialización  
**Duración estimada**: 15-20 horas  
**Prerrequisitos**: Unidades 1 a 5

[📓 Ir a la Unidad 6](unit_06_integration_project/)

---

## 🚧 Próximas Unidades (En Desarrollo)

### Unidad 7: Computación Científica Profesional
- Testing y validación
- Escalabilidad
- Deployment


---

## 🎯 Cómo Usar Este Material

### 1. Configurar Ambiente

Asegúrate de tener el ambiente `ia_nano` configurado:

```bash
# Desde el directorio raíz del repositorio
./setup.sh  # o setup.bat en Windows
conda activate ia_nano
```

### 2. Ejecutar Notebooks

```bash
# Navegar a la unidad deseada
cd educational_content/unit_01_nanoscale_modeling

# Iniciar Jupyter Lab
jupyter lab
```

### 3. Seguir el Orden Recomendado

Las unidades están diseñadas para seguirse en orden secuencial, ya que cada una construye sobre conceptos de la anterior.

---

## 📖 Filosofía Pedagógica

Cada unidad sigue el **Gold Standard** definido en [GOVERNANCE.md](../GOVERNANCE.md):

1. **Explicaciones Claras**: El "por qué" antes del "cómo"
2. **Código Documentado**: Comentarios tipo "Master Class"
3. **Matemáticas Impecables**: LaTeX para todas las ecuaciones

---

## 🤝 Contribuir

¿Encontraste un error o tienes sugerencias? Ver [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## 📊 Progreso del Curso

| Unidad | Estado | Notebook |
|--------|--------|----------|
| 1. Modelado Nanoescala | ✅ Disponible | ✅ |
| 2. Simulación Molecular | ✅ Disponible | ✅✅ (2 notebooks) |
| 3. ML Fundamentos | ✅ Disponible | ✅✅ (2 notebooks) |
| 4. IA Aplicada | ✅ Disponible | ✅✅ (2 notebooks) |
| 5. Multi-Agente | ✅ Disponible | ✅ (10 notebooks) |
| 6. Proyecto Final | ✅ Disponible | ✅ (6 notebooks) |
| 7. Computación Profesional | 🚧 En desarrollo | - |

---

## 🎓 Para Instructores

Este material puede ser usado en:
- Cursos de licenciatura en Química Computacional
- Posgrados en Nanociencia
- Talleres de IA aplicada a Ciencias
- Proyectos de investigación

**Licencia**: Apache-2.0 - Ver [LICENSE](../LICENSE)

---

<div align="center">
  <sub>Material educativo desarrollado con el Consejo de 7 Expertos 🔬</sub>
</div>
