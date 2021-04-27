import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import datetime
import graphs

import base64
import datetime
import io


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            connections_df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            connections_df["Connected On"] = connections_df["Connected On"].apply(lambda x: datetime.datetime.strptime(x, "%d-%b-%y").strftime("%Y-%m-%d"))
        else:
           return html.Div([
            'This file extension is not supported'
        ])
    except Exception as e:
        print(e)
        print("loglog")
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

