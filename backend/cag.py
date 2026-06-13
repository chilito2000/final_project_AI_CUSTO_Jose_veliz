"""Base placeholder for student implementation."""

def apply_context(user_id, question, base_answer, context_items):
    if not context_items:
        return base_answer, []

    context_used = []
    context_text = []

    for item in context_items:
        key = item.get("key")
        value = item.get("value")

        if key and value:
            context_used.append(key)
            context_text.append(f"{key}: {value}")

    if not context_text:
        return base_answer, []

    enhanced_answer = (
        f"{base_answer} "
        f"Contexto del usuario aplicado: {'; '.join(context_text)}."
    )

    return enhanced_answer, context_used