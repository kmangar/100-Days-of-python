import time


# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     def one():
#         print("one")
#
#     def two():
#         print("two")
#
#     return nested_function, one, two
#
#
# inner_function, a, b = outer_function()
# inner_function(), a()
#
# # Decorator functions
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # do something
#         function()
#         function()
#         # do something after
#
#     return wrapper_function()
#
#
# @delay_decorator
# def say_hello():
#     print("hello")
#
# def say_bye():
#     print("bye")
#
# def say_greeting():
#     print("How are you? ")
#
#
# decorated_function = delay_decorator(say_greeting)
# decorated_function()


# CODING ROOM DAY 54
import time

current_time = time.time()



def speed_calc_decorator():
    def fast_function():
        for i in range(10000000):
            i * i
        print("fast_function run speed: %s s" % (time.time() - current_time))
    fast_function()

    def slow_function():
        for i in range(100000000):
            i * i
        print("slow_function run speed: %s s" % (time.time() - current_time))
    slow_function()



speed_calc_decorator()
