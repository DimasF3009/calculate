import numpy as np

# Matriks frekuensi transisi
frekuensi_transisi_cpo = np.array([
[0, 3, 0, 0, 0],
 [0, 8, 0, 14, 3],
 [0, 0, 0, 1, 0],
 [1, 15, 1, 1, 1],
 [2, 1, 0, 1, 0]
])

# Hitung matriks peluang transisi
total_transisi = frekuensi_transisi_cpo.sum(axis=1, keepdims=True)
matriks_peluang_transisi_cpo = np.divide(frekuensi_transisi_cpo, total_transisi, where=total_transisi != 0)

print("Matriks Peluang Transisi CPO:")
print(np.round(matriks_peluang_transisi_cpo, 2))
