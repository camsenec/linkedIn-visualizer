import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import graphs
import base64
import io


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            if "Notes:" == decoded.decode('utf-8')[0:6]:
                connections_df = pd.read_csv(io.StringIO(decoded.decode('utf-8').split('\n\n')[1]))
            else:
                connections_df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        else:
           return html.Div([
            'This file extension is not supported'
        ])
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                      figure=graphs.trend(connections_df)
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        figure=graphs.company_hist(connections_df)
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        figure=graphs.company_treemap(connections_df)
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        figure=graphs.position_treemap(connections_df)
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

