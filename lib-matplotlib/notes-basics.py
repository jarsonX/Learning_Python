#-MATPLOTLIB-FOR-DATA-VISUALIZATION----------------------------------------------------------------#

'''
Matplotlib has 3 layers: scripting, artist and backend. For the most cases in data analysis, we're
good with using the scripting layer (esentially the matplotlib.pyplot), which is intended to be 
easy to use.

'''

#--STYLES------------------------------------------------------------------------------------------#

# Enables to use different styles.

print(plt.style.available)
mpl.style.use(['ggplot'])

#--PLOT-FUNCTION-----------------------------------------------------------------------------------#

# Enables to create almost all of the conventional visualizations.

import matplotlib.pyplot as plt

plt.plot(5, 5, 'o')
plt.show()

# NOTE: when using Jupyter notebook, we might need to force the graph to be printed within the 
# browser by adding 'magic' function before importing matplotlib, i.e.:

%matplotlib_inline
import matplotlib.pyplot as plt

# However, _inline backend keeps us from modifying graph once it is created and shown. To overcome
# this, we can use %matplotlib_notebook backend instead. Then, when a function is called, it checks
# if an active figure already exist and apply any effects to it.


#--PANDAS------------------------------------------------------------------------------------------#

# Pandas has a built-in implementation of matplotlib, therefore plotting is as simple as calling the
# plot function on a given pandas series or dataframe.

df_name.plot(kind='line')   or   df_name['column_1'].plot(kind='hist') etc.
