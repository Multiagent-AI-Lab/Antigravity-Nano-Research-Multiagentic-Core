# Unidad 3: Machine Learning para Nanomateriales

**Fundamentos de ML y Redes Neuronales aplicadas a Nanociencia**

---

## 🎯 Objetivos de Aprendizaje

Al completar esta unidad, serás capaz de:

1. ✅ Comprender los fundamentos matemáticos del Machine Learning
2. ✅ Aplicar algoritmos clásicos de ML a datos de nanomateriales
3. ✅ Diseñar y entrenar redes neuronales para predicción de propiedades
4. ✅ Preprocesar datos experimentales y de simulación para ML
5. ✅ Evaluar y validar modelos con métricas científicas apropiadas
6. ✅ Interpretar modelos desde una perspectiva química y física

---

## 📋 Contenido

Esta unidad se divide en **dos partes complementarias**:

### Parte 1: Fundamentos de Machine Learning
**Notebook**: `UNIDAD_3_ML_FUNDAMENTOS.ipynb`

**Contenido**:
- Introducción al aprendizaje automático: supervisado, no supervisado, por refuerzo
- Regresión lineal y logística con interpretación física
- Árboles de decisión y Random Forest para clasificación de materiales
- Support Vector Machines (SVM) para propiedades de nanomateriales
- Feature engineering: descriptores moleculares y cristalográficos
- Validación cruzada y métricas de evaluación científica

### Parte 2: Redes Neuronales
**Notebook**: `UNIDAD_3_PARTE2_REDES_NEURONALES.ipynb`

**Contenido**:
- Fundamentos matemáticos: perceptrón, retropropagación, funciones de activación
- Arquitecturas profundas (DNN) para predicción de propiedades
- Redes neuronales de grafos (GNN) para moléculas y cristales
- Redes convolucionales (CNN) para imágenes de microscopía
- Transferencia de aprendizaje en aplicaciones nanoscientíficas
- Interpretabilidad: SHAP values, mapas de atención

---

## 🛠️ Requisitos Técnicos

### Ambiente Conda

```bash
conda activate ia_nano
```

### Dependencias Principales

**Para Parte 1 (ML Clásico)**:
- **Scikit-learn** - Algoritmos de ML
- **NumPy**, **Pandas** - Manejo de datos
- **Matplotlib**, **Seaborn** - Visualización
- **Matminer** - Descriptores de materiales

**Para Parte 2 (Redes Neuronales)**:
- **TensorFlow** o **PyTorch** - Frameworks de Deep Learning
- **PyTorch Geometric** - GNN para moléculas (opcional)
- **SHAP** - Interpretabilidad de modelos

---

## 🚀 Cómo Ejecutar

```bash
cd educational_content/unit_03_ml_nanomaterials

# Parte 1: ML Fundamentos
jupyter lab UNIDAD_3_ML_FUNDAMENTOS.ipynb

# Parte 2: Redes Neuronales
jupyter lab UNIDAD_3_PARTE2_REDES_NEURONALES.ipynb
```

---

## 🎓 Nivel y Duración

- **Nivel**: Licenciatura avanzada - Posgrado
- **Prerrequisitos**:
  - Completar Unidades 1 y 2
  - Álgebra lineal básica
  - Cálculo diferencial (para gradientes)
  - Python intermedio (NumPy, Pandas)
- **Duración estimada**:
  - Parte 1: 4-5 horas
  - Parte 2: 5-6 horas
  - **Total**: 9-11 horas

---

## 🧪 Conceptos Clave

### ML Clásico (Parte 1)

- **Supervisado**: Aprender mapeo input→output con datos etiquetados
- **Feature engineering**: Descriptores moleculares (fingerprints, Coulomb matrix)
- **Bias-Variance tradeoff**: Balance entre underfitting y overfitting
- **Cross-validation**: Evaluación robusta con datos limitados
- **Random Forest**: Ensemble de árboles, robusto y explicable

### Redes Neuronales (Parte 2)

- **Retropropagación**: Algoritmo para ajuste de pesos por gradiente
- **Función de activación**: ReLU, Sigmoid, Tanh y su impacto físico
- **Dropout**: Regularización para evitar sobreajuste
- **GNN (Graph Neural Networks)**: Representación natural de moléculas como grafos
- **Transfer learning**: Reutilizar modelos preentrenados en nuevos dominios

---

## 📚 Referencias Científicas

1. **Goodfellow, Bengio & Courville** (2016). "Deep Learning." MIT Press.
2. **Géron** (2022). "Hands-On Machine Learning." O'Reilly.
3. **Duvenaud et al.** (2015). "Convolutional Networks on Graphs for Learning Molecular Fingerprints." *NeurIPS*.
4. **Schütt et al.** (2017). "SchNet: A continuous-filter convolutional neural network for modeling quantum interactions." *NeurIPS*.
5. **Brockherde et al.** (2017). "Bypassing the Kohn-Sham equations with machine learning." *Nature Comm.* 8, 872.

---

## ✅ Checklist de Aprendizaje

### Parte 1: ML Clásico
- [ ] Distinguir tipos de aprendizaje automático y cuándo usar cada uno
- [ ] Calcular y interpretar métricas (RMSE, R², MAE, F1)
- [ ] Construir pipeline completo: datos → features → modelo → validación
- [ ] Aplicar Random Forest a predicción de propiedades
- [ ] Generar e interpretar descriptores moleculares

### Parte 2: Redes Neuronales
- [ ] Diseñar arquitecturas DNN apropiadas al problema
- [ ] Entrenar redes con optimización por gradiente descendente
- [ ] Aplicar técnicas de regularización (Dropout, L2)
- [ ] Implementar una GNN simple para moléculas
- [ ] Interpretar predicciones con SHAP values

---

## 🔄 Conexión con Otras Unidades

**De Unidad 2**: Los descriptores estructurales (RDF, número de coordinación) se usan como features de entrada para los modelos de ML

**Hacia Unidad 4**: Los modelos entrenados aquí se integran con datos experimentales reales

---

## 🐛 Troubleshooting

### Error: "No module named 'torch'"

```bash
conda activate ia_nano
conda install pytorch torchvision -c pytorch
```

### Error: "No module named 'matminer'"

```bash
pip install matminer
```

### Memoria insuficiente al entrenar

```python
# Reducir batch_size
trainer = Trainer(batch_size=16)  # en vez de 64

# O reducir el dataset inicial
X_train_small = X_train[:1000]
```

Ver [INSTALL.md](../../INSTALL.md) para más soluciones.

---

## 🤝 Contribuir

1. Abre un [Issue](https://github.com/ljyudico/Antigravity-Nano-Research-Multiagentic-Core/issues)
2. Etiqueta con `unit-3` y `educational-content`

---

<div align="center">
  <sub>Machine Learning aplicado a la frontera de la investigación en nanomateriales 🤖🔬</sub>
</div>
