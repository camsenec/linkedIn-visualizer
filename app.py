import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import visualizer

# Initiate Application Instance
app = dash.Dash(__name__)
app.title = "LinkedIn Visualizer"

server = app.server

# HTML document that is initially displayed, which consists of a title area and an input form)
app.layout = html.Div(children=[ 
    # title area
    html.Div(
          children=[
              html.H1(
                  children="LinkedIn Visualizer", className="header-title"
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

    html.Div(
          children=[
              html.H2(
                  children="Select graphs you want to see and upload a file", className="instruction"
              ),
          ]
    ),

    dcc.Checklist(
    id = 'checklist',
    options=[
        {'label': 'Change of your number of Connections (Plot)', 'value': 'trend'},
        {'label': 'Distribution of companies your connected people work (Histgram)', 'value': 'company_hist'},
        {'label': 'Distribution of job positions your connected people (Histgram)', 'value': 'position_hist'},
        {'label': 'Companies where your connected people work (Treemap)', 'value': 'company_treemap'},
        {'label': 'Job positions of your connected people (Treemap)', 'value': 'position_treemap'},
        {'label': 'Job positions of your connected people for each company (Hybrid Treemap)', 'value': 'company_position_treemap'},
        {'label': 'Companies where your connected people work for each job position (Hybrid Treemap)', 'value': 'position_company_treemap'}
    ],
    value = ['trend', 'company_hist', 'position_hist', 'company_position_treemap'],
    labelStyle={'display': 'block'},
    style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '30px',
            'marginTop' : '30px',
            'paddingBottom' : '150px',
            'textAlign': 'center',
        },
    ),
    # a hidden html element
    html.Div(id='output-data-upload'),
])


# call back function, which receive csv file as `Input` and have two states namely filename and last_modified and replace the HTML element id=`output-data-upload` with returned value.
# i.e. children = [`the returned value by the function parse_contents`] are retuned by update_output and displayed at the place with `html.Div(id='output-data-upload)`  
@app.callback(Output('output-data-upload', 'children'),
              Input('checklist', 'value'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(values, contents, filename):
    #print("called")
    if contents is not None:
        children = [
            visualizer.parse_contents(values, c, f) for c, f in zip(contents, filename) 
        ]
        return children


# main function
if __name__ == "__main__":
  app.run_server(debug=True, use_reloader=True)
