import requests
import pandas as pd
import streamlit as st


container = st.container()

with st.sidebar:
	south_input = st.text_input('South Bound', 'South Coordinates')
	north_input = st.text_input('North Bound', 'North Coordinates')
	west_input = st.text_input('West Bound', 'West Coordinates')
	east_input = st.text_input('East Bound', 'East Coordinates')

	if st.button('Show Bounds'):
		south = float(south_input)
		north = float(north_input)
		east = float(east_input)
		west = float(west_input)
		xbounds = [south,south,north,north]
		ybounds = [east,west,east,west]
		df = pd.DataFrame(data={'lat':xbounds,'lon':ybounds})
		container.map(df)
	if st.button('Download DEM'):
		url = 'https://portal.opentopography.org/API/globaldem?demtype=SRTMGL3&south='+south_input+'&north='+north_input+'&west='+west_input+'&east='+east_input+'&outputFormat=GTiff&API_Key=affc94e52b51bbc5657be5b80e1bf15f'
        response = requests.get(url) 
		open('raster.tiff','wb').write(response.content)