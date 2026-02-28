from dash import Dash, html, dcc
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Button('Submit', id='numbers'),
    dcc.Input(
        placeholder="Enter a valid number",
        id='Data',
        type='number'
    ),
    html.H1(id='Results')
])

@app.callback(
    Output('Results', 'children'),
    Input('numbers', 'n_clicks'),
    Input('Data', 'value')
)
def play_data(n, data):
    if n is not None and data is not None:
        return f"You entered: {data}"
    return ""

app.run(debug=True)
