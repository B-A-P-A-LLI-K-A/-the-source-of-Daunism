import numpy
import numpy as np
m1 = np.array([[2, 2, 3], [2, 2, 3], [2, 2, 3]])
print(m1)
m2 = np.array([[4, 4, 5], [4, 4, 5], [4, 4, 5]])
print(m2)
r1 = m1 + m2
print(r1)
r2 = np.dot(m1, m2)
print(r2)
lm = np.zeros((1000, 1000))
print(lm)
r3 = m1 * m2
print(r3)
