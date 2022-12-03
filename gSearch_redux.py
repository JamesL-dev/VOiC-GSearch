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

# Import lorem ipsum for filler text
import lorem
lorem_sentence = lorem.sentence()

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
                                placeholder='Enter todays date',
                                type='text',
                                value='',
                                id = 'current_date_value',
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
                                dash.html.Span(id="state_case_file_0"),
                                " on ",
                                dash.html.Span(id="date_case_filed_0"),
                            ]),
                            dcc.Input(
                                placeholder='Enter number of days',
                                type='text',
                                value='',
                                id='length_of_residence_in_case_and_file_date',
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
                                placeholder='Enter child name',
                                type='text',
                                value='',
                                id='child_name_value',
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
                                value='',
                                id='current_residence_state_value'
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
                                placeholder='Enter a name',
                                type='text',
                                value='',
                                id='claimant_name_value',
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
                                dash.html.Span(id="current_residence_state_0"),
                                " on ",
                                # Current date
                                dash.html.Span(id="current_date_0"),
                                ],
                            ),
                            dcc.Input(
                                placeholder='Enter number of days',
                                type='text',
                                value='',
                                id='length_of_residence_respondent_value'
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
                                placeholder='Enter a name',
                                type='text',
                                value='',
                                id='respondent_name_value'
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5([
                                dash.html.Span(id="claimant_name_0"),
                                " residence: ",
                                ],
                            ),
                            dcc.Input(
                                placeholder='Enter a state',
                                type='text',
                                value='',
                                id='claimant_residence_state_value',
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
                                placeholder='Enter a date',
                                type='text',
                                value='',
                                id='date_case_filed_value',
                            ),
                        ],
                        className="input_component",
                        ),

                    ),
                    dbc.Col(
                        dash.html.Div(
                        [
                            dash.html.H5([
                                dash.html.Span(id="respondent_name_0"),
                                " residence: "
                                ], 
                            ),
                            dcc.Input(
                                placeholder='Enter a state',
                                type='text',
                                value='',
                                id='respondent_residence_state_value',
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
                                value='',
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
                                value='',
                                id='most_recent_determination_value',
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
                            dcc.Dropdown({1: "Home State Jurisdiction", 2: "Exclusive continued jurisdiction", 3: "Michigan having initial modification jurisdiction determined Virginia", 4: "No court has jurisdiction subdivision 1, 2, or 3"}, id='jurisdiction_options'),
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

                dash.html.Div([
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"a. Mississippi has exclusive, continued jurisdiction", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                # line break
                dash.html.B("AND", style={"margin-left":40}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"b. Mississippi declined jurisdiction in favor of Virginia", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                    dash.html.B("AND", style={"margin-left":40}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"c. Fiia and Abebi have significant connection", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                dash.html.B("AND", style={"margin-left":40}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"d. Substantial evidence present in Virginia", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                ],id="options2", hidden=True),

                dash.html.Div([
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
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
                            dash.html.P(f"b. {claimant_current_residence} {lorem_sentence}", style={"margin-left":30}),
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
                            dash.html.P(f"i. {lorem_sentence} {current_date}", style={"margin-left":70}),
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
                            dash.html.P(f"ii. {child_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
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
                            dash.html.P(f"iii. {claimant_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                ],id="options3", hidden=True),

                dash.html.Div([
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                # line break
                dash.html.B("AND", style={"margin-left":40}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"b. {lorem_sentence}", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                    dash.html.B("AND", style={"margin-left":40}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"c. {lorem_sentence}", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                dash.html.B("AND", style={"margin-left":40}),
                    dbc.Row([
                        dbc.Col([
                            dash.html.P(f"d. {lorem_sentence}", style={"margin-left":30}),
                        ]
                        ),
                        dbc.Col([
                            dcc.RadioItems(['True', 'False','Override'], 'False'),
                        ],
                        ),
                    ]
                    ),

                ],id="options4", hidden=True),

                ],
                className="container-fluid border"
            ),   

            dash.html.Div([
                dash.html.Div(
                    dash.html.H5("OR")
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
                        dcc.Dropdown({1: "Home State Jurisdiction", 2: "Exclusive continued jurisdiction", 3: "Michigan having initial modification jurisdiction determined Virginia", 4: "No court has jurisdiction subdivision 1, 2, or 3"}, id='jurisdiction_options_2'),
                        html.Div(id='dd-output-container2'),
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

            ],id="options5", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. Mississippi has exclusive, continued jurisdiction", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            # line break
            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"b. Mississippi declined jurisdiction in favor of Virginia", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

                dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"c. Fiia and Abebi have significant connection", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"d. Substantial evidence present in Virginia", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options6", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
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
                        dash.html.P(f"b. {claimant_current_residence} {lorem_sentence}", style={"margin-left":30}),
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
                        dash.html.P(f"i. {lorem_sentence} {current_date}", style={"margin-left":70}),
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
                        dash.html.P(f"ii. {child_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
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
                        dash.html.P(f"iii. {claimant_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options7", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            # line break
            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"b. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

                dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"c. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"d. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options8", hidden=True),

            ],
            className="container-fluid border"
        ),   

            dash.html.Div([
                dash.html.Div(
                    dash.html.H5("OR")
                    ),
                ],
            className="container-fluid border"
            ),

            dash.html.Div([
            # line break
            dash.html.Br(),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown({1: "Home State Jurisdiction", 2: "Exclusive continued jurisdiction", 3: "Michigan having initial modification jurisdiction determined Virginia", 4: "No court has jurisdiction subdivision 1, 2, or 3"}, id='jurisdiction_options_3'),
                        html.Div(id='dd-output-container3'),
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

            ],id="options9", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. Mississippi has exclusive, continued jurisdiction", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            # line break
            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"b. Mississippi declined jurisdiction in favor of Virginia", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

                dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"c. Fiia and Abebi have significant connection", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"d. Substantial evidence present in Virginia", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options10", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
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
                        dash.html.P(f"b. {claimant_current_residence} {lorem_sentence}", style={"margin-left":30}),
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
                        dash.html.P(f"i. {lorem_sentence} {current_date}", style={"margin-left":70}),
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
                        dash.html.P(f"ii. {child_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
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
                        dash.html.P(f"iii. {claimant_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options11", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            # line break
            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"b. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

                dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"c. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"d. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options12", hidden=True),

            ],
            className="container-fluid border"
        ),   

            dash.html.Div([
                dash.html.Div(
                    dash.html.H5("OR")
                    ),
                ],
            className="container-fluid border"
            ),

            dash.html.Div([
            # line break
            dash.html.Br(),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown({1: "Home State Jurisdiction", 2: "Exclusive continued jurisdiction", 3: "Michigan having initial modification jurisdiction determined Virginia", 4: "No court has jurisdiction subdivision 1, 2, or 3"}, id='jurisdiction_options_4'),
                        html.Div(id='dd-output-container4'),
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

            ],id="options13", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. Mississippi has exclusive, continued jurisdiction", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            # line break
            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"b. Mississippi declined jurisdiction in favor of Virginia", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

                dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"c. Fiia and Abebi have significant connection", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"d. Substantial evidence present in Virginia", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options14", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
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
                        dash.html.P(f"b. {claimant_current_residence} {lorem_sentence}", style={"margin-left":30}),
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
                        dash.html.P(f"i. {lorem_sentence} {current_date}", style={"margin-left":70}),
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
                        dash.html.P(f"ii. {child_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
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
                        dash.html.P(f"iii. {claimant_name} {lorem_sentence} {claimant_current_residence}", style={"margin-left":70}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options15", hidden=True),

            dash.html.Div([
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"a. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            # line break
            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"b. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

                dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"c. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            dash.html.B("AND", style={"margin-left":40}),
                dbc.Row([
                    dbc.Col([
                        dash.html.P(f"d. {lorem_sentence}", style={"margin-left":30}),
                    ]
                    ),
                    dbc.Col([
                        dcc.RadioItems(['True', 'False','Override'], 'False'),
                    ],
                    ),
                ]
                ),

            ],id="options16", hidden=True),

            ],
            className="container-fluid border"
        ),   

            dash.html.Div([
                dash.html.Div(
                    dash.html.H5("OR")
                    ),
                ],
            className="container-fluid border"
            ),

            
            dbc.Row([
                dash.html.Div([
                    html.Button('Submit', id='btn-nclicks-1', n_clicks=0, className='btn-primary'),
                ],
                className="",
                ),
            ],
            ),
            dash.html.Br(),
            ],
            className="container border",
            ),
        ],
)

#####################################################
# Callbacks for dynamic input
#####################################################

# This is for hidden dropdown options for jurisdtiction 1
@app.callback(
    dash.Output('options1', 'hidden'),
    dash.Output('options2', 'hidden'),
    dash.Output('options3', 'hidden'),
    dash.Output('options4', 'hidden'),
    dash.Input('jurisdiction_options', 'value')
 )
def update_output(value):
    return (value != "1"),(value != "2"),(value != "3"),(value != "4")

# This is for hidden dropdown options for jurisdtiction options 2
@app.callback(
    dash.Output('options5', 'hidden'),
    dash.Output('options6', 'hidden'),
    dash.Output('options7', 'hidden'),
    dash.Output('options8', 'hidden'),
    dash.Input('jurisdiction_options_2', 'value')
 )
def update_output(value):
    return (value != "1"),(value != "2"),(value != "3"),(value != "4")

# This is for hidden dropdown options for jurisdtiction options 3
@app.callback(
    dash.Output('options9', 'hidden'),
    dash.Output('options10', 'hidden'),
    dash.Output('options11', 'hidden'),
    dash.Output('options12', 'hidden'),
    dash.Input('jurisdiction_options_3', 'value')
 )
def update_output(value):
    return (value != "1"),(value != "2"),(value != "3"),(value != "4")

# This is for hidden dropdown options for jurisdtiction options 4
@app.callback(
    dash.Output('options13', 'hidden'),
    dash.Output('options14', 'hidden'),
    dash.Output('options15', 'hidden'),
    dash.Output('options16', 'hidden'),
    dash.Input('jurisdiction_options_4', 'value')
 )
def update_output(value):
    return (value != "1"),(value != "2"),(value != "3"),(value != "4")

# Todays date
@app.callback(
    dash.Output('current_date_0', 'children'),
    dash.Input('current_date_value', 'value'),
)
def update_todays_date(current_date_value):
    return current_date_value

# Childs Name
@app.callback(
    dash.Output('child_name_0', 'children'),
    dash.Input('child_name_value', 'value'),
)
def update_child_name(child_name_value):
    return child_name_value

# Parent1 / Claimant name
@app.callback(
    dash.Output('claimant_name_0', 'children'),
    dash.Input('claimant_name_value', 'value'),
)
def update_claimant_name(claimant_name_value):
    return claimant_name_value

# Parent2 / Respondent Name
@app.callback(
    dash.Output('respondent_name_0', 'children'),
    dash.Input('respondent_name_value', 'value'),
)
def update_respondent_name(respondent_name_value):
    return respondent_name_value

# Date case filed
@app.callback(
    dash.Output('date_case_filed_0', 'children'),
    dash.Input('date_case_filed_value', 'value'),
)
def update_date_case_filed(date_case_filed_value):
    return date_case_filed_value

# State case filed
@app.callback(
    dash.Output('state_case_file_0', 'children'),
    dash.Input('state_case_value', 'value'),
)
def update_state_case_location(state_case_value):
    return state_case_value

# Length of residence in {state}
@app.callback(
    dash.Output('length_of_residence_in_state_0', 'children'),
    dash.Input('length_of_residence_in_state_value', 'value'),
)
def update_length_of_residence_in_state(length_of_residence_in_state_value):
    return length_of_residence_in_state_value

# Current residence state
@app.callback(
    dash.Output('current_residence_state_0', 'children'),
    dash.Input('current_residence_state_value', 'value'),
)
def update_current_residence_state(current_residence_state_value):
    return current_residence_state_value

# Length of residence in {case state} on {case filed date}
@app.callback(
    dash.Output('length_of_residence_in_case_and_file_date_0', 'children'),
    dash.Input('length_of_residence_in_case_and_file_date_value', 'value'),
)
def update_length_of_residence_respondent(length_of_residence_in_case_and_file_date_value):
    return length_of_residence_in_case_and_file_date_value

# current residence state

# Claimant residence state
@app.callback(
    dash.Output('claimant_residence_state_0', 'children'),
    dash.Input('claimant_residence_state_value', 'value'),
)
def update_claimant_residence_state(claimant_residence_state_value):
    return claimant_residence_state_value

# Respondent residence state
@app.callback(
    dash.Output('respondent_residence_state_0', 'children'),
    dash.Input('respondent_residence_state_value', 'value'),
)
def update_claimant_residence_state(respondent_residence_state_value):
    return respondent_residence_state_value

#most recent determination/modification by state
@app.callback(
    dash.Output('most_recent_determ_mod_state_0', 'children'),
    dash.Input('most_recent_determ_mod_state_value', 'value'),
)
def update_recent_determ_mod(most_recent_determ_mod_state_value):
    return most_recent_determ_mod_state_value

# Boilerplate to run app, debug true if you want to refresh in real time for testing
def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

