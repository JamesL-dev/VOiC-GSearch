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
        external_stylesheets=[{
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
        children = [
            html.H1(children = "gSearch!",
            className="header-title",
                    ),
            html.P(
                children="Build a premise graph and search the VOiC database.",
                ),
            ],
            className="header",
        )
#####################################################
# Display page
#####################################################

def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()

