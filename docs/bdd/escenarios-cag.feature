Feature: Integración de Context-Augmented Generation (CAG)

Scenario: Guardar contexto de usuario
Given un usuario llamado "ana"
When guarda el contexto "preferred_style" con valor "explicaciones con analogias"
Then el sistema debe almacenar el contexto correctamente

Scenario: Recuperar contexto de usuario
Given existe contexto almacenado para "ana"
When se consulta el contexto del usuario
Then el sistema debe devolver la información almacenada

Scenario: Utilizar contexto en respuestas
Given el usuario "luis" tiene el contexto "audience" igual a "explicar como principiante"
When realiza una pregunta sobre CAG
Then la respuesta debe incluir información adaptada a principiantes
And debe indicar qué contexto fue utilizado
