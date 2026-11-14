from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[Logger] Starting function...")
        result = func(*args, **kwargs)
        print("[Logger] Stopping function...")
        return result
    return wrapper

@log_activity
def hash_smthng(token, alg):
    print(f"Lets hash '{token}' with algorithm {alg}")

hash_smthng("hi","SHA256")
