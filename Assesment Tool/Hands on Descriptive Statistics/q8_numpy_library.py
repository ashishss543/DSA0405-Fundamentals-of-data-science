import numpy as np

data = np.array([10, 20, 20, 30, 40])
print('Mean:', np.mean(data))
print('Median:', np.median(data))
print('Mode:', np.bincount(data).argmax())
