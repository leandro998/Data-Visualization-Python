import numpy as np
import pandas as pd
import folium

# world_map = folium.Map()
# world_map.save('world.html')

world_map = folium.Map(location=[56.130, -106.35],
                       zoom_start=4,
                       tiles='Stamen Terrain')
world_map.save('world.html')
