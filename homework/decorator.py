def log_function_call(fn):
    def wrapper(*args):
        fn(*args)
        print(f"Вызвана функция {fn.__name__} c аргументами {args}")

    return wrapper
@log_function_call
def add(a, b):
    return a + b

result = add(3, 5)