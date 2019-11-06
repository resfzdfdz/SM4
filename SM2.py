import time

def moddiv(a, b, p):
	u, v, m, n = a, p, b, 0
	
	while (u != 1):
		r = v // u
		u, v = v - r * u, u
		m, n = (n - r * m) % p, m

	return m

