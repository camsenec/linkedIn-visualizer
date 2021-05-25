import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import graphs
import base64
import io


def parse_contents(vizualize_list, contents, filename):
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
    
    #HTML component for each graph defined in graphs.py 
    trend_html = html.Div(
                    children=dcc.Graph(
                      figure=graphs.trend(connections_df)
                    ),
                    className="card",
                )
    company_hist_html = html.Div(
                    children=dcc.Graph(
                        figure=graphs.company_hist(connections_df)
                    ),
                    className="card",
                )
    position_hist_html = html.Div(
                    children=dcc.Graph(
                        figure=graphs.position_hist(connections_df)
                    ),
                    className="card",
                )

    company_treemap_html = html.Div(
                    children=dcc.Graph(
                        figure=graphs.company_treemap(connections_df)
                    ),
                    className="card",
                )
    position_treemap_html = html.Div(
                    children=dcc.Graph(
                        figure=graphs.position_treemap(connections_df)
                    ),
                    className="card",
                )
    company_position_treemap_html = html.Div(
                    children=dcc.Graph(
                        figure=graphs.company_position_treemap(connections_df)
                    ),
                    className="card",
                )

    position_company_treemap_html = html.Div(
                    children=dcc.Graph(
                        figure=graphs.position_company_treemap(connections_df)
                    ),
                    className="card",
    )

    graphs_html_map = {"trend": trend_html, 
                   "company_hist": company_hist_html,
                   "position_hist": position_hist_html,
                   "company_treemap": company_treemap_html, 
                   "position_treemap": position_treemap_html,
                   "company_position_treemap": company_position_treemap_html,
                   "position_company_treemap": position_company_treemap_html}
    
    graphs_html_list = []
    for graph_name in graphs_html_map:
        if graph_name in vizualize_list:
            graphs_html_list.append(graphs_html_map[graph_name])

    return html.Div(
    children=[
        html.Div(
            children=graphs_html_list,
            className="wrapper",
        ),
    ]
)

