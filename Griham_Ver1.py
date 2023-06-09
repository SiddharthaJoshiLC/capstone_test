# Siddhartha Joshi
#
# Griham_Ver1.py
#
# Setup stuff.

# from descartes import PolygonPatch
# import shapefile
# import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from matplotlib.colors import ListedColormap
from shapely.geometry import Point
import streamlit as st

# *******************************************************************************
# Load datafile with CD name and geo-location.

CD_Loc = "GeoLookup.csv"
nyc_CD_data = pd.read_csv(CD_Loc)

# Take a quick peek at the data.
nyc_CD_data.head()

# *******************************************************************************

# Lookit column names.
# nyc_CD_data.columns

# Get the rows with community district geolocation.
geotype = nyc_CD_data['GeoType']
locns=nyc_CD_data[geotype == "CD"] 
locns = locns.reset_index(drop=True)
geoid=list(locns['GeoID'])
lat=list(locns['Lat'])
long=list(locns['Long'])
LL=pd.concat([locns['Name'],locns['Borough'],locns['Long'], locns['Lat'],locns['GeoID'],locns['BoroID']],
             axis=1, keys=['District name','Boro name','Long', 'Lat','CommunityDistrict','ParticulateMatter'])

# *******************************************************************************

# # fig, ax = plt.subplots(figsize=(10, 10))

# geometry = [Point(xy) for xy in zip(LL['Long'], LL['Lat'])]
# gdf = gpd.GeoDataFrame(LL, geometry=geometry, crs=4326)
# # MM = gdf.explore(height=500, width=700, color='blue', name='Points')
# MM = gdf.explore(height=500, width=700, color='blue', name='Points',style_kwds={"style_function":lambda x: {"radius":6}})
# MM

# *******************************************************************************

# Load pollution data.

CD_Pollution = "Pollution_NYC.csv"
nyc_pollution_data = pd.read_csv(CD_Pollution)

# Take a quick peek at the data.
nyc_pollution_data.head()

# *******************************************************************************

data_time=nyc_pollution_data['Time']
locns_pollution=nyc_pollution_data[data_time=='Annual Average 2021']

geotype = locns_pollution['GeoType']
locns_CD=locns_pollution[geotype == "CD"]

m_id = locns_CD['MeasureID']
locns_pol=locns_CD[m_id == 365]

locns_pol = locns_pol.reset_index(drop=True)

# data_time2 = [x.replace(" ", "") for x in data_time]

# locns_avg=locns[data_time2=='AnnualAverage2021']
# pol_index=list(locns['DisplayValue'])
# geoid=list(locns['GeoID'])

LL2=pd.concat([locns['Name'],locns['Borough'],locns['Long'], locns['Lat'],locns_pol['DisplayValue']],
             axis=1, keys=['District name','Boro name','Long', 'Lat','ParticulateMatter'])
LL1=pd.concat([locns['Name'],locns['Borough'],locns_pol['DisplayValue']],
             axis=1, keys=['District name','Boro name','ParticulateMatter'])

# Save "data"

import dill

with open('LL2.pkd', 'wb') as f:
    dill.dump(LL2, f)
with open('LL1.pkd', 'wb') as f:
    dill.dump(LL1, f)
    
# # *******************************************************************************

# # fig, ax = plt.subplots(figsize=(10, 10))

# geometry2 = [Point(xy) for xy in zip(LL2['Long'], LL2['Lat'])]
# gdf2 = gpd.GeoDataFrame(LL1,  geometry=geometry2, crs=4326)
# # gdf2 = gpd.GeoDataFrame(LL2, geometry=geometry2, crs=4326)
# # MM = gdf.explore(height=500, width=700, color='blue', name='Points')

# st.write(gdf2.head())

# MM2 = gdf2.explore(height=500, width=700, color='blue', name='Points',style_kwds={"style_function":lambda x: {"radius":6}})
# MM2



