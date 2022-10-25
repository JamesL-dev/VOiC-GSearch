#####################################################
# File: 
# Description:      
#####################################################



#####################################################
# Imports
#####################################################
# Built-in packages
import sys

# Installed packages
import dash
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import pandas as pd
from dash import dcc
from dash import html

from collections import OrderedDict

# Import pages here


#####################################################
# App Setup
# 
#####################################################
app = dash.Dash(
        __name__,
        title="gSearch: A VOiC extension",
        external_stylesheets=[
            dbc.themes.BOOTSTRAP,
            {
            "rel": "stylesheet",
            },
            ],
            suppress_callback_exceptions=True

)
server = app.server

#####################################################
# Dummy Data table 
# 
#####################################################
data = OrderedDict(
    [
        ("Id", ["1C3DP", "3CPD3", "4AIPC", "1KL2D", "3KLML", "4PDCM"]),
        ("Document", ["ericson_defense", "Rowley_vs_Shmoe", "Kong_vs_Mario", "legalDoc15", "Xfiles", "byLaws4Dummies"]),
        ("Relevance", [32, 20, 90, 8, 40, 88]),
    ]
)

df = pd.DataFrame(
    OrderedDict([(name, col_data * 6) for (name, col_data) in data.items()])
)

#####################################################
# Componenets 
#####################################################
voic_logo = "/assets/globe.png"
#####################################################
# Page Layout
#####################################################
app.layout = html.Div(
        [
            # NavBar
            dbc.Navbar(
                dbc.Container(
                [
                    html.A(
                # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=voic_logo, height="30px")),
                            dbc.Col(dbc.NavbarBrand("Virtual Office In the Cloud", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
                    ),
                        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                        ),
                ]
                ),
                color="dark",
                dark=True,
            ),
            dash.html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                        [
                            dash.html.Div(
                            [
                                cyto.Cytoscape(
                                    id='cytoscape-left',
                                    layout={'name': 'preset'},
                                    style={'width': '50%', 'height': '400px'},
                                    elements=[
                                        {'data': {'id': 'one', 'label': 'Divorce'}, 'position': {'x': 100, 'y': 100}},
                                        {'data': {'id': 'two', 'label': 'children'}, 'position': {'x': 200, 'y': 200}},
                                        {'data': {'id': 'three', 'label': 'drugs'}, 'position': {'x': 0, 'y': 0}},
                                        {'data': {'id': 'four', 'label': 'arrest'}, 'position': {'x': 0, 'y': 100}},
                                        {'data': {'id': 'five', 'label': 'support'}, 'position': {'x': 100, 'y': 0}},
                                        {'data': {'source': 'one', 'target': 'two'}},
                                        {'data': {'source': 'one', 'target': 'three'}},
                                        {'data': {'source': 'one', 'target': 'four'}},
                                        {'data': {'source': 'one', 'target': 'five'}},
                                    ],
                                ),
                            ],
                            ),
                        ],
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(dcc.Dropdown(
                            ['divorce', 'has something', 'has children', 'children', 'alcohol', 'probation', 'annulment', 'arrest', 'has arrest', 'appeal','bail', 'bond', 'felony', 'has felony', 'court', 'drugs', 'has drugs'
                            ,'custody', 'has custody', 'has support'],
                            ['divorce','has children', 'has support','drugs', 'has arrest'], 
                            multi=True,
                            id="queryGraphDropdown",
                            )
                        ),
                        dbc.Col(
                        dbc.Button(
                        "Search", color="primary", className="ms-2", n_clicks=0
                        ),
                        width="auto",
                        ),
                        dbc.Col(""),
                    ],
                    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
                    align="left",
                ),
            ],
            ),
            dash.html.Br(),
            dash.html.Div([
                dbc.Row([
                    dbc.Col(
                        dash.dash_table.DataTable(
                        data=df.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df.columns],
                        page_size=10,
                        ),
                    ),
                    dbc.Col(),
                ]),
            ],
            ),
            dash.html.Br(),

        ],
)
#####################################################
# Display page
#####################################################

#@dash.callback(
#        dash.Output("cytoscape", "children"),
#        dash.State("dropdown", "value"),
#)
#def something(dropdown):
#    do something
#    return something

def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

