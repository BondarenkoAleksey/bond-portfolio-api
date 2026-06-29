import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Выполнение {func.__name__} заняло {end_time - start_time:.4f} секунд")
        return result
    return wrapper
