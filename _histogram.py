from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# Figura inicial vazia para o histograma
fig = go.Figure()

fig.update_layout(
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Componente do histograma
his = dbc.Row(
    [
        dcc.Graph(id='histogram', figure=fig)
    ],
    style={'height': '40vh'}
)
