 #VIOLIN PLOT
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
import pandas as pd
#from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module
data = [np.random.randn(100) for _ in range(4)]
# Create violin plot
plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()