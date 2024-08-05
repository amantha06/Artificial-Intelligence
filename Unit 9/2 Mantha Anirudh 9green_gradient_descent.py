import sys
import numpy as np

if sys.argv[1] == "A":
    g = lambda x, y: np.array((8*x - 3*y + 24, -3*x + 4*y - 20))
else:
    g = lambda x, y: np.array((2*(x - y**2), 2*(-2*x*y + 2*y**3 + y - 1)))
x, y = (0,0)

temp = g(x, y)  # gradient at (0, 0)
#dot product with itself gives magnitude
while np.sqrt(temp @ temp) > 0.00000001:
    x = x - 0.05 * (temp:=g(x, y))[0];
    y = y - 0.05 * temp[1]
    print("(" ,x, ", ", y, "), ", temp)