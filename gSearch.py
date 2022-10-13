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
# Page Layout
#####################################################
app.layout = html.Div(
        [
            # Navbar
            dbc.Navbar(
                dbc.Container(
                    #logo Here
                    dash.html.A(
                        dbc.Row(
                            [
                                dbc.Col(dash.html.Img(
                                    src="/assets/globe.png",
                                    alt="VOiC",
                                    className="logo_image",
                                )),
                                dbc.Col(dbc.NavbarBrand(
                                    "Virtual Office in the Cloud",
                                )),
                            ],
                            align="center",
                            className="g-3",
                        ),
                        href="/",
                        className="navbar-brand mr-4" ,
                    ),

                    # Nav Links
                )
            ),
            # Page Title
            dash.html.H2("gSearch!"),

        ],
)
#####################################################
# Display page
#####################################################

def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

