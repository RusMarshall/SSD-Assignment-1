import contextlib
# import functions from previous tasks to avoid repeating the code
from task1 import execution_time
from task2 import print_function_info


class decorator_3:
    """
    Class that calculates function execution time
    and the number of times the decorated function was called
    """

    # constructor of the class
    def __init__(self, func):
        # define call counter
        self.call = 0
        self.func = func
        # define list of the time executions
        self.time_execution_list = dict()

    # method that is called by the constructor
    def __call__(self, *args, **kwargs):
        # increase counter
        self.call += 1
        # calculate execution time and get output of the function
        time_passed, func_output = execution_time(self.func, *args)
        self.time_execution_list[self.func.__name__] = time_passed
        # open .txt file for functions output information
        with open(f"src/{self.__class__.__name__}.txt", "a") as file:
            with contextlib.redirect_stdout(file):
                print(f"func {self.func.__name__} call for {self.call} "
                      f"executed in {self.time_execution_list[self.func.__name__]} sec")
                print_function_info(self.func, func_output, args, kwargs)

    def change_function(self, new_func):
        """
        Function that change test function
        :param new_func: new function which will be tested
        """
        self.call = 0
        self.func = new_func

    def print_rank_table(self):
        """
        Function which prints rank table
        """
        print("{:_^80}".format(" Rank Table "))
        # sort the dictionary
        self.time_execution_list = sorted(self.time_execution_list.items(), key= lambda x:x[1])
        print("{:_^30s} {:_^5s} {:_^10s} {:_^5s} {:_^26s}".format("PROGRAM", "|", "RANK", "|", "TIME ELAPSED"))
        rank = 0
        for key, value in self.time_execution_list:
            rank += 1
            print("{:30s} {:^5s} {:^10s} {:^5s} {:^20}".format(key, "|", str(rank), "|", value))
        print(80 * '-' + '\n')
