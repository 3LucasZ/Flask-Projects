import time
#current_time = time.time()
#print(current_time)

def speed_calc_decorator(function):
    def speed_calc():
        startTime = time.time()
        function()
        finishTime = time.time()
        print(function.__name__, "run speed:", finishTime - startTime, "s")
    return speed_calc

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator   
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()


