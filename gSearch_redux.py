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
                dbc.Row([
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),    
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),    
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),    
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),    
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),    
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),    
                    dbc.Col(
                        dcc.Input(
                        placeholder='Enter a value...',
                        type='text',
                        value=''
                        )
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown1'),
                        html.Div(id='dd-output-container1'),
                    ]),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'Override'),
                    ]
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown2'),
                        html.Div(id='dd-output-container2'),
                    ]),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'Overrride'),
                    ]
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown3'),
                        html.Div(id='dd-output-container3'),
                    ]),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'True'),
                    ]
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown4'),
                        html.Div(id='dd-output-container4'),
                    ]),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'Override'),
                    ]
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown5'),
                        html.Div(id='dd-output-container5'),
                    ]),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ]
                    ),
                ],
                ),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown6'),
                        html.Div(id='dd-output-container6'),
                    ]),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'Override'),
                    ]
                    ),
                ],
                ),
            ],
            ),
        ],
)
#####################################################
# Display page
#####################################################

#@dash.callback(
#        dash.Output("cytoscape", "children"),
#        dash.State("dropdown", "value"),
#)
#update_nodes(data):
#    if data is None:
#        return no_update
#    else:


def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

