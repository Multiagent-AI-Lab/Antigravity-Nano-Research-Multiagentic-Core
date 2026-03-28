# Unidad 3: Machine Learning y Redes Neuronales para Nanomateriales

**Fundamentos de ML y Deep Learning aplicados a Nanociencia — PyTorch**

---

## Objetivos de Aprendizaje

Al completar esta unidad, seras capaz de:

1. Comprender los fundamentos matematicos del Machine Learning y las redes neuronales
2. Aplicar algoritmos clasicos de ML (SVM, Random Forest, Gradient Boosting) a datos de nanomateriales
3. Disenar y entrenar redes neuronales profundas en **PyTorch** para prediccion de propiedades
4. Implementar retropropagacion simbolica con **SymPy** y entender el gradiente a fondo
5. Usar redes de grafos (GCN) para representar moleculas y cristales
6. Aplicar Transfer Learning (MobileNetV2) y Knowledge Distillation
7. Entrenar un agente de Reinforcement Learning (DQN) con gymnasium
8. Evaluar y validar modelos con metricas cientificas apropiadas

---

## Notebooks

### Notebook 1 — ML Clasico (Fundamentos)
**Archivo**: `UNIDAD_3_ML_FUNDAMENTOS.ipynb`

Pipeline completo de ML clasico aplicado a nanomateriales:
- Regresion lineal/logistica con interpretacion fisica
- Arboles de decision, Random Forest y Gradient Boosting
- Support Vector Machines para propiedades de materiales
- Feature engineering: descriptores moleculares y cristalograficos
- Validacion cruzada y metricas (RMSE, R², MAE, F1)
- Dataset: `nanomaterials_full_dataset.csv`

### Notebook 2 — Algoritmos Clasicos Avanzados
**Archivo**: `UNIDAD_3_ML_FUNDAMENTOS_algoritmos_clasicos.ipynb`

Profundizacion con analisis comparativo:
- Comparativa sistematica de modelos (KNN, SVM, RF, GradBoost)
- Seleccion de caracteristicas y reduccion de dimensionalidad (PCA, UMAP)
- Ensambles heterogeneos y stacking
- Interpretabilidad sin caja negra

### Notebook 3 — Redes Neuronales: Fundamentos (Parte I)
**Archivo**: `UNIDAD_3_REDES_NEURONALES_FUNDAMENTOS.ipynb` — 118 celdas

Notebook principal de Deep Learning de la unidad:

**Fundamentos matematicos**
- Retropropagacion simbolica con SymPy (calculo del gradiente paso a paso)
- Funciones de activacion: ReLU, Sigmoid, Tanh, Leaky ReLU
- Regularizacion: Dropout visualizado numericamente

**Arquitecturas y entrenamiento**
- MLP en PyTorch: prediccion de bandgap de oxidos (R²~0.9998)
- CNN para clasificacion de nanoparticulas por TEM
- Modelos de difusion (DDPM): generacion de distribuciones de nanoparticulas

**Tecnicas avanzadas**
- Transfer Learning con MobileNetV2 (feature extraction + fine-tuning)
- Knowledge Distillation: comprimir modelos grandes en modelos eficientes
- Reinforcement Learning: DQN en CartPole con gymnasium

### Notebook 4 — Redes Neuronales: Avanzado (Parte II)
**Archivo**: `UNIDAD_3_PARTE2_REDES_NEURONALES.ipynb` — 33 celdas

Temas de frontera:
- Retropropagacion simbolica extendida (SymPy + PyTorch comparacion)
- MLP v1/v2 con sklearn (curvas de convergencia)
- Redes de grafos convolucionales (GCN) con PyTorch Geometric para moleculas
- Transfer Learning avanzado con MobileNetV2

---

## Requisitos Tecnicos

### Entorno Conda

```bash
conda activate ia_nano
```

### Dependencias Principales

| Libreria | Version | Uso |
|---|---|---|
| `torch` | >=2.0 | Framework principal Deep Learning |
| `torchvision` | >=0.15 | CNN, Transfer Learning |
| `torch-geometric` | >=2.3 | Redes de grafos (GCN) |
| `gymnasium` | >=0.29.0 | Reinforcement Learning (DQN) |
| `scikit-learn` | >=1.3 | ML clasico, MLP baseline |
| `sympy` | >=1.12 | Algebra simbolica, retropropagacion |
| `numpy` / `pandas` | latest | Manejo de datos |
| `matplotlib` / `seaborn` | latest | Visualizacion |

