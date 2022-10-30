from pathlib import Path
from filehandler.filehandler import Filehandler
import os

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Read Data
fp = Filehandler('data', 'fetched_data.csv')

# An immutable sequence providing access to the logical ancestors of the path:
# path = Path(__file__).parents[1] / 'data/fetched_data.csv'
# print(path)
df = fp.read_csv_file()

# print(df.info())

app = Dash(__name__)


fig = px.bar(df, x="Date", y="High", color="Volume", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello This is the WIL Project Dash',
            style={'textAlign': 'center'}),
    html.Div(children='''
             '''),


    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
