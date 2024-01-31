import pandas as pd
import numpy as np
import webbrowser
import plotly.express as px
import plotly as py

df = px.data.tips()
fig = px.scatter(df, x = 'total_bill', y = 'tip', color = 'size', facet_col = 'sex',
                 color_continuous_scale= px.colors.sequential.Viridis, render_mode= 'webgl')
fig.show()