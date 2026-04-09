# secure_system

current_user = {"username": "jhonnu", "role": "user"}

def require_admin(func):
    def wrapper(*args, **kwargs):
        if current_user.get("role") != "admin":
            return "ACCESS_DENIED" # Yetki yoksa bunu dön
        return func(*args, **kwargs)
    return wrapper

@require_admin
def delete_database_record(record_id):
    return f"RECORD_{record_id}_DELETED" # Yetki varsa asıl işlemi dön