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
                            dash.html.H5([
                                "Length of residence in ",
                                dash.html.Span(id="state_case_file_0")
                                
                            ]),
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
                                placeholder='Enter State',
                                type='text',
                                value='{state}',
                                id = 'state_case_value',
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
                            dcc.Dropdown({1: "Home State Jurisdiction", 2: "Blahblah", 3: "third option", 4: "fourth option"}, id='jurisdiction_options'),
                            html.Div(id='dd-output-container1'),
                        ]
                        ),
                        dbc.Col([
                        ],
                        ),
                    ],
                    ),

                # line break
                dash.html.Br(),
                dash.html.Div([
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"a. {claimant_current_residence} is home state", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                # line break
                dash.html.B("OR", style={"margin-left":40}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"b. {claimant_current_residence} is previous home state", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"i. Within six months of {current_date}", style={"margin-left":70}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                dash.html.B("AND", style={"margin-left":80}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"ii. {child_name} is absent from {claimant_current_residence}", style={"margin-left":70}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                dash.html.B("AND", style={"margin-left":80}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"iii. {claimant_name} lives in {claimant_current_residence}", style={"margin-left":70}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                ],id="options1", hidden=True),

                ],
                className="container-fluid border"
            ),   
            dash.html.Br(),
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

# This is for hidden dropdown options for jurisdtiction
@app.callback(
    dash.Output('options1', 'hidden'),
#    dash.Output('options2', 'hidden'),
#    dash.Output('options3', 'hidden'),
#    dash.Output('options4', 'hidden'),
    dash.Input('jurisdiction_options', 'value')
 )
def update_output(value):
    print(type(value))
    # return (value != "1"),(value != "2"),(value != "3"),(value != "4")
    return (value != "1")

# This is for State filed
@app.callback(
    dash.Output('state_case_file_0', 'children'),
    dash.Input('state_case_value', 'value'),
)
def update_state_case_location(state_case_value):
    return state_case_value

def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

