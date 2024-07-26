import pandas as pd
import numpy as np

# Menetapkan jumlah data dan kolom
num_rows = 100
num_cols = 5

# Membuat data dummy menggunakan numpy
data = np.random.rand(num_rows, num_cols)

# Menetapkan nama kolom
columns = [f'Column_{i}' for i in range(1, num_cols + 1)]

# Membuat DataFrame menggunakan pandas
df = pd.DataFrame(data, columns=columns)

# Menampilkan DataFrame
print(df)
