import numpy as np
import pandas as pd
import plotly.express as px

population = pd.read_html('https://en.wikipedia.org/wiki/Demographics_of_India')

literacy_rate = population[16].drop(35).drop('State or UT code',axis=1)

literacy_rate.at[0,'State or UT'] = 'Jammu & Kashmir'
literacy_rate.at[27,'State or UT'] = 'Andhra Pradesh'


population = population[8].drop(36).rename(columns={'Population[57]': 'Population','Rural[58]':'Rural','Urban[58]':'Urban','Area[59] (km2)':'Area (km2)'})

population.at[[18,19,28,30,32,33,34,35],'State/UT'] = ['Delhi','Jammu & Kashmir','Puducherry','Chandigarh','Andaman and Nicobar Islands','Dadra and Nagar Haveli','Daman and Diu','Lakshadweep']


population = population.set_index('Rank')


fig1 = px.choropleth(
  data_frame=literacy_rate,
geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
featureidkey='properties.ST_NM',
locations='State or UT',
color='Overall (%)',
color_continuous_scale='Blues',
title='Literacy Rate in India'
)

fig2 = px.choropleth(
  data_frame=population,
geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
featureidkey='properties.ST_NM',
locations='State/UT',
color='Population',
color_continuous_scale='Reds',
title='Population of India in 2011'
)

fig1.update_geos(fitbounds="locations", visible=False)
fig2.update_geos(fitbounds="locations", visible=False)

fig1.show()
fig2.show()

population.to_csv('Population of India.csv')

literacy_rate.to_csv('Literacy Rate of India.csv')
