# Integración de Context-Augmented Generation (CAG)

## Examen Final - Inteligencia Artificial

**Universidad Mariano Gálvez de Guatemala**
**Carrera:** Ingeniería en Sistemas de Información
**Curso:** Inteligencia Artificial
**Estudiante:** Josué Ricardo Enamorado Parham

---

# Descripción del Proyecto

El proyecto base proporcionaba una implementación de Retrieval-Augmented Generation (RAG) utilizando una base documental pequeña para responder preguntas relacionadas con el curso.

Como parte del examen final se desarrolló una integración de Context-Augmented Generation (CAG), permitiendo almacenar contexto por usuario y utilizar dicho contexto en respuestas posteriores.

La solución implementada permite:

* Guardar contexto personalizado por usuario.
* Recuperar contexto almacenado.
* Utilizar contexto previo para enriquecer respuestas.
* Mantener compatibilidad con el sistema RAG original.
* Validar funcionalidad mediante pruebas automatizadas.

---

# Arquitectura

## Componentes Principales

### Backend

* `server.py`

  * Expone los endpoints REST.
  * Gestiona solicitudes de contexto y preguntas.

* `assistant.py`

  * Genera respuestas.
  * Integra RAG y CAG.

* `knowledge.py`

  * Recuperación documental (RAG).

* `context_store.py`

  * Almacenamiento de contexto por usuario.

* `cag.py`

  * Aplicación del contexto a las respuestas.

### Frontend

Interfaz web para interactuar con el asistente.

### Data

Base de conocimiento utilizada por RAG.

---

# Funcionalidades Implementadas

## Almacenamiento de Contexto

Permite registrar información asociada a un usuario.

Ejemplo:

```json
{
  "user_id": "ana",
  "key": "preferred_style",
  "value": "explicaciones con analogias"
}
```

## Recuperación de Contexto

Permite consultar el contexto previamente almacenado.

## Uso de Contexto en Respuestas

Las respuestas generadas consideran información almacenada previamente para el usuario.

---

# Metodología Scrum

## Sprint 1

### Objetivo

Implementar almacenamiento y recuperación de contexto.

### Actividades

* Configuración del entorno.
* Ejecución de pruebas base.
* Análisis de arquitectura.
* Implementación de ContextStore.

### Resultado

Contexto almacenado y recuperado correctamente.

---

## Sprint 2

### Objetivo

Integrar contexto dentro del flujo de respuestas.

### Actividades

* Implementación de cag.py.
* Modificación de assistant.py.
* Ejecución de validaciones.
* Documentación final.

### Resultado

Las respuestas utilizan contexto previamente almacenado.

---

# BDD

Los escenarios BDD se encuentran en:

```text
docs/bdd/escenarios-cag.feature
```

Incluyen:

* Guardar contexto.
* Recuperar contexto.
* Utilizar contexto en respuestas.

---

# TDD

La estrategia TDD utilizada se encuentra en:

```text
docs/tdd/plan-tdd.md
```

Proceso aplicado:

1. Ejecutar pruebas iniciales.
2. Analizar fallos.
3. Implementar funcionalidades.
4. Ejecutar validación final.

Resultado:

```text
6 passed
```

---




---

# Uso de Inteligencia Artificial

La IA fue utilizada como herramienta de apoyo para:

* Interpretación de requisitos.
* Diseño de solución.
* Análisis de arquitectura.
* Validación de implementación.

Todas las decisiones finales, modificaciones y verificaciones fueron realizadas manualmente por el estudiante.

---

# Ejecución del Proyecto

## Instalar dependencias

```bash
pip install pytest
```

## Ejecutar backend

```bash
PYTHONPATH=. python -m backend.server
```

## Ejecutar pruebas

```bash
pytest
```

---

# Resultado Final

Validación completada exitosamente:

```text
6 passed
```

La implementación cumple con los requisitos establecidos para la integración de Context-Augmented Generation (CAG).
