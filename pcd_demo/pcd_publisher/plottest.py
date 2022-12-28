import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

a = [(1,1,1),(2,2,2)]

print(a[0])

ax.scatter(a[0]) # plot the point (2,3,4) on the figure

plt.show()