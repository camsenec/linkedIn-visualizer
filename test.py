#!/usr/bin/env python
# coding: utf-8

# In[102]:


import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

network = pd.read_csv('Connections.csv')
network.head(10)


# In[103]:


company_groupby = network.groupby("Company").count()
fig  = px.histogram(network, x = "Company"); fig.show()


# In[104]:


import datetime

def convert(date):
    return datetime.datetime.strptime(date, "%d %b %Y").strftime("%Y-%m-%d")

network["Connected On"] = network["Connected On"].apply(convert)

connections_line = px.line(network.groupby(by='Connected On').count().reset_index(), 
                           x="Connected On", 
                           y="First Name", 
                           labels={'First Name': 'Number'},
                           title='My Connections')
connections_line.show()


# In[105]:


df = network.groupby(by="Connected On").count()
df.reset_index()
df["count"] = 0
df["Connected On"] = df.index


# In[106]:


for i, index in enumerate(df.index):
    if i == df.index[0]:
        df.loc[index,"count"] = df.loc[index,"First Name"]
    else:
        df.loc[index,"count"] = df.iloc[i-1]["count"] + df.loc[index,"First Name"]
        
        
connections_line = px.line(df,
                           x="Connected On", 
                           y="count", 
                           labels={'count': 'Number'},
                           title='My Connections')
connections_line.show()


# In[ ]:




