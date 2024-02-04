import sympy
from sympy import symbols 

vars('x','y')

eq = 2*x  + 10*y + 4

sympy.factor(eq)