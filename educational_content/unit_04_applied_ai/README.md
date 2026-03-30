# Unidad 4: IA Aplicada a Nanotecnología y Datos Experimentales

**IA aplicada a propiedades de materiales, optimización y análisis de datos experimentales**

---

## Objetivos de Aprendizaje

Al completar esta unidad, seras capaz de:

1. Entrenar potenciales interatomicos con redes neuronales (NNP) para simulacion molecular
2. Aplicar modelos de regresion (Random Forest, GBR) para predecir propiedades de nanomateriales
3. Entender y verificar simbolicamente funciones SOAP y criterios de Lindemann con SymPy
4. Implementar Optimizacion Bayesiana y algoritmos geneticos para diseno de materiales
5. Procesar imagenes de microscopia (SEM/TEM) con vision por computadora
6. Clasificar espectros UV-Vis de nanoparticulas con Random Forest y PCA/t-SNE
7. Detectar anomalias en datos experimentales con Isolation Forest
8. Evaluar modelos con metricas cientificas apropiadas

---

## Notebooks

### Notebook 1 — IA Aplicada: Potenciales y Propiedades
**Archivo**: `UNIDAD_4_IA_APLICADA.ipynb`

Pipeline completo de IA aplicada a nanotecnologia:

**Neural Network Potentials (NNP)**
- Funciones de simetria de Behler-Parrinello (radiales y angulares)
- Verificacion simbolica con SymPy: funcion de corte y funciones radiales
- Entrenamiento con datos EMT (Effective Medium Theory) en ASE
- Evaluacion: R² de correlacion energia calculada vs predicha

**Prediccion de propiedades**
- Prediccion de bandgap con Random Forest y Gradient Boosting
- Dataset: oxidos del Materials Project (mp_api)
- Analisis comparativo de modelos (RMSE, R², MAE)

**Estabilidad termica y catálisis**
- Criterio de Lindemann para temperatura de fusion
- Efecto Gibbs-Thomson en nanoparticulas
- d-band Center Theory para prediccion de actividad catalitica

**Diseno inteligente de materiales**
- Optimizacion Bayesiana con Gaussian Process (kernel RBF/Matern)
- Expected Improvement (EI) como funcion de adquisicion, verificado simbolicamente
- Algoritmos Geneticos: seleccion, cruzamiento y mutacion
- Modelos Generativos: Variational Autoencoders (VAE) y GANs

### Notebook 2 — Datos Experimentales: Microscopia y Espectroscopia
**Archivo**: `UNIDAD_4_PARTE2_DATOS_EXPERIMENTALES.ipynb`

Analisis de datos experimentales reales con IA:

**Vision por Computadora para Microscopia**
- Procesamiento de imagenes SEM/TEM: suavizado, umbral de Otsu, Watershed
- Deteccion y segmentacion de nanoparticulas
- Extraccion de descriptores morfologicos: circularidad, solidez, excentricidad
- Criterio de Abbe para resolucion de microscopia (verificacion simbolica)
- U-Net para segmentacion semantica avanzada

**Clasificacion de Espectros UV-Vis**
- Generacion de espectros sinteticos realistas (Au, Ag, Cu, AuAg, AuCu)
- Extraccion de caracteristicas: FWHM, centroide, area, momentos espectrales
- Clasificacion con Random Forest (5 clases de nanoparticulas)
- PCA y t-SNE para visualizacion del espacio espectral
- Curva de aprendizaje y probabilidades de clasificacion

**Deteccion de Anomalias**
- Isolation Forest para detectar defectos y outliers en datos experimentales
- Visualizacion de fronteras de decision

---

## Requisitos Tecnicos

### Entorno Conda

```bash
conda activate ia_nano
```

### Dependencias Principales

| Libreria | Version | Uso |
|---|---|---|
| `scikit-learn` | >=1.3 | RF, GBR, PCA, t-SNE, Isolation Forest |
| `scikit-image` | >=0.21 | Procesamiento de imagenes (Watershed, Otsu) |
| `ase` | >=3.22 | Simulacion atomica, EMT |
| `sympy` | >=1.12 | Verificacion simbolica |
| `scipy` | >=1.11 | Signal processing, estadistica |
| `numpy` / `pandas` | latest | Manejo de datos |
| `matplotlib` / `seaborn` | latest | Visualizacion |

