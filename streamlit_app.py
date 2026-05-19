import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Establece el título y el favicon que aparecen en la barra de pestañas del navegador.
st.set_page_config(
    page_title='Panel de PIB',
    page_icon=':earth_americas:', # Este es un shortcode de emoji. También podría ser una URL.
)

# -----------------------------------------------------------------------------
# Declarar algunas funciones útiles.

@st.cache_data
def get_gdp_data():
    """Obtener datos de PIB desde un archivo CSV.

    Esto usa caché para evitar tener que leer el archivo cada vez. Si estuviéramos
    leyendo desde un endpoint HTTP en lugar de un archivo, es buena idea establecer
    una edad máxima para la caché con el argumento TTL: @st.cache_data(ttl='1d')
    """

    # En lugar de un CSV en disco, también podrías leer desde un endpoint HTTP aquí.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # Los datos arriba tienen columnas como:
    # - Country Name
    # - Country Code
    # - [Cosas que no me importan]
    # - GDP para 1960
    # - GDP para 1961
    # - GDP para 1962
    # - ...
    # - GDP para 2022
    #
    # ...pero quiero esto en su lugar:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # Así que vamos a pivotar todas esas columnas de año en dos: Year y GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convertir años de cadena a enteros
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Dibujar la página actual

# Establecer el título que aparece en la parte superior de la página.
'''
# :earth_americas: Panel de PIB

Navega los datos de PIB desde el sitio de [World Bank Open Data](https://data.worldbank.org/). Como notarás,
los datos solo llegan hasta 2022 por ahora, y los puntos de datos para ciertos años a menudo faltan.
Pero sigue siendo una gran fuente de datos (¿y mencioné que es _gratis_?).
'''

# Agregar algo de espacio
''
''

min_value = gdp_df['Year'].min()
max_value = gdp_df['Year'].max()

from_year, to_year = st.slider(
    '¿Qué años te interesan?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

countries = gdp_df['Country Code'].unique()

if not len(countries):
    st.warning("Selecciona al menos un país")

selected_countries = st.multiselect(
    '¿Qué países te gustaría ver?',
    countries,
    ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

''
''
''

# Filtrar los datos
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('PIB a lo largo del tiempo', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'PIB en {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'PIB de {country}',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
