#Note:  Run the programme by pressing Alt + R
import folium
import pandas

data = pandas.read_csv("hotels.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
ad = list(data["Address"])
sta = list(data["State"])

#This function together with the for loop and the color makes the diffrent colors on the map
def color_maker(state):
    if state == "Abuja":
        return "blue"
    elif state == "Lagos":
        return "green"

#This produces the particular area on the map to be shown
map = folium.Map(location=[8.94, 7.22], zoom_start = 6) #tiles="Mapbox Bright")


#Create a featured group for the map so we can call the add_child, it helps when you want to add other features to your map
fgh = folium.FeatureGroup(name="Hotels")

#This produces the markers on the maps
for lt, ln, ad, st in zip(lat, lon, ad, sta):
    fgh.add_child(folium.Marker(location=[lt, ln], popup=ad, tooltip="click to get Address", icon=folium.Icon(color=color_maker(st))))



#featured group for the population color and its attribute
fgp = folium.FeatureGroup(name="Population")

#to add the json file for the polygon attribute:                                     #here we added a lambda function to give our map a population color
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), style_function =lambda x: {'fillColor':'yellow'
if x['properties']['POP2005'] <10000000 else 'green' }))

map.add_child(fgh)
map.add_child(fgp)

#To turn on and off the feature groups on the map layers
map.add_child(folium.LayerControl())



map.save("Map1.html")
