import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4, 5])

print(s.mean())
print(s.sum())