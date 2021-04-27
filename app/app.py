import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go # or plotly.express as px
import datetime
from dash.dependencies import Input, Output, State
import visualizer

app = dash.Dash(__name__)
app.title = "LinkedIn Visualizer"

connections_df = pd.read_csv('../input/sample1/Connections.csv')
connections_df["Connected On"] = connections_df["Connected On"].apply(lambda x: datetime.datetime.strptime(x, "%d-%b-%y").strftime("%Y-%m-%d"))

app.layout = html.Div(children=[ 
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
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            visualizer.parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == "__main__":
  app.run_server(debug=True, use_reloader=True)