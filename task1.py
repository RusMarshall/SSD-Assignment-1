import io
import time
import contextlib


def decorator_1(script):
    """
    function decorator that calculates function execution time
    and the number of times the decorated function was called

    :param script: function that will be test
    :return: wrapper for this function
    """
    # define call counter
    count = 0

    def wrapper(*args):
        nonlocal count
        count += 1
        # calculate execution time and get output of the function
        time_passed, output = execution_time(script, *args)
        print(f"func {script.__name__} call for {count} executed in {time_passed} sec")

    return wrapper


def execution_time(script, *args):
    """
    Function that measures script's execution time

    :param script: function that will be test
    :param args: function arguments
    :return: tuple which consists of function's execution time and function's output
    """
    start = time.perf_counter()
    # redirect function output to the variable func_output
    with contextlib.redirect_stdout(io.StringIO()) as func_output:
        script(*args)
    end = time.perf_counter()
    return end - start, func_output
