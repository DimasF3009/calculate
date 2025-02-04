import numpy as np

# Matriks peluang transisi baru
P = np.array([
    [0.18, 0.27, 0, 0.36, 0.18],
    [0.06, 0.25, 0, 0.5, 0.19],
    [1, 0, 0, 0, 0],
    [0.15, 0.35, 0, 0.3, 0.2],
    [0.33, 0.33, 0.08, 0.08, 0.17]
])

# Menghitung P^8
P_8 = np.linalg.matrix_power(P, 8)

# Membulatkan hasil hingga 4 desimal
print(np.round(P_8, 4))
