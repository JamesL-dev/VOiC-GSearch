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

# TEMPORARY PLACEHOLDER VALUES
residence_date = "05/2005"
current_date = "07/2007"
child_name = "Fiia"
claimant_name = "Abebi"
claimant_current_residence = "Virginia"
respondent_name = "Pierre"
respondent_current_residence = "Michigan"
most_recent_determination = "Mississippi"


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
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "Today's Date:"
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                f"Length of residence in {claimant_current_residence}"
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "Child Name: "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "Current residence State: "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "Parent 1 Name (claimant): "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                f"Length of residence in {respondent_name} on {current_date}"
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "Parent 2 Name (respondent): "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                f"{claimant_name} residence: "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "Date case filed: "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                f"{respondent_name} residence: "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(),
                ],
                ),
                dbc.Row([
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "State case filed: "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5(
                                "Most recent determination/modification by state: "
                            ),
                            dcc.Input(
                                placeholder='Enter a value...',
                                type='text',
                                value=''
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(),
                ],
                ),
                # line Break
                dash.html.Br(),
                dash.html.Div([
                    dcc.Dropdown(['1. 20-146.12, Initial child custody jurisdiction'], '1. 20-146.12. Initial child custody jurisdiction', id='child_jurisdicton'),
                    html.Div(id='dd-output-container10'),
                ],
                className="text-danger",
                ),
                # line break
                dash.html.B("A"),
                dash.html.Div([
                # line break
                dash.html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown2'),
                            html.Div(id='dd-output-container1'),
                        ]
                        ),
                        dbc.Col([
                        ]
                        ),
                    ],
                    ),
                # line break
                dash.html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"a. {claimant_current_residence} is home state"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                # line break
                dash.html.B("OR"),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"b. {claimant_current_residence} is previous home state"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"i. Within six months of {current_date}"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                dash.html.B("AND"),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"ii. {child_name} is absent from {claimant_current_residence}"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                dash.html.B("AND"),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"iii. {claimant_name} lives in {claimant_current_residence}"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                ],
                className="container-fluid border"
            ),   
            dash.html.Br(),
                dash.html.Div([
                # line break
                dash.html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(['1. Home state jurisdiction', '2. Exclusive continued jurisdiction', '3. Michigan having initial modification jurisdiction determined virginia', '4. No court has jurisdiction subdivision 1, 2, or 3'], '1. Home state jurisdiction', id='demo-dropdown50'),
                            html.Div(id='dd-output-container500'),
                        ]),
                        dbc.Col([
                        ]
                        ),
                    ],
                    ),
                # line break
                dash.html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"a. {claimant_current_residence} is home state"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                # line break
                dash.html.B("OR"),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"b. {claimant_current_residence} is previous home state"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"i. Within six months of {current_date}"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                dash.html.B("AND"),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"ii. {child_name} is absent from {claimant_current_residence}"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                dash.html.B("AND"),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"iii. {claimant_name} lives in {claimant_current_residence}"),
                        ]
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                dcc.RadioItems(['True']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['False']),
                                ],
                                className="col-md-auto",
                                ),
                                dbc.Col([
                                dcc.RadioItems(['Override']),
                                ],
                                className="col-md-auto",
                                ),
                            ],
                            className="col-md-auto",
                            ),
                        ]
                        ),
                    ]
                    ),
                ],
                className="container-fluid border"
            ),   
            ],
            className="container border",
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

