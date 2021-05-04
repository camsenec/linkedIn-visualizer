import plotly.graph_objects as go 
import plotly.express as px
import datetime

# Changes of the number of connections
def trend(connections_df):
    format_cand = ["%d %b %y", "%d %b %Y", "%d-%b-%y", "%d-%b-%Y"]
    for format in format_cand:
        try:
            connections_df["Connected On"] = connections_df["Connected On"].apply(lambda x: datetime.datetime.strptime(x, format).strftime("%Y-%m-%d"))
        except:
            print("errror")
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
    fig  = px.histogram(connections_df, x = "Company")
    fig.update_layout(title='Distribution of companies your connected people work')
    return fig

# Companies where connected people work
def company_treemap(connections_df):
    df_by_company = connections_df.groupby(by="Company").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
    company_treemap = px.treemap(df_by_company[:100], path=["Company"],
                    values="First Name",
                    labels={"First Name": "Count"})
    company_treemap.update_layout(title='Companies where your connected people work')
    return company_treemap

# Job Positions of connected people
def position_treemap(connections_df):
    df_by_position = connections_df.groupby(by="Position").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
    position_treemap = px.treemap(df_by_position[:100], path=["Position"],
                    values="First Name",
                    labels={"First Name": "Count"})
    position_treemap.update_layout(title='Job Positions of your connected people') 
    return position_treemap