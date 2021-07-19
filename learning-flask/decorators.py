import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

#Method 1:

@delay_decorator
def say_hello():
    print("Hello")

say_hello()

#Method 2:

def say_bye():
    print("Bye")

delay_bye = delay_decorator(say_bye)
delay_bye()