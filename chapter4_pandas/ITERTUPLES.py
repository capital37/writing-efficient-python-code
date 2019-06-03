import pandas as pd
data = pd.read_csv('PitchingPost.csv')

for row_namedtuple in data.itertuples():
    if row_namedtuple.Index < 7:
        print(row_namedtuple.playerID)
