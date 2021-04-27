import plotly.graph_objects as go 
import plotly.express as px

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

def company_hist(connections_df):
    fig  = px.histogram(connections_df, x = "Company");
    return fig

def company_treemap(connections_df):
    df_by_company = connections_df.groupby(by="Company").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
    company_treemap = px.treemap(df_by_company[:100], path=["Company"],
                    values="First Name",
                    labels={"First Name": "Count"})
    return company_treemap

def position_treemap(connections_df):
    df_by_position = connections_df.groupby(by="Position").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
    position_treemap = px.treemap(df_by_position[:100], path=["Position"],
                    values="First Name",
                    labels={"First Name": "Count"})
    return position_treemap