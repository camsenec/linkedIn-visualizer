import plotly.graph_objects as go 
import plotly.express as px
import datetime

# Changes of the number of connections
def trend(connections_df):
    format_cand = ["%d %b %y", "%d %b %Y", "%d-%b-%y", "%d-%b-%Y"]
    for i, format in enumerate(format_cand):
        try:
            connections_df["Connected On"] = connections_df["Connected On"].apply(
                lambda x: datetime.datetime.strptime(x, format).strftime("%Y-%m-%d"))
        except:
            if i == len(format_cand) - 1:
                print("Datetime format error")
            continue
        else:
            break
    
    df = connections_df.groupby(by="Connected On").count().reset_index()
    df["count"] = 0
    for i, index in enumerate(df.index):
        if i == df.index[0]:
            df.loc[index,"count"] = df.loc[index,"First Name"]
        else:
            df.loc[index,"count"] = df.iloc[i-1]["count"] + df.loc[index,"First Name"]
            

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Connected On"], 
                        y=df["count"]))
    fig.update_layout(title='Changes of your number of Connections',
                    xaxis_title='Connected On',
                    yaxis_title='Number')
    return fig

# Distribution of companies connected people work at
def company_hist(connections_df):
    #connections_df = connections_df.dropna(subset=['Position', 'Company'])
    fig  = px.histogram(connections_df, x = "Company")
    fig.update_layout(title='Distribution of companies your connected people work')
    return fig

def position_hist(connections_df):
    #connections_df = connections_df.dropna(subset=['Position', 'Company'])
    fig  = px.histogram(connections_df, x = "Position").update_xaxes(categoryorder="total descending")
    fig.update_layout(title='Distribution of job positions of your connected people')
    return fig

# Companies where connected people work
def company_treemap(connections_df):
    connections_df['Company'] = connections_df['Company'].fillna("Other")
    connections_df['Position'] = connections_df['Position'].fillna("other")
    #connections_df = connections_df.dropna(subset=['Position', 'Company'])
    connections_df["CompanyCount"] = 1
    connections_df["Name"] = connections_df["First Name"] + " " + connections_df["Last Name"]
    fig = px.treemap(connections_df, path=['Company', "Last Name"],
                    values="CompanyCount",
                    )
    fig.update_layout(title='Companies where your connected people work')
    return fig

# Job Positions of connected people
def position_treemap(connections_df):
    #connections_df = connections_df.dropna(subset=['Position', 'Company'])
    connections_df['Company'] = connections_df['Company'].fillna("Other")
    connections_df['Position'] = connections_df['Position'].fillna("Other")
    connections_df["PositionCount"] = 1
    connections_df["Name"] = connections_df["First Name"] + " " + connections_df["Last Name"]
    fig = px.treemap(connections_df, path=["Position", "Name"], 
                    values="PositionCount",
                    )
    fig.update_layout(title='Job positions of your connected people') 
    return fig

def company_position_treemap(connections_df):
    #connections_df = connections_df.dropna(subset=['Position', 'Company'])
    connections_df['Company'] = connections_df['Company'].fillna("Other")
    connections_df['Position'] = connections_df['Position'].fillna("Other")
    connections_df["PositionCount"] = 1
    connections_df["Name"] = connections_df["First Name"] + " " + connections_df["Last Name"]
    fig = px.treemap(connections_df, path=['Company', 'Position', 'Name'], 
                    values="PositionCount",
                    )
    fig.update_layout(title='Companies where your connected people work for each job position')
    return fig

def position_company_treemap(connections_df):
    #connections_df = connections_df.dropna(subset=['Position', 'Company'])
    connections_df['Company'] = connections_df['Company'].fillna("Other")
    connections_df['Position'] = connections_df['Position'].fillna("Other")
    connections_df["PositionCount"] = 1
    connections_df["Name"] = connections_df["First Name"] + " " + connections_df["Last Name"]
    fig = px.treemap(connections_df, path=['Position', "Company", "Name"], 
                    values="PositionCount",
                    )
    fig.update_layout(title='Job positions of your connected people for each company')
    return fig