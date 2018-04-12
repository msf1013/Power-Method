import numpy as np

A = np.array([[1.0, 2.0, 3.0, 2.0],
              [2.0, 12.0, 13.0, 11.0],
              [-2.0, 3.0, 0.0, 2.0],
              [4.0, 5.0, 7.0, 2.0]])

x_k = np.array([1.0, 0.0, 0.0, 0.0])

for i in range(0, 20):
    A_x_k = A.dot(x_k)
    miu = max(A_x_k.min(), A_x_k.max(), key=abs)
    print("Iteration #%d" % (i))
    print(miu)
    print(x_k)
    print("")
    x_k = 1.0 / miu * A_x_k


