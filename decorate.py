#Angela Yu
#SoftDev2 pd8
#HW13 -- Decoration Day
#2017-05-01

import time

def name(f):
    def inner(*arg):
        print f.func_name+ str(arg)
        return f(*arg)
    return inner

def timer(f):
    def inner (*arg):
        start=time.time()
        f(*arg)
        stop=time.time()
        return "time used: " + str(stop-start)
    return inner

'''def wrapper( f ):
   def inner( *arg ):
       return f( *arg )
   return inner'''

@timer
@name
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print fib(15)
