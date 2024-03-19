# def mydecorator(function):
#
#     def wrapper(*args, **kwargs):
#         print("Decorating the function.")
#         return_value = function(*args, *kwargs)
#         return return_value
#
#     return wrapper
#
#
# @mydecorator
# def hello(person):
#     print(f'Hi {person}')
#     return f"Hi {person}"
#
#
# print(hello("Tony"))

# Practical example #1: logging
# def logged(function):
#     def wrapper(*args, **kwargs):
#         value = function(*args, **kwargs)
#         with open('logfile.txt', 'a+') as f:
#             fname = function.__name__
#             f.write(f'{fname} returned value {value}')
#         return value
#
#     return wrapper
#
# @logged
# def add (x, y):
#     return x + y
#
# print(add(10, 20))
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after-before} seconds to execute')
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result

myfunction(11000)
