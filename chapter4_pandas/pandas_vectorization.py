"""
    We can use NumPy methods with pandas, like broadcasting
    we can use the .values method to transform it into a numpy
    array.
"""

import pandas as pd

data = pd.read_csv('PitchingPost.csv')

print(type(data['W'].values - data['L'].values))
data['WL'] = data['W'].values - data['L'].values
print(data['WL'].head())
