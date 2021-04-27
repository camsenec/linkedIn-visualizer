import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go # or plotly.express as px
import datetime
import graphs

app = dash.Dash(__name__)
app.title = "LinkedIn Visualizer"

connections_df = pd.read_csv('../input/sample1/Connections.csv')
connections_df["Connected On"] = connections_df["Connected On"].apply(lambda x: datetime.datetime.strptime(x, "%d-%b-%y").strftime("%Y-%m-%d"))
connections_df["Company"]

app.layout = html.Div(
    children=[
        
      html.Div(
          children=[
              html.H1(
                  children="LinkedIn Vizualizer", className="header-title"
              ),
              html.P(
                  children="Analyze your LinkedIn Data",
                  className="header-description",
              ),
          ],
                  className="header",
        ),
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

if __name__ == "__main__":
  app.run_server(debug=True, use_reloader=True)