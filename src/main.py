import math
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4


def Pascal_Triangle(n = 5):
    """
    Function that prints in console
    n lines of Pascals triangle

    Keyword arguments:
    :param n: number of printable lines (default 5)
    """

    top = [1]
    append_val = [0]
    for _ in range(n):
        print(top)
        top = [l+r for l, r in zip(top+append_val, append_val + top)]


def Quadratic_equation_solver(a=1, b=1, c=1):
    """
    Function that solves simple quadratic equation
    and prints the result as list in console:

    ax^2+b*x+c=0

    Keyword arguments:
    :param a: The first coefficient (default 1)
    :param b: The second coefficient (default 1)
    :param c: Free coefficient (default 1)
    :return:  None if param equals to 0
    """
    if a == 0:
        print("'a' value mustn't equals to 0!")
        return None

    discriminant = b ** 2 - 4 * a * c
    answers = list()

    if discriminant < 0:
        print("There are no real roots")
    elif discriminant == 0:
        answers.append(-b / 2 * a)
        print(answers)
    else:
        answers.append((-b + math.sqrt(discriminant)) / 2 * a)
        answers.append((-b - math.sqrt(discriminant)) / 2 * a)
        print(answers)


def Arithmetic_sequence(a0=0, d=1, n=5):
    """
    Function that prints n lines of arithmetic sequence in console:
    a1 = a0 + d
    a2 = a1 + d
    ...

    :param a0: the first member of the sequence (default 0)
    :param d:  the difference of the sequence (default 1)
    :param n:  total number of printable values of sequence (default 5)
    """
    sequence = list()
    formula = lambda a, d, pos: a + pos * d
    for position in range(n):
        sequence.append(formula(a0, d, position))
    print(sequence)


def Geometric_sequence(b0=0, q=1, n=5):
    """
    Function that prints n lines of geometric sequence in console:
    b1 = b0 * q
    b2 = b1 * q
    ...

    :param b0: the first member of the sequence (default 0)
    :param q:  the denominator of the sequence (default 1)
    :param n:  total number of printable values of sequence (default 5)
    """
    sequence = list()
    formula = lambda b, q, pos: b * q ** pos
    for position in range(n):
        sequence.append(formula(b0, q, position))
    print(sequence)


if __name__ == '__main__':
    print("{:-^80s}".format(" TEST 1 "))
    Task1 = decorator_1(Pascal_Triangle)
    Task1(10)
    Task1 = decorator_1(Quadratic_equation_solver)
    Task1(1, -2, -3)
    Task1 = decorator_1(Arithmetic_sequence)
    Task1(1, 4, 10)
    Task1 = decorator_1(Geometric_sequence)
    Task1(2, 2, 10)

    print("{:-^80s}".format(" TEST 2 "))
    Task2 = decorator_2(Pascal_Triangle)
    Task2(5)
    Task2 = decorator_2(Quadratic_equation_solver)
    Task2(1, -2, -3)
    Task2 = decorator_2(Arithmetic_sequence)
    Task2(1, 4, 10)
    Task2 = decorator_2(Geometric_sequence)
    Task2(2, 2, 10)

    print("{:-^80s}".format(" TEST 3 "))
    Task3 = decorator_3(Pascal_Triangle)
    Task3(6)
    Task3(4)
    Task3.change_function(Quadratic_equation_solver)
    Task3(1, -2, -3)
    Task3(2, 5, 3)
    Task3.change_function(Arithmetic_sequence)
    Task3(1, 4, 10)
    Task3.change_function(Geometric_sequence)
    Task3(2, 2, 10)
    Task3(1, 3, 10)
    Task3.print_rank_table()
    print(f"All decorator's output was sent to {Task3.__class__.__name__}.txt\n")

    print("{:-^80s}".format(" TEST 4 "))
    Task4 = decorator_4(Pascal_Triangle)
    Task4('d')
    Task4.change_function(Quadratic_equation_solver)
    Task4(1, -2, [2,4])
    Task4.change_function(Arithmetic_sequence)
    Task4(0, 5, 10)
    Task4.change_function(Geometric_sequence)
    Task4(2, 2, 10)
    Task4(1, 8, 5)
    Task4.print_rank_table()
    print(f"All decorator's output was sent to {Task4.__class__.__name__}.txt")
    print(f"All decorator's errors was sent to {Task4.__class__.__name__}_log.txt")
