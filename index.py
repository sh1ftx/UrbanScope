from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from app import app
from _map import *
from _histogram import *
from _controllers import *

# -----------------------
# Data ingestion
# -----------------------
df_data = pd.read_csv('dataset/cleaned_data.csv', index_col=0)
mean_lat = df_data['LATITUDE'].mean()
mean_long = df_data['LONGITUDE'].mean()

# Conversão e tratamento de dados
df_data['size_m2'] = df_data['GROSS SQUARE FEET'] / 10.764
df_data = df_data[df_data['YEAR BUILT'] > 0]
df_data['SALE DATE'] = pd.to_datetime(df_data['SALE DATE'])
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap as dbc
import pandas as pd\
import plotly

from app import app
from _map import *
from _histogram import *
from _controllers import *

# -----------------------
# Data ingestion
# -----------------------
df_data = pd.read_csv('dataset/cleaned_data.csv', index_col=0)
mean_lat = df_data['LATITUDE'].mean()
mean_long = df_data['LONGITUDE'].mean()

df_data['size_m2'] = df_data['GROSS SQUARE FEET'] / 10.764
df_data = df_data[df_data['YEAR BUILT'] > 0]
df_data['SALE DATE'] = pd.to_datetime(df_data['SALE DATE'])

df_data.loc[df_data['size_m2'] > 10000, 'size_m2'] = 10000
df_data.loc[df_data['SALE PRICE'] > 50000000, 'SALE PRICE'] = 50000000

df_data.loc[df_data['SALE PRICE'] < 100000, 'SALE PRICE'] = 100000

# -----------------------
# Layout
# -----------------------
app.layout = dbc.Container(
        children=[
                dbc.Row([
                        dbc.Col([controllers], md=3),
                        dbc.Col([map, his])
                ])
        ] fluid=True,
)

# -----------------------
# Callbacks
# -----------------------

def update_hist(location, square_size, color_map):
        if location is None:
                df_intermediate = df_data.copy()
        else:
                df_intermediate = df_data[df_data['BOROUGH'] == location] if location != 0 else df_data,
                size_limit = slider_size[square_size] if square_size is not None else df_data ['GROSS SQUARE FEET'],
                df_intermediate = df_intermediate[df_intermediate['GROOS SQUARE FEET'] <= size_limit]

hist_fig = px.histogram(df_intermediate, x=color_map)
hist_layout = go.Layout(
        margin=go.layout.Margin(l=10, r=0, t=0, b=50),
        showlegend=False,
        template='plotly_dark,
        paper_bgcolor='rgba(0,0,0,0)'
)
hist_fig.layout = hist_layout

px.set_mapbox_access_token(open('keys/mapbox_key').read())
map_fig = px.scatter_mapbox(df_intermediate, lat='LATITUDE', lon='LONGITUDE',
        color=color_map, size='size_m2', size_max=15, zoom=10, opacity=0.4)
return hist_fig

if __name__ == '__main__':
  app.run_server(debug = True, port = '8051')
  # app.run_server(host = '0.0.0.0', port = '8050)


# Limites para visualização
df_data.loc[df_data['size_m2'] > 10000, 'size_m2'] = 10000
df_data.loc[df_data['SALE PRICE'] > 50000000, 'SALE PRICE'] = 50000000
df_data.loc[df_data['SALE PRICE'] < 100000, 'SALE PRICE'] = 100000

# -----------------------
# Layout
# -----------------------
app.layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([controllers], md=3),
            dbc.Col([map, his])
        ])
    ],
    fluid=True,
)

# -----------------------
# Callbacks
# -----------------------

# Tabela de limites para os tamanhos, pode ser adaptada conforme necessidade
slider_size = {
    'Pequeno': 500,
    'Médio': 2000,
    'Grande': 10000
}

@app.callback(
    Output('histogram', 'figure'),
    Input('location-dropdown', 'value'),
    Input('size-radio', 'value'),
    Input('color-dropdown', 'value')
)
def update_hist(location, square_size, color_map):
    # Filtragem dos dados
    if location is None or location == 0:
        df_intermediate = df_data.copy()
    else:
        df_intermediate = df_data[df_data['BOROUGH'] == location]

    if square_size is not None and square_size in slider_size:
        size_limit = slider_size[square_size]
        df_intermediate = df_intermediate[df_intermediate['GROSS SQUARE FEET'] <= size_limit]

    # Criação do histograma
    hist_fig = px.histogram(df_intermediate, x=color_map)
    hist_fig.update_layout(
        margin=go.layout.Margin(l=10, r=0, t=0, b=50),
        showlegend=False,
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return hist_fig

# (Opcional) Callback para o mapa se também for interativo:
# @app.callback(...)
# def update_map(...):
#     ...

# -----------------------
# Executar servidor
# -----------------------
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
    # app.run_server(host='0.0.0.0', port=8050)
