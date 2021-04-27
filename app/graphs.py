import plotly.graph_objects as go # or plotly.express as px

def trend(connections_df):
    df = connections_df.groupby(by="Connected On").count().reset_index()
    df["count"] = 0

    for i, index in enumerate(df.index):
        if i == df.index[0]:
            df.loc[index,"count"] = df.loc[index,"First Name"]
        else:
            df.loc[index,"count"] = df.iloc[i-1]["count"] + df.loc[index,"First Name"]
            

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df["Connected On"], 
                        y=df["count"]))
    fig1.update_layout(title='Your Connection Changes',
                    xaxis_title='Connected On',
                    yaxis_title='Number')
    return fig1
