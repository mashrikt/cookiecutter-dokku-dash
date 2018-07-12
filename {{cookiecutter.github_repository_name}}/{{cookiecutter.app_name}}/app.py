import dash
import dash_html_components as html
from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    # Title - Row
    html.Div(
        [
            html.H1(
                '{{cookiecutter.app_name}}',
                style={
                    'font-family': 'Helvetica',
                    "margin-top": "25",
                    "margin-bottom": "25"
                },
                className='eight columns',
            ),
            html.H1(
                id='month-year-label',
                style={
                    'font-family': 'Helvetica',
                    "margin-top": "25",
                    "margin-bottom": "25",
                    "text-align": "right"
                },
                className='four columns',
            ),
        ],
        className='row'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