---

## Como Ejecutar

```bash
cd educational_content/unit_04_applied_ai

# Secuencia recomendada:
jupyter lab UNIDAD_4_IA_APLICADA.ipynb
jupyter lab UNIDAD_4_PARTE2_DATOS_EXPERIMENTALES.ipynb
```

---

## Datasets y Archivos Generados

- **`materials_project_oxides_*.csv`**: Propiedades de oxidos descargados del Materials Project
- **`spectral_features.csv`**: Caracteristicas espectrales extraidas de 750 espectros UV-Vis
- **`particle_data.csv`**: Morfologia de nanoparticulas segmentadas en SEM
- **`spectroscopy_results.txt`**: Metricas del clasificador espectral
- **`oxides_stats_*.txt`**: Estadisticas de oxidos descargados

---

## Nivel y Duracion

- **Nivel**: Licenciatura avanzada — Posgrado
- **Prerequisitos**:
  - Completar Unidades 1, 2 y 3
  - Machine Learning clasico (Random Forest, SVM, validacion cruzada)
  - Python intermedio (NumPy, Pandas, scikit-learn)
  - Nociones de microscopia y espectroscopia (recomendado)
- **Duracion estimada**:
  - Notebook 1 (IA Aplicada): 5-7 horas
  - Notebook 2 (Datos Experimentales): 4-6 horas
  - **Total**: 9-13 horas

---

## Conceptos Clave

### Neural Network Potentials
- **Funciones de simetria**: invariantes a traslacion, rotacion y permutacion de atomos
- **SOAP**: Smooth Overlap of Atomic Positions — kernel para GPR/GAP
- **Superficie de Energia Potencial (PES)**: aprendida por la red neuronal

### Optimizacion Inteligente
- **Optimizacion Bayesiana**: equilibrio exploration/exploitation via Expected Improvement
- **Algoritmos Geneticos**: seleccion natural simulada para busqueda de materiales optimos
- **VAE/GAN**: generacion de nuevas moleculas en espacio latente

### Procesamiento de Datos Experimentales
- **Watershed**: segmentacion topografica para particulas adyacentes
- **Umbral de Otsu**: maximizacion de varianza inter-clase
- **FWHM**: Full Width at Half Maximum — ancho del pico espectral
- **t-SNE**: reduccion no lineal para visualizacion de clusteres

---

## Referencias Cientificas

1. **Behler & Parrinello** (2007). "Generalized Neural-Network Representation of High-Dimensional Potential-Energy Surfaces." *PRL* 98, 146401.
2. **Bartok et al.** (2010). "Gaussian Approximation Potentials." *PRL* 104, 136403.
3. **Jain et al.** (2013). "Commentary: The Materials Project." *APL Materials* 1, 011002.
4. **Snoek et al.** (2012). "Practical Bayesian Optimization of Machine Learning Algorithms." *NeurIPS*.
5. **Holland** (1992). *Adaptation in Natural and Artificial Systems.* MIT Press.
6. **Otsu** (1979). "A Threshold Selection Method from Gray-Level Histograms." *IEEE Trans.* 9, 62-66.
7. **Ronneberger et al.** (2015). "U-Net: Convolutional Networks for Biomedical Image Segmentation." *MICCAI*.

---

## Checklist de Aprendizaje

### IA para Propiedades
- [ ] Construir y evaluar un NNP con funciones de simetria de Behler-Parrinello
- [ ] Predecir bandgap de oxidos con R² > 0.8 usando Random Forest
- [ ] Implementar y analizar la funcion Expected Improvement de Optimizacion Bayesiana
- [ ] Ejecutar un Algoritmo Genetico y visualizar la convergencia del fitness
- [ ] Describir las diferencias entre VAE y GAN para generacion de moleculas

### Datos Experimentales
- [ ] Segmentar nanoparticulas en una imagen SEM con Watershed
- [ ] Extraer y comparar descriptores morfologicos (circularidad, FWHM) por material
- [ ] Clasificar espectros UV-Vis de 5 materiales con accuracy > 90%
- [ ] Interpretar un biplot de PCA en el contexto de espectros de nanoparticulas
- [ ] Detectar anomalias en un dataset experimental con Isolation Forest

---

*Parte del curso **IA y Nanotecnologia** — Antigravity-Nano-Research-Multiagentic-Core*
