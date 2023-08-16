def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

#test
print(fact(6)) 
''' 
 going to recreate this function with only the constructs 
# available in the lambda calculus, which are

definitions of functions with one argument
calls to functions with one argument

'''
IS_ZERO = lambda x: x == 0
ONE = 1
SUB1 = lambda x: x - 1
MULT = lambda x,y: x * y
IF = lambda cond, t_func, f_func: t_func if cond else f_func()


def fact(n):
    return IF (
      IS_ZERO(n),
      lambda: ONE,
      lambda: MULT(n, fact(SUB1(n)))
    )