> **Nota**: Este modulo usa **exclusivamente PyTorch**. No se requiere TensorFlow.

### Instalacion de gymnasium (si no esta instalado)

```bash
pip install "gymnasium>=0.29.0"
```

---

## Como Ejecutar

```bash
cd educational_content/unit_03_ml_nanomaterials

# Secuencia recomendada:
jupyter lab UNIDAD_3_ML_FUNDAMENTOS.ipynb
jupyter lab UNIDAD_3_ML_FUNDAMENTOS_algoritmos_clasicos.ipynb
jupyter lab UNIDAD_3_REDES_NEURONALES_FUNDAMENTOS.ipynb
jupyter lab UNIDAD_3_PARTE2_REDES_NEURONALES.ipynb
```

---

## Dataset

- **`nanomaterials_full_dataset.csv`**: Dataset principal con propiedades de nanomateriales
  (tamanio, geometria, composicion, punto de fusion, bandgap, energia de cohesion).
  Generado sinteticamente con distribuciones fisicamente realistas.

---

## Nivel y Duracion

- **Nivel**: Licenciatura avanzada — Posgrado
- **Prerequisitos**:
  - Completar Unidades 1 y 2
  - Algebra lineal (vectores, matrices, valores propios)
  - Calculo diferencial (gradientes, regla de la cadena)
  - Python intermedio (NumPy, Pandas, orientado a objetos)
- **Duracion estimada**:
  - Notebook 1 (ML Clasico): 3-4 horas
  - Notebook 2 (Algoritmos): 2-3 horas
  - Notebook 3 (Fundamentos DL): 5-6 horas
  - Notebook 4 (Avanzado DL): 3-4 horas
  - **Total**: 13-17 horas

---

## Conceptos Clave

### ML Clasico
- **Feature engineering**: descriptores moleculares (fingerprints, Coulomb matrix)
- **Bias-Variance tradeoff**: underfitting vs overfitting
- **Cross-validation**: evaluacion robusta con datos experimentales limitados

### Deep Learning (PyTorch)
- **Retropropagacion**: derivacion simbolica + implementacion en autograd
- **Funciones de activacion**: ReLU, Sigmoid, Tanh y su impacto en el gradiente
- **Dropout**: regularizacion estocastica con visualizacion de mascaras
- **GCN**: representacion natural de moleculas y cristales como grafos
- **Transfer Learning**: reutilizar MobileNetV2 en imagenes de microscopia
- **Knowledge Distillation**: comprimir modelos manteniendo el rendimiento
- **DQN / RL**: aprendizaje por refuerzo para optimizacion de sintesis

---

## Referencias Cientificas

1. **Goodfellow, Bengio & Courville** (2016). *Deep Learning.* MIT Press.
2. **Geron** (2022). *Hands-On Machine Learning.* O'Reilly, 3a ed.
3. **Kipf & Welling** (2017). "Semi-Supervised Classification with Graph Convolutional Networks." *ICLR*.
4. **Schutt et al.** (2017). "SchNet: A continuous-filter convolutional neural network." *NeurIPS*.
5. **Ho et al.** (2020). "Denoising Diffusion Probabilistic Models." *NeurIPS*.
6. **Hinton et al.** (2015). "Distilling the Knowledge in a Neural Network." *NIPS Workshop*.
7. **Mnih et al.** (2015). "Human-level control through deep reinforcement learning." *Nature* 518, 529-533.

---

## Checklist de Aprendizaje

### ML Clasico
- [ ] Distinguir tipos de aprendizaje y elegir el algoritmo apropiado
- [ ] Calcular e interpretar RMSE, R², MAE, F1-score en contexto de materiales
- [ ] Construir un pipeline completo: datos -> features -> modelo -> validacion
- [ ] Comparar Random Forest vs GradientBoosting en datasets de nanomateriales
- [ ] Aplicar PCA/UMAP para exploracion del espacio de caracteristicas

### Deep Learning
- [ ] Derivar retropropagacion manualmente con SymPy para una red de 2 capas
- [ ] Implementar una red MLP en PyTorch con nn.Module
- [ ] Entrenar una CNN para clasificacion de imagenes de TEM
- [ ] Aplicar Transfer Learning (feature extraction vs fine-tuning)
- [ ] Construir un grafo molecular y aplicar GCN
- [ ] Implementar Knowledge Distillation (temperatura softmax)
- [ ] Entrenar un agente DQN y visualizar la curva de recompensa

---

*Parte del curso **IA y Nanotecnologia** — Antigravity-Nano-Research-Multiagentic-Core*
