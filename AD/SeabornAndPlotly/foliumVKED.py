import folium
from folium import plugins
import pandas as pd
import numpy as np
import webbrowser


partizan = pd.read_excel("E:/Programming/VKED/AD/SeabornAndPlotly/partizan.xlsx")
print(partizan.tail())

lats = list(partizan.lat)
longs = list(partizan.lon)
places = [[x[0], x[1]] for x in zip(lats,longs)]

m = folium.Map(places[0], tiles = 'OpenStreetMap', zoom_start = 13)

plugins.MarkerCluster(places).add_to(m)
m.save("map.html")
webbrowser.open("map.html")

plugins.BoatMarker(places[0]).add_to(m)
m.save("map2.html")
webbrowser.open("map2.html")

plugins.FastMarkerCluster(places).add_to(m)
m.save("map3.html")
webbrowser.open("map3.html")