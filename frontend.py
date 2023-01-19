# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:50:36 2023

@author: gabba
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

app = dash.Dash()
symbol = 'TSLA'

app.layout = html.Div([
    html.H1(f'Current value of {symbol}'),
    html.Div(id='current_value'),
    html.Br(),
    html.Label('Start Date (YYYY-MM-DD)'),
    dcc.Input(id='start_date', type='text', value=''),
    html.Br(),
    html.Label('End Date (YYYY-MM-DD)'),
    dcc.Input(id='end_date', type='text', value=''),
    html.Br(),
    html.Button('Submit', id='button'),
    html.Br(),
    dcc.Graph(id='historical_values')
])

@app.callback(
    Output('current_value', 'children'),
    [Input('button', 'n_clicks')],
    [State('start_date', 'value'),
     State('end_date', 'value')])
def update_current_value(n_clicks, start_date, end_date):
    # call the function get_current_value from backend_script
    current_value = get_current_value()
    return current_value

@app.callback(
    Output('historical_values', 'figure'),
    [Input('button', 'n_clicks')],
    [State('start_date', 'value'),
     State('end_date', 'value')])
def update_graph(n_clicks, start_date, end_date):
    # call the function get_historical_values from backend_script
    historical_values = get_historical_values(start_date, end_date)
    data = [go.Scatter(x=[i['date'] for i in historical_values], y=[i['value'] for i in historical_values])]
    return {'data': data}

if __name__ == '__main__':
    start_date, end_date = get_default_timerange()
    app.run_server(debug=True)

