### Calculate the mean of each row in a array of arrays
import numpy as np

arr = np.array([
        [90, 92, 75],
        [25, 20, 10]
    ])

# Mean for each row, mean acros the column values(axis=1)
avgs_np = arr.mean(axis=1)
print(avgs_np)
