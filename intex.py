import sys
import sympy as sy
from sympy.parsing.sympy_parser import parse_expr

def main(arg):
    if len(arg) > 3:
        return "Error. Too many arguments given."
    elif len(arg) == 1:
        return "Error. No arguments were provided."
    else:
        return intex(arg[-1], "d" in arg[1], "i" in arg[1], "l" in arg[1])

def intex(txt, dif, integ, latex):
    x, y, z, t = sy.symbols("x, y, z, t")
    f = parse_expr(txt)
    if dif:
        f = sy.diff(f, x)
    if integ:
        f = sy.integrate(f, x)
    if latex:
        f = sy.latex(f)
        return sy.latex(f)
    else:
        return f

print(main(sys.argv))
