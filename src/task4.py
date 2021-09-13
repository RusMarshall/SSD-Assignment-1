import datetime
import contextlib
# import functions from previous tasks to avoid repeating the code
from task3 import decorator_3


# decorator_4 has single inheritance to simplify code
class decorator_4(decorator_3):
    """
    Class that decorates function. It measures functions execution time,
    count of calls and dumb it to the .txt file. If errors are exist in function call,
    then method dumbs information with timestamp to the log file
    """
    # class constructor
    def __int__(self, func):
        # call parents constructor
        decorator_3.__init__(self, func)

    # method that is called by the constructor
    def __call__(self, *args, **kwargs):
        # we try to call parents 'call' method, but if errors are exist in functions parameters
        # function dump it to log file
        try:
            decorator_3.__call__(self, *args, **kwargs)
        except Exception as error:
            with open(f"{self.__class__.__name__}_log.txt", "a") as f:
                with contextlib.redirect_stdout(f):
                    print(datetime.datetime.now())
                    print(f"{self.func.__name__}: " + str(error), end="\n\n")
            # set execution time very high (infinity)
            self.time_execution_list[self.func.__name__] = float("inf")

