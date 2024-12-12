#measuring the time_taken by the function to execute
import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


def speed_calc_decorator(function):
    def wrapper_function():
        time_before = time.time()
        function()
        time_after = time.time()
        time_taken = time_after - time_before
        print(time_taken)

    return wrapper_function   # this calls wrapper_function and is returned


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()