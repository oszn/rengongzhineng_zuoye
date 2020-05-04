import  folium

map_hooray=folium.Map(location=[51.5074,0.1278],zoom_start=11)
map_hooray.choropleth()
map_hooray.save("d.html")