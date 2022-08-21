import matplotlib
import matplotlib.pyplot as plt
import numpy as np

count, bin_edges = np.histogram(df['column'])

df['column'].plot(kind='hist', bins=10, xticks=bin_edges)

plt.title('Salary distribution')
plt.xlabel('Salary')
plt.ylabel('Count')

plt.show()

#We can create a histogram without numpy, however numpy makes sure that bin edges
#are aligned with the tick marks on the horizontal axis (x axis).
