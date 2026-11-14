from functools import wraps


def my_decorator(func):
    @wraps(func)  # Makes sure that func defs and metadata remains same
    def wrapper():
        print("Before inner function runs")
        func()
        print("After inner function runs")
    return wrapper

@my_decorator # Using this directly will change the func name from greet to wrapper
def greet():
    print("Hello from decorators")

greet()
print(greet.__name__)
