#!/usr/bin/env python
# coding: utf-8

# In[1]:


import altair as alt
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_excel('clean_up_data.xlsx')
data


# In[3]:


data['case_title'].value_counts()


# In[4]:


brush = alt.selection_interval()

scatterplot = alt.Chart(data).mark_point(filled=True).encode(
    x='Population',
    y='Internet users',
    color=alt.condition(brush, "neighborhood", alt.value("lightgray")),
    tooltip=["Country","neighborhood"]
).add_selection(brush
).transform_filter(alt.datum.Population<5000000
).properties(width=200)

bar = alt.Chart(data).mark_bar().encode(
    y="reason",
    x="count()",
    color=alt.Color("reason", legend=None) # Removing the legend here because it is redundant with bar chart axis labels.
).transform_filter(brush
).properties(width=200)


# In[5]:


bar = alt.Chart(data).mark_bar().encode(
    y="reason",
    x="count()",
    color=alt.Color("reason", legend=None) # Removing the legend here because it is redundant with bar chart axis labels.
).properties(width=200)

alt.data_transformers.disable_max_rows()
bar


# In[7]:


tree_data = pd.read_csv('Boston_Tree.csv')
tree_data


# In[8]:


noise_complaints = data[(data['reason']== 'Noise Disturbance')]
noise_complaints              


# In[14]:


tree = pd.read_csv('Boston_Tree.csv')
tree


# In[10]:


tree_points = alt.Chart(tree_data).mark_point(fill = 'green', size =.001).encode(latitude = 'Y', longitude = 'X')
tree_points


# In[11]:


noise_complaints_points = alt.Chart(noise_complaints).mark_point(fill = 'orange', size =40).encode(latitude = 'latitude', longitude = 'longitude', size=alt.value(20),tooltip=['count()','neighborhood'])
noise_complaints_points


# In[12]:


boston_url = "https://raw.githubusercontent.com/lsouth/DS4200/main/Boston_Neighborhoods.json"
boston = alt.topo_feature(boston_url, feature ='Boston_Neighborhoods')

background =alt.Chart(boston).mark_geoshape(fill='lightgray',stroke='white').encode(tooltip='properties.Name:N').properties(width=500,height=500)
background


# In[13]:


brush =  alt.selection_interval()

neighboorhood_bar = alt.Chart(noise_complaints).mark_bar().encode(
    y="neighborhood",
    x="count()",
    color=alt.Color("reason",legend=None)
).transform_filter(brush
).properties(width=200)

scatterplot = alt.Chart(noise_complaints).mark_point(filled=True
).encode(
    latitude = 'latitude',
    longitude = 'longitude',
    color=alt.condition(brush,"neighborhood",alt.value("lightgray")),
).add_selection(brush)


background =alt.Chart(boston).mark_geoshape(fill='lightgray',stroke='white').encode(tooltip='properties.Name:N').properties(width=500,height=500)
full_chart = background  + scatterplot + tree_points



#scatterplot

full_chart | neighboorhood_bar


# In[ ]:





# In[ ]:




