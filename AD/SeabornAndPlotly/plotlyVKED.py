import pandas as pd
import numpy as np
import webbrowser
import plotly.express as px
import plotly as py

df = px.data.tips()
fig = px.scatter(df, x = 'total_bill', y = 'tip', color = 'size', facet_col = 'sex',
                 color_continuous_scale= px.colors.sequential.Viridis, render_mode= 'webgl')
fig.show()

df = px.data.gapminder()
fig = px.scatter(df.query('year == 2007'), x = 'gdpPercap', y = 'lifeExp',
                 size = 'pop', color = 'continent', hover_name = 'country', log_x = True, size_max = 60)
fig.show()

df = px.data.gapminder()
fig = px.scatter(df, x = 'gdpPercap', y = 'lifeExp', animation_frame = 'year',
                 animation_group = 'country', size = 'pop', color = 'continent', hover_name = 'country', 
                 facet_col= 'continent', log_x = True, size_max = 45, range_x = [100, 100000], range_y = [25, 90])
fig.show()

py.offline.plot(fig, filename = 'plotLYMap.html', auto_open = False)