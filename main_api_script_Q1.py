#!/usr/bin/env python
# coding: utf-8

# # Ventagium
# 
# 
# 
# ## Task: Desarrollar un pipeline en Python que deberá:
# 
# 1. Extraer los datos correspondientes al total de población de cada país usando la API JSON
# de Indicadores del Banco Mundial.
# 
# - a. Debe recibir un parámetro para limitar la respuesta a la cantidad de países que se
# soliciten. De tal forma que se puedan solicitar, por ejemplo, los 10, 20, 30 países con la
# mayor población.
# 
# - b. Almacenar los datos extraídos en un objeto DataFrame de la librería Pandas.

# 

# # Structuring an API Call:
# #### https://datahelpdesk.worldbank.org/knowledgebase/articles/898581
# 
# Responses
# Retrieving indicator data about countries is one common use of the API.
# 
# For example, the following is a call for 2006 data on the GDP of Brazil: https://api.worldbank.org/v2/country/br/indicator/NY.GDP.MKTP.CD?date=2006
# 
# Response Format
# By default, all requests will respond with valid XML. To receive the response in JSON format, provide format=json in any request.
# 
# 
# ## Using 'all' for all countries' data:
# 
# How to use the V2 Indicators API
# Version 2 (V2) of the Indicators API has been released and replaces V1 of the API. V1 API calls will no longer be supported. To use the V2 API, you must place v2 in the call. For example: https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL.
# 

# In[2]:


#pop_url = "https://api.worldbank.org/v2//country/all/indicator/SP.POP.TOTL?date=2020:2025&format=json"
#response = requests.get(pop_url)
#data = response.json()


# ### Country ISO Codes: https://wits.worldbank.org/wits/wits/WITSHELP-es/content/codes/country_codes.htm
# 
# They only have 3 upper case letters --> 'countryiso3code'

# 

# In[3]:


# Libraries

import wbgapi as wb
import pandas as pd
import pycountry
import plotly
import plotly.express as px

# Function
def top_countries_by_population(num_countries=10, return_df_only=False):

    # Fetch population data for all available countries for all years
    # Fetching data from API (wb): 
        # total, Population: 'SP.POP.TOTL'
        # economy='all' for all countries' data
        # time='all' for all years
        # labels=True to include country names
    df = wb.data.DataFrame('SP.POP.TOTL', economy='all', time='all', labels=True)

    # Reset index to make 'Country Code' a column
    df = df.reset_index()
    # Rename 'economy' column to 'Country Code'
    df.rename(columns={'economy': 'Country Code'}, inplace=True)
    # Removing rows that are not actual countries with pycountry's alpha_3 function
    valid_country_codes = [country.alpha_3 for country in pycountry.countries]
    df = df[df['Country Code'].isin(valid_country_codes)]
    # Find the most recent year in the dataset dynamically
    latest_year = str(df.columns[df.columns.str.startswith('YR')].max())
    # Keep only relevant columns: 'Country Code', 'Country' and the most recent year
    df = df[['Country Code', 'Country', latest_year]].rename(columns={latest_year: 'Population'})
    # Convert population to integer, fill NaNs with 0, and sort by population
    df['Population'] = df['Population'].fillna(0).astype(int)
    df = df.sort_values(by='Population', ascending=False)
    # Select the top N countries
    df = df.head(num_countries)
    # Reset index to start at 1 instead of 0
    df.index = range(1, len(df) + 1)
    
    #  If only the DataFrame is needed, return it without plotting
    if return_df_only:
        return df
    
    # Plot

    # Interactive bar chart using plotly
    fig = px.bar(df, 
                x='Population', 
                y='Country', 
                orientation='h', 
                title=f'Top {num_countries} Countries by Population',
                labels={'Population': 'Population', 'Country': 'Country'})

    # When hovering, create a text box per country with country's information
    fig.update_traces(
        customdata=df[['Country Code', 'Population']].values,
        hovertemplate=
        '<b>Country</b>: %{y}<br>' +
        '<b>Country Code</b>: %{customdata[0]}<br>' +  # Country Code from customdata
        '<b>Population</b>: %{customdata[1]:,}<br>'  # Population from customdata with comma formatting
    )

    # Plot layout with axis titles and grid
    fig.update_layout(
        xaxis_title="Population",
        yaxis_title="Country",
        plot_bgcolor='white',
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
        yaxis=dict(
            showgrid=False,
            tickangle=0  # Country names are horizontal
        ),
        # Increase canvas size
        width=1000,  # Increase width of the figure
        height=1000,  # Increase height of the figure
    )

    # Show the plot
    fig.show()

    return df


# In[24]:


top_countries_by_population(25)

