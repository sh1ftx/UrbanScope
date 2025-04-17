from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

# Dicionário com os distritos
list_of_locations = {
    'Todos': 0,
    'Manhattan': 1,
    'Bronx': 2,
    'Brooklyn': 3,
    'Queens': 4,
    'Staten Island': 5,
}

# Faixas de tamanho para o slider (em m²)
slider_size = [100, 500, 1000, 10000, 10000000]

controllers = html.Div([
    # Logo
    html.Img(id='logo', src=app.get_asset_url('tubrao.jpg'), style={'width': '50%'}),

    # Título e descrição
    html.H3('Vendas de imóveis - NYC', style={'margin-top': '30px'}),
    html.P('''
        Utilize este dashboard para analisar vendas ocorridas na cidade de New York no período de 1 ano.
    '''),

    # Dropdown de localização
    html.H4('Distrito', style={'margin-top': '50px', 'margin-bottom': '25px'}),
    dcc.Dropdown(
        id='location-dropdown',
        options=[{'label': i, 'value': j} for i, j in list_of_locations.items()],
        value=0,
        placeholder='Selecione um distrito'
    ),

    # Slider de metragem
    html.H4('Metragem (m²)', style={'margin-top': '40px', 'margin-bottom': '10px'}),
    dcc.Slider(
        id='size-radio',  # Corrigido para coincidir com o ID usado no callback
        min=0,
        max=2,
        step=1,
        marks={0: 'Pequeno', 1: 'Médio', 2: 'Grande'},
        value=1
    ),

    # Dropdown para escolha da variável de cor no gráfico
    html.H4('Variável para colorir', style={'margin-top': '40px', 'margin-bottom': '10px'}),
    dcc.Dropdown(
        id='color-dropdown',
        options=[
            {'label': 'Preço de Venda', 'value': 'SALE PRICE'},
            {'label': 'Ano de Construção', 'value': 'YEAR BUILT'},
            {'label': 'Tamanho (m²)', 'value': 'size_m2'}
        ],
        value='SALE PRICE',
        placeholder='Escolha uma variável'
    )
])
