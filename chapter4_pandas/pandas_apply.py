"""
    * pandas.apply acts like the function map function,
    it takes a function as an input and applies this function
    to an entire DataFrame.

    * Must specify axis to apply (0 for columns; 1 for rows)

    * Can be used with anonymous functions (lambda functions)
"""
import pandas as pd

data = pd.read_csv('PitchingPost.csv')
print(data.head(2))

data['WR'] =  data.apply(
                        lambda row: row['W'] + row['R'],
                        axis=1)
print(data.loc[:5, ['W', 'R', 'WR']])
