'''
    NumPy array provide a fast and memory efficient alternative to Python lists.
'''

import numpy as np

# NumPy arrays are homogenious, they must contain elements of the same type
nums_np_ints = np.array([1, 2, 3])
print(nums_np_ints.dtype)


'''
    When analysing data, you'll often want to perform operations over entire
    collections of values quickly.
'''
nums_np = np.array([-2, -1, 0, 1, 2])
print(nums_np ** 2)

# NumPy array boolean indexing
print(nums_np>0)
