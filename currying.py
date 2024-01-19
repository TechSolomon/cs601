# Exercises:
# "Currying" is the conversion of multi-argument functions into a chain of simpler single-argument functions that give the same result.
#    Write a Python function curry2 that takes a single argument: a function, that in turn takes two arguments.  Curry2 should return a chain of higher-order functions that take one argument at a time.  For example, curry2(f)(a)(b) should give the same result as f(a,b).
#    Now write a Python or Javascript function curryN that takes the number of arguments to curry.  For example, curryN(f,2)(a)(b) should give the same result as f(a,b). Hint: curryN needs to use recursion.

# In Python you can call a function with N arguments in a [] list with a star syntax
# In JavaScript you can call a function with an array of arguments using fn.apply(fn,argArray) , or set each parameter one at a time using fn.bind(fn,firstArg)
