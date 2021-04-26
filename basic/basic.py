#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
import datetime

connections_df = pd.read_csv('../input/sample1/Connections.csv')
connections_df.head(10)

company_groupby = connections_df.groupby("Company").count()
fig  = px.histogram(connections_df, x = "Company"); 
fig.show()


connections_df["Connected On"] = connections_df["Connected On"].apply(lambda x: datetime.datetime.strptime(x, "%d-%b-%y").strftime("%Y-%m-%d"))
connections_line = px.line(connections_df.groupby(by='Connected On').count().reset_index(), 
                           x="Connected On", 
                           y="First Name", 
                           labels={'First Name': 'Number'},
                           title='My Connections Daily Increase')
connections_line.show()

df = connections_df.groupby(by="Connected On").count().reset_index()
df["count"] = 0

for i, index in enumerate(df.index):
    if i == df.index[0]:
        df.loc[index,"count"] = df.loc[index,"First Name"]
    else:
        df.loc[index,"count"] = df.iloc[i-1]["count"] + df.loc[index,"First Name"]
        
        
connections_line = px.line(df,
                           x="Connected On", 
                           y="count", 
                           labels={'count': 'Number'},
                           title='My Connections Changes')
connections_line.show()

df_by_company = connections_df.groupby(by="Company").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
company_treemap = px.treemap(df_by_company[:100], path=["Company"],
                 values="First Name",
                 labels={"First Name": "Count"})
company_treemap.show()

# Group and sort the data by position 
df_by_position = connections_df.groupby(by="Position").count().reset_index().sort_values(by="First Name", ascending=False).reset_index(drop=True)
position_treemap = px.treemap(df_by_position[:100], path=["Position"],
                 values="First Name",
                 labels={"First Name": "Count"})
position_treemap.show()

