import numpy as np
# Matriks peluang transisi
P = np.array([
    [0, 1, 0, 0, 0],
    [0, 0.32, 0, 0.56, 0.12],
    [0, 0, 0, 1, 0],
    [0.05, 0.78, 0.05, 0.05, 0.05],
    [0.5, 0.25, 0, 0.25, 0]
])

# Peluang state awal
p0 = np.array([0.053, 0.486, 0.016, 0.338, 0.076])

# Simpan hasil peluang dari langkah ke-1 hingga ke-6
pn_steps = [p0]

# Iterasi untuk menghitung hingga langkah ke-6
for _ in range(6):
    pn_next = np.dot(pn_steps[-1], P)
    pn_steps.append(pn_next)

# Format hasil sebagai DataFrame untuk tampilan yang lebih baik
import pandas as pd

pn_df = pd.DataFrame(pn_steps[1:], columns=["State 1", "State 2", "State 3", "State 4", "State 5"])
pn_df.index = [f"p{n}" for n in range(1, 7)]
print(pn_df)

