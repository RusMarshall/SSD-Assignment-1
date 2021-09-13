import inspect
# import additional function from the previous task to avoid repeating the code
from task1 import execution_time


def decorator_2(script):
    """
    Function decorator that calculates function execution time
        and the number of times the decorated function was called
    Also, it dumps information of the function to the console

    :param script: function that will be test
    :return: wrapper for this function
    """

    # define call counter
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        # calculate execution time and get output of the function
        time_passed, func_output = execution_time(script, *args)
        print(f"func {script.__name__} call for {count} executed in {time_passed} sec")
        # print information about function to the console
        print_function_info(script, func_output, args, kwargs)
    return wrapper


def print_function_info(script, func_output, args, kwargs):
    """
    Additional function that prints information about passed script
    information consists of:
        Name,
        Type,
        Sign,
        Args,
        Docstring,
        Source,
        Output

    :param script: function, information about which will be print
    :param func_output: redirected output of the test function
    :param args: positional arguments of the test function
    :param kwargs: key arguments of the test function
    :return: None
    """

    # create a dictionary from function members
    function_info = dict(inspect.getmembers(script))
    # get functions signature
    function_signature = inspect.signature(script)
    # get docstring of the function and split it
    doc_splited_lines = inspect.getdoc(script).split('\n')
    # create lambda-function to print the doc
    print_Doc_lines = lambda doc_splited_line: [print("{:<10s} {:<20s}".format("", line.lstrip())) for line in
                                                doc_splited_line]
    # create lambda-function to print the source
    source_code = inspect.getsourcelines(script)[0]
    source_code_print = lambda doc_splited_line: [print("{:<10s} {:<20s}".format("", line.replace("\n", "").lstrip()))
                                                  for line in doc_splited_line]
    # create lambda-function to print the output
    output = func_output.getvalue().split('\n')
    print_output = lambda line_output: [print("{:<10s} {:<20s}".format("", line.lstrip())) for line in line_output]

    print("{:<10s} {:<20s}".format("Name:", function_info['__name__']))
    print("{:<10s} {:<20s}".format("Type:", str(function_info['__class__'])))
    print("{:<10s} {:<20s}".format("Sign:", str(function_signature)))
    print("{:<10s} {:<20s}".format("Args:", "positional" + str(args)))
    print("{:<10s} {:<20s}".format("", "keyworded" + str(kwargs)))
    print('{:<10s}'.format("Doc"), end="")
    print_Doc_lines(doc_splited_lines)
    print(f"Source: ", end="")
    source_code_print(source_code)
    print(f"Output: ", end="")
    print_output(output)