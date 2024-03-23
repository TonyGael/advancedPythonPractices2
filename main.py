########################################################################
# Basic idea:

# def my_decorator(function):
#
#     def wrapper():
#         print("Decorating in 3, 2, 1...")
#         function()
#
#     return wrapper  # Sin paréntesis aquí
#
#
# def hey_you():
#
#     print("Hey you!")
#
#
# my_decorator(hey_you)()

########################################################################

# def my_decorator(function):
#
#     def wrapper(*args, **kwargs):  # argu
#         print("Decorating the function.")
#         return_value = function(*args, *kwargs)
#         print("Before exit, we have again...")
#         return return_value
#
#     return wrapper
#
#
# @my_decorator
# def hello(person):
#     print(f'Hi {person}')
#     return f"Hi {person}"
#
#
# print(hello("Tony"))

########################################################################

# Unos ejemplos más práctico: #1 logging

# def logged(function):
#     def wrapper(*args, **kwargs):
#         value = function(*args, **kwargs)
#         with open('logfile.txt', 'a+') as f:
#             f_name = function.__name__
#             print(f'{f_name} function returned value {value}\n')
#             f.write(f'{f_name} function returned value {value}\n')
#         return f'this one {value} goes outside the logfile'
#     return wrapper
#
#
# @logged
# def add(x, y):
#     return x + y
#
#
# print(add(10, 20))

########################################################################
# otro ejemplo práctico: #2 logging

import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()  # actual timestamp
        value = function(*args, **kwargs)
        after = time.time()  # actual timestamp
        f_name = function.__name__
        print(f'{f_name} took {after-before} seconds to execute')
        return value
    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


myfunction(90000)
