#Simple Line Chart using Plotly Graph Objects (low-level interface) and Plotly Express (high-level wrapper)

import plotly.graph_objects as go
import plotly.express as  px
import numpy as np

np.random.seed(10)
x = np.arange(12)
y = np.random.randint(50, 500, size=12)

#Plotly Graph Objects

fig = go.Figure(data = go.Scatter(x=x, y=y))
fig.update_layout(title='Simple Line Plot', xaxis_title='Month', yaxis_title='Sales')
fig.show()

#Plotly Express

fig = px.line(x=x, y=y, title='Simple Line Plot', labels=dict(x='Month', y='Sales'))
fig.show()
