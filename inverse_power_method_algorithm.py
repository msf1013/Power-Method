import numpy as np

A = np.array([[1.0, 2.0, 3.0, 2.0],
              [2.0, 12.0, 13.0, 11.0],
              [-2.0, 3.0, 0.0, 2.0],
              [4.0, 5.0, 7.0, 2.0]])

x_k = np.array([1.0, 0.0, 0.0, 0.0])

alpha = 0.0001

for i in range(0, 20):
    y = np.linalg.inv(A - alpha * np.identity(4)).dot(x_k)
    miu = max(y.min(), y.max(), key=abs)
    v = alpha + 1.0 / miu
    print("Iteration #%d" % (i))
    print(v)
    print(x_k)
    print("")
    x_k = y * 1.0 / miu


