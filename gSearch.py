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
from dash import dcc
from dash import html

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
                                        {'data': {'id': 'one', 'label': 'Node 1'}, 'position': {'x': 75, 'y': 75}},
                                        {'data': {'id': 'two', 'label': 'Node 2'}, 'position': {'x': 200, 'y': 200}},
                                        {'data': {'source': 'one', 'target': 'two'}}
                                    ],
                                ),
                            ],
                            ),
                        ],
                        ),
                        dbc.Col(
                        [
                            dash.html.Div(
                            [
                                cyto.Cytoscape(
                                    id='cytoscape_right',
                                    layout={'name': 'preset'},
                                    style={'width': '50%', 'height': '400px'},
                                    elements=[
                                        {'data': {'id': 'one', 'label': 'Node 1'}, 'position': {'x': 75, 'y': 75}},
                                        {'data': {'id': 'two', 'label': 'Node 2'}, 'position': {'x': 200, 'y': 200}},
                                        {'data': {'source': 'one', 'target': 'two'}}
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
                        dbc.Col(dbc.Input(type="search", placeholder="Query Graph")),
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

        ],
)
#####################################################
# Display page
#####################################################

def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

