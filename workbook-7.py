#!/usr/bin/env python
# coding: utf-8

# In[114]:


import pandas as pd 
import plotly.graph_objs as go 


# In[115]:


from chart_studio import plotly


# In[116]:


from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot


# In[117]:


init_notebook_mode(connected = True)


# In[118]:


data = dict(type = "choropleth",
            locations = ["AZ", "GA", "NY"], 
            locationmode = "USA-states", 
            colorscale = "Jet",
           text = ["text 1", "text 2", "text 3"], 
           z = [1.0,2.0,3.0], 
           colorbar = {"title": "Colorbar Title Goes Here"})


# In[119]:


layout = dict(geo = {"scope" : "usa"})


# In[120]:


choromap = go.Figure(data = [data], layout = layout)


# In[121]:


iplot(choromap)


# In[122]:


df = pd.read_csv("2011_US_AGRI_Exports")


# In[123]:


df.head()


# In[124]:


data = dict(type = "choropleth",
            locations = df["code"], 
            locationmode = "USA-states", 
            colorscale = "YIOrRd",
           text = df["text"], 
           z = df["total exports"], 
           colorbar = {"title": "Millions USD"},
           marker = dict(line = dict(color = "rgb(255,255,255)", width = 2)))


# In[125]:


layout = dict(title = "2011 US Agriculture Exports by State", \
              geo = dict(scope = "usa", showlakes = True, lakecolor = "rgb(85,173,240)" ))


# In[ ]:




