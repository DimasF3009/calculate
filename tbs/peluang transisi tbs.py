import numpy as np

# Matriks frekuensi transisi
frekuensi_transisi_tbs = np.array([
 [2, 3, 0, 4, 2],
 [1, 4, 0, 8, 3],
 [1, 0, 0, 0, 0],
 [3, 7, 0, 6, 4],
 [4, 4, 1, 1, 2]
])

# Hitung matriks peluang transisi
total_transisi = frekuensi_transisi_tbs.sum(axis=1, keepdims=True)
matriks_peluang_transisi_tbs = np.divide(frekuensi_transisi_tbs, total_transisi, where=total_transisi != 0)

print("Matriks Peluang Transisi TBS:")
print(np.round(matriks_peluang_transisi_tbs, 2))

