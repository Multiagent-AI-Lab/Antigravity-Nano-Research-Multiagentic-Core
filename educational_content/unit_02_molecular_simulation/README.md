# Unidad 2: Simulación Molecular Avanzada

**Dinámica Molecular, DFT y Nanofabricación Computacional**

---

## 🎯 Objetivos de Aprendizaje

Al completar esta unidad, serás capaz de:

1. ✅ Comprender los fundamentos de Dinámica Molecular (MD)
2. ✅ Implementar simulaciones MD con diferentes potenciales interatómicos
3. ✅ Aplicar Teoría del Funcional de la Densidad (DFT) para cálculos electrónicos
4. ✅ Analizar propiedades termodinámicas y estructurales de nanomateriales
5. ✅ Diseñar nanoestructuras mediante síntesis computacional
6. ✅ Validar resultados contra datos experimentales

---

## 📋 Contenido

Esta unidad se divide en **dos partes complementarias**:

### Parte 1: Simulación Molecular (MD)
**Notebook**: `UNIDAD_2_SIMULACION_MOLECULAR.ipynb`

**Contenido**:
- Fundamentos de Dinámica Molecular
- Potenciales interatómicos (Lennard-Jones, EAM, Tersoff)
- Integración temporal (Verlet, Velocity Verlet)
- Ensembles termodinámicos (NVE, NVT, NPT)
- Análisis de trayectorias
- Propiedades de transporte

### Parte 2: DFT y Nanofabricación
**Notebook**: `UNIDAD_2_PARTE2_DFT_NANOFABRICACION.ipynb`

**Contenido**:
- Teoría del Funcional de la Densidad (DFT)
- Bases Gaussianas vs. planas
- Pseudopotenciales
- Optimización de estructuras con DFT
- Cálculo de propiedades electrónicas
- Diseño de nanoestructuras

---

## 🛠️ Requisitos Técnicos

### Ambiente Conda

Ambas partes requieren el ambiente `ia_nano`:

```bash
conda activate ia_nano
```

### Dependencias Principales

**Para Parte 1 (MD)**:
- **ASE** - Atomic Simulation Environment
- **NumPy** - Cálculos numéricos
- **Matplotlib** - Visualización
- **SciPy** - Integración numérica

**Para Parte 2 (DFT)**:
- **ASE** + módulo calculador DFT
- **GPAW** o **PySCF** - Código DFT (opcional, para cálculos reales)
- **NGLView** - Visualización 3D

---

## 🚀 Cómo Ejecutar

### Ejecutar en Orden Secuencial

Las dos partes están diseñadas para cursarse en orden:

```bash
cd educational_content/unit_02_molecular_simulation

# Parte 1: Fundamentos de MD
jupyter lab UNIDAD_2_SIMULACION_MOLECULAR.ipynb

# Parte 2: DFT y Nanofabricación
jupyter lab UNIDAD_2_PARTE2_DFT_NANOFABRICACION.ipynb
```

---

## 📊 Datos y Archivos Generados

Durante la ejecución se generarán:

**Parte 1 (MD)**:
- `*.traj` - Trayectorias de simulación MD
- `energia_vs_tiempo.png` - Gráficos de conservación de energía
- `temperatura_vs_tiempo.png` - Control termodinámico
- `rdf_*.png` - Funciones de distribución radial

**Parte 2 (DFT)**:
- `*.gpw` - Archivos de checkpoint DFT (si usa GPAW)
- `estructura_optimizada.xyz` - Geometrías optimizadas
- `densidad_electronica.png` - Mapas de densidad
- `bandas_electronicas.png` - Estructura de bandas

Todos los archivos se guardan en `assets/`.

---

## 🎓 Nivel y Duración

- **Nivel**: Licenciatura avanzada - Posgrado
- **Prerrequisitos**: 
  - Completar Unidad 1 (Modelado a Nanoescala)
  - Mecánica cuántica básica (para Parte 2)
  - Termodinámica estadística (recomendado)
- **Duración estimada**: 
  - Parte 1: 3-4 horas
  - Parte 2: 4-5 horas
  - **Total**: 7-9 horas

---

## 🧪 Conceptos Clave

### Dinámica Molecular (Parte 1)

