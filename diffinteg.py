from sympy import Symbol, diff, sin
from scipy.integrate import quad

def Charles():
	# I love NSA Cryptologic Museum
	x = Symbol('x')
	dx = sin(x ** 2 / 1955)
	dx = diff(dx)
	print(dx)
Charles()