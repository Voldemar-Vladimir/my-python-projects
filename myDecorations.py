import time
from functools import wraps
from datetime import datetime

call_count = {"log":0, "save_call":0, "timer":0, "counter":0}

class oldEX(Exception):
    pass
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("calls.log", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] {func.__name__}{args} = {result}\n")
        return result
    return wrapper
def safe_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open("errors.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] {func.__name__}: {e}\n")
            return None
    return wrapper
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнялась {end - start:.4f} сек")
        return result
    return wrapper
def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        call_count[func.__name__] = call_count.get(func.__name__, 0) + 1
        return func(*args, **kwargs)
    return wrapper
@safe_call       
@log           
@timer            
@counter
def club(age):
    if age>=18:
        print("Можно")
    else:
        print("Нельзя")