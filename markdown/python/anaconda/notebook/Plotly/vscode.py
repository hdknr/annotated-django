#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

#%%
print("Hello")

#%%
DATA = '/Users/hide/Documents/Tech/annotated-django/samples/django-history/web/notebooks/Plotly/birth.csv'
import pandas as pd
raw = pd.read_csv(DATA)
import plotly
plotly.offline.init_notebook_mode(connected=False)
print(raw['bitrhs'], raw['year'], raw['birth rate'])
data = [
    plotly.graph_objs.Bar(x=raw["year"], y=raw["bitrhs"], name="Births"),
    plotly.graph_objs.Scatter(x=raw["year"], y=raw["birth rate"], name="Birth Rate", yaxis="y2")
]
layout = plotly.graph_objs.Layout(
    title="Births and Birth Rate in Japan",
    legend={"x":0.8, "y":0.1},
    xaxis={"title":"Year"},
    yaxis={"title":"Births"},
    yaxis2={"title":"Birth Rate", "overlaying":"y", "side":"right"},
)
fig = plotly.graph_objs.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)