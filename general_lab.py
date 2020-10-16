# This file runs the practice of Data Visualization Course
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

fig = Figure()
canvas = FigureCanvas(fig)
x = np.random.randn(10000)

# Using figure:
# ax = fig.add_subplot(111) # 111 = 1 row + 1 column + 1 cell for location of that axis
# ax.hist(x, 100)
# ax.set_title('Normal Distribution with $\mu=0, \sigma=1$')
# fig.savefig('matplotlib_histogram.png') # file saved to folder

# Using pyplot:
# %matplotlib inline >> code to force exhibition in the same screen
plt.hist(x, 100)
plt.title(r'Normal Distribution with $\mu=0, \sigma=1$')
# plt.savefig('matplotlib_histogram.png') # file saved to folder
plt.show()
