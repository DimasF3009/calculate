import numpy as np
import pandas as pd

# Matriks peluang transisi TBS
transition_matrix = np.array([
    [0.18, 0.27, 0.00, 0.36, 0.18],
    [0.06, 0.25, 0.00, 0.50, 0.19],
    [1.00, 0.00, 0.00, 0.00, 0.00],
    [0.15, 0.35, 0.00, 0.30, 0.20],
    [0.33, 0.33, 0.08, 0.08, 0.17]
])

# Peluang state awal
initial_state = np.array([0.054900, 0.491160, 0.016900, 0.324060, 0.075220])

# Jumlah langkah prediksi
n_steps = 8

# DataFrame untuk menyimpan hasil
results = pd.DataFrame(columns=["State 1", "State 2", "State 3", "State 4", "State 5"], index=[f"p{i+1}" for i in range(n_steps)])

# Simulasi peluang state untuk n langkah
current_state = initial_state
for step in range(n_steps):
    results.iloc[step] = current_state
    current_state = np.dot(current_state, transition_matrix)

# Format hasil agar tampil sesuai keinginan
print(results.round(6))