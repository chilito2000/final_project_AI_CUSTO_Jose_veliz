"""Base placeholder for student implementation."""


class ContextStore:
    _storage = {}

    def save(self, user_id, key, value):
        if user_id not in ContextStore._storage:
            ContextStore._storage[user_id] = {}

        ContextStore._storage[user_id][key] = value
        return True

    def list_for_user(self, user_id):
        user_context = ContextStore._storage.get(user_id, {})

        return [
            {"key": key, "value": value}
            for key, value in user_context.items()
        ]