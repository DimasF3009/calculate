import numpy as np

# Matriks peluang transisi CPO
P = np.array([
    [0, 1, 0, 0, 0],
    [0, 0.32, 0, 0.56, 0.12],
    [0, 0, 0, 1, 0],
    [0.05, 0.79, 0.05, 0.05, 0.05],
    [0.5, 0.25, 0, 0.25, 0]
])

# Menghitung P^6
P_6 = np.linalg.matrix_power(P, 6)

# Membulatkan hasil hingga 4 desimal
print(np.round(P_6, 4))
