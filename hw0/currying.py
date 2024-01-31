# currying.py
# Solomon Himelbloom
# 2024-01-22
#
# For CS 601 Spring 2024
#
# "Currying" Exercises
# - Conversion of multi-argument functions into a chain of simpler single-argument functions that give the same result.
# - In Python you can call a function with N arguments in a [] list with a star syntax.
# - In JavaScript you can call a function with an array of arguments using fn.apply(fn,argArray),
#    or set each parameter one at a time using fn.bind(fn,firstArg).


def curry2(f):
    """Returns a chain of higher-order functions that take one argument at a time.
    For example, curry2(f)(a)(b) should give the same result as f(a,b)."""
    return lambda a: lambda b: f(a, b)


def curryN(f, n):
    """Takes the number of arguments to curry.
    For example, curryN(f,2)(a)(b) should give the same result as f(a,b)."""

    # BASE CASE

    if n == 0:
        return f

    # RECURSIVE CASE

    def curried(*args):
        if len(args) == n:
            return f(*args)
        return lambda x: curried(*(args + (x,)))

    return curried


def f(*args):
    return sum(args)
