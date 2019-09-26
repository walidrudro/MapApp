import folium
import pandas

data = pandas.read_csv("bd.csv")


map = folium.Map(location=[22.8456, 89.5403])
fg
map.add_child(folium.Marker(location=[]))

map.save("Map1.html")
