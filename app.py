import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import visualizer

# Initiate Application Instance
app = dash.Dash(__name__)
app.title = "LinkedIn Visualizer"

server = app.server

"""
#connections_df = pd.read_csv('../input/sample1/Connections.csv')
#connections_df["Connected On"] = connections_df["Connected On"].apply(lambda x: datetime.datetime.strptime(x, "%d-%b-%y").strftime("%Y-%m-%d"))
"""

# HTML document that is initially displayed, which consists of a title area and an input form)
app.layout = html.Div(children=[ 
    # title area
    html.Div(
          children=[
              html.H1(
                  children="LinkedIn Viisualizer", className="header-title"
              ),
              html.P(
                  children="Analyze your LinkedIn Data",
                  className="header-description",
              ),
          ],
                  className="header",
        ),
    # input form 
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select your Connections.csv')
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
    # a hidden html element
    html.Div(id='output-data-upload'),
])


# call back function, which receive csv file as `Input` and have two states namely filename and last_modified and replace the HTML element id=`output-data-upload` with returned value.
# i.e. children = [`the returned value by the function parse_contents`] are retuned by update_output and displayed at the place with `html.Div(id='output-data-upload)`  
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
