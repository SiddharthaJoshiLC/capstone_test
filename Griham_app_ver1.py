import pandas as pd
import geopandas as gpd
import streamlit as st
import dill
from shapely.geometry import Point

fname1='LL1.pkd'
fname2='LL2.pkd'

# Load "data".
# with open('LL1.pkd', 'rb') as f:
with open(fname1, 'rb') as f:
    LL1 = dill.load(f)
with open(fname2, 'rb') as f:
    LL2 = dill.load(f)
        
# gdf2 = gpd.GeoDataFrame(
#     LL1, geometry=gpd.points_from_xy(LL2.Long, LL2.Lat), crs=4326)

geometry2=gpd.points_from_xy(LL2.Long, LL2.Lat)
# geometry2 = [Point(xy) for xy in zip(LL2['Long'], LL2['Lat'])]
gdf2 = gpd.GeoDataFrame(LL1,  geometry=geometry2, crs=4326)

MM2 = gdf2.explore(height=500, width=700, color='blue', name='Points',style_kwds={"style_function":lambda x: {"radius":6}})
# MM2
interactive_map = MM2._repr_html_()

file_html = open("your_map.html", "w")
file_html.write(interactive_map)
file_html.close()

