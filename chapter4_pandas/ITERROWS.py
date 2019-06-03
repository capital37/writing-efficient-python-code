# Loop over every element in a column of a DF
# Use iterrows instead of data.iloc[]

import pandas as pd
data = pd.read_csv('PitchingPost.csv')

WL = []
for index, row in data.iterrows():

    W = row['W']

    L = row['L']

    WL.append(W+L)

data['WL'] = WL
print(data.WL.head())
