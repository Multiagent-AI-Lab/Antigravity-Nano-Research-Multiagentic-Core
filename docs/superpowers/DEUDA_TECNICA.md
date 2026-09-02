# Deuda técnica registrada

## Sub-proyectos 4-6 de la separación/nivelación — pendientes, en pausa deliberada

Spec de referencia: `docs/superpowers/specs/2026-09-01-separacion-y-nivelacion-antigravity-nano.md`.

De los 6 sub-proyectos de esa spec, los **Sub-proyectos 1-3 ya están completos y publicados** en el repo hermano `AI-Agentic-Systems-Core` (repo base, infraestructura de 8 agentes + 3 componentes de soporte, y contenido pedagógico de 5 unidades U0-U4). Los **Sub-proyectos 4-6, que tocan este repo, quedan en pausa deliberada** a partir del 2026-09-02, por decisión explícita del usuario ("vamos a dejar pendiente por el momento los sub proyectos del repo antigravity nano") — no son un olvido, son trabajo identificado y diseñado que todavía no se ha ejecutado.

### Sub-proyecto 4 — Migrar/adaptar los agentes a Antigravity-Nano

- Replicar (no compartir como paquete) los 8 agentes de `src/multiagent_core/` de `AI-Agentic-Systems-Core` a este repo, adaptando `SafetyGateAgent` con la especialización química real (RDKit, `stability_guardian.py` rescatado de `external_skills/numerical/`, reemplazo del mock `toxicity_predictor.py`).
- Entregable explícito pendiente: `notebooks_extra/USO_SISTEMA_MULTIAGENTE.ipynb` (LP y Probabilidad ya lo tienen, este repo no).
- Precondición técnica ya identificada en la spec: actualizar `[tool.setuptools.packages.find]` en `pyproject.toml` de este repo (hoy solo declara `include = ["external_skills*"]`) para incluir `src*`/`multiagent_core*` **antes** de agregar código nuevo — si no, el CI actual (`pip install -e ".[dev]"` + `pytest tests/`) fallaría con `ImportError` en cualquier test que importe un agente nuevo.

### Sub-proyecto 5 — Gobernanza honesta en Antigravity-Nano

- Reescribir `GOVERNANCE.md` de este repo, reemplazando el "Consejo de 7 Expertos" ficticio (@Architect, @Scientist, @Engineer, @Safety_Gate, @Analyst, @Librarian, @QA — prosa sin código ejecutable detrás) por la documentación de los agentes reales ya migrados en el Sub-proyecto 4.
- Mismo principio ya aplicado en el `GOVERNANCE.md` de Probability-Statistics-Agentic-AI-Core en esta sesión.

### Sub-proyecto 6 — Contenido pedagógico de Antigravity-Nano nivelado

- U1 (Modelado a Nanoescala) y U2 (Simulación Molecular/DFT): se quedan tal cual, ya son nano puro.
- U3 (ML aplicado) y U4 (IA aplicada): se reescriben citando `AI-Agentic-Systems-Core` como prerequisito curricular, profundizando solo los ejemplos aplicados a nanotecnología (dataset de nanopartículas, predicción de bandgap, SEM, espectroscopía, óxidos) — los fundamentos genéricos ya migraron a U1/U2 del repo nuevo.
- U5 (Sistemas Multi-Agente): se elimina de este repo — su contenido genérico ya vive en U3 de `AI-Agentic-Systems-Core`, fusionado con los Capítulos 9/10-bis de EMALCA.
- U6 (Proyecto Integrador): se reescribe integrando explícitamente las herramientas del repo nuevo.
- Activos adicionales a actualizar en esta misma tarea (hallazgos de la revisión de la spec, 2026-09-01): `docs/units/*.md` (espejos de MkDocs Material, al menos la versión en español — las traducciones a los otros 6 idiomas quedan como deuda conocida documentada, no como olvido); y, solo al final, una vez la arquitectura real esté construida, actualizar y recién entonces evaluar someter el paper JOSS de `paper/` (confirmado con el usuario: sigue siendo borrador, nunca sometido, sin problema de integridad académica).

## Nota sobre el estado del árbol de trabajo (2026-09-02)

Al momento de escribir este registro, el árbol de trabajo de este repo tenía cambios sin commitear preexistentes (no originados en la sesión que escribió este documento): `CITATION.cff` y 3 notebooks de `educational_content/unit_05_multi_agent_sys/` (`U5_02`, `U5_05`, `U5_06`). No se tocaron ni se investigó su origen — quedan tal cual para que el usuario decida qué hacer con ellos cuando retome este repo.