- **MD**: Simulación de movimiento atómico mediante integración de ecuaciones de Newton
- **Potencial Lennard-Jones**: Modelo simple de interacciones van der Waals
- **EAM (Embedded Atom Method)**: Potencial para metales considerando densidad electrónica
- **Verlet**: Algoritmo de integración temporal conservativo
- **Ensemble NVT**: Número de partículas, volumen y temperatura constantes
- **RDF**: Función de distribución radial para análisis estructural

### DFT y Nanofabricación (Parte 2)

- **DFT**: Método ab initio para calcular estructura electrónica
- **Funcional de intercambio-correlación**: Aproximación LDA, GGA, híbridos
- **Bases Gaussianas**: Funciones centradas en átomos (ej: 6-31G*)
- **Pseudopotenciales**: Reemplazo de electrones internos para reducir costo computacional
- **Optimización geométrica**: Minimización de energía total
- **Gap de banda**: Diferencia HOMO-LUMO, determina propiedades electrónicas

---

## 📚 Referencias Científicas

### Dinámica Molecular

1. **Frenkel & Smit** (2001). "Understanding Molecular Simulation." Academic Press.
2. **Allen & Tildesley** (2017). "Computer Simulation of Liquids." Oxford University Press.
3. **Rapaport** (2004). "The Art of Molecular Dynamics Simulation." Cambridge University Press.

### DFT

1. **Parr & Yang** (1989). "Density-Functional Theory of Atoms and Molecules." Oxford.
2. **Martin** (2004). "Electronic Structure: Basic Theory and Practical Methods." Cambridge.
3. **Koch & Holthausen** (2001). "A Chemist's Guide to Density Functional Theory." Wiley-VCH.

### Nanomateriales

1. **Baletto & Ferrando** (2005). "Structural properties of nanoclusters." *Rev. Mod. Phys.* 77, 371.
2. **Bansmann et al.** (2005). "Magnetic and structural properties of isolated clusters." *Surf. Sci. Rep.* 56, 189.

---

## ✅ Checklist de Aprendizaje

Después de completar esta unidad, deberías poder:

### Parte 1: MD
- [ ] Explicar cómo funciona un algoritmo de integración MD
- [ ] Seleccionar el potencial interatómico apropiado
- [ ] Configurar y ejecutar simulaciones en diferentes ensembles
- [ ] Analizar conservación de energía y temperatura
- [ ] Calcular RDF y número de coordinación
- [ ] Interpretar propiedades termodinámicas

### Parte 2: DFT
- [ ] Comprender los fundamentos de DFT
- [ ] Seleccionar bases y funcionales apropiados
- [ ] Optimizar geometrías con DFT
- [ ] Calcular propiedades electrónicas (gap, HOMO, LUMO)
- [ ] Visualizar densidades electrónicas
- [ ] Diseñar nanoestructuras con propiedades específicas

---

## 🔄 Conexión con Otras Unidades

**De Unidad 1**: Conceptos de ASE, visualización, análisis estructural

**Hacia Unidad 3**: Los descriptores estructurales calculados aquí se usarán como features para ML

**Hacia Unidad 4**: Validación de simulaciones MD/DFT contra datos experimentales

---

## 🐛 Troubleshooting

### Simulaciones MD muy lentas

```python
# Reducir número de átomos o timesteps
from ase.build import bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
# En lugar de (10,10,10), usar (5,5,5)
atoms = atoms.repeat((5,5,5))  # 500 átomos en vez de 4000
```

### Error: "GPAW not installed"

DFT requiere código especializado. Si no tienes GPAW:

```bash
# Opción 1: Instalar GPAW (puede ser complicado)
conda install -c conda-forge gpaw

# Opción 2: Usar EMT (potencial empírico) para práctica
from ase.calculators.emt import EMT
atoms.calc = EMT()
```

### Visualización 3D no funciona

```bash
# Asegurar que nglview esté habilitado
jupyter nbextension enable --py --sys-prefix nglview
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

Ver [INSTALL.md](../../INSTALL.md) para más soluciones.

---

## 🤝 Contribuir

¿Encontraste un error o tienes mejoras para esta unidad?

1. Abre un [Issue](https://github.com/ljyudico/Antigravity-Nano-Research-Multiagentic-Core/issues)
2. Usa el template "Bug Report" o "Feature Request"
3. Etiqueta con `unit-2` y `educational-content`

---

<div align="center">
  <sub>Simulaciones de primer nivel para investigación en nanomateriales 🔬⚛️</sub>
</div>
