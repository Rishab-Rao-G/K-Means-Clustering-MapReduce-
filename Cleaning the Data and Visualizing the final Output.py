#!/usr/bin/env python
# coding: utf-8

# In[157]:


import pandas as pd
import pandas as pd
import os
import sys
import numpy as np
from sklearn import preprocessing
import re


# In[158]:


###########################################CLEANING THE DATA################################################################### 


# In[159]:


# PATH TO THE DATASET
data = pd.read_csv("C:\\Users\\risha\\Desktop\\HD\\Anderlecht_5.csv")


# In[160]:


# SELECTING 200000 ROWS FROM THE DATASET
data = data.head(200000)


# In[162]:


# DROPPING ALL THE NULL VALUES
data = data[data != '0']
data = data.dropna()
data.isnull().values.any()


# In[163]:


# SELECTING THE REQUIRED COLUMNS(AS THE FIRST COLUMN IS A DATE COLUMN)
data = data.iloc[: , 1:]


# In[164]:


# CONVERTING THE DATAFRAME INTO NUMPY FOR SCALING AND NORMALISATION
data_num = data.to_numpy()


# In[165]:


data_num


# In[166]:


# NORMALISING AND SCALING THE DATA
normalised_data = preprocessing.scale(data_num,with_std=True)


# In[167]:


# CONVERTING THE NUMPY ARRAY BACK TO A DATAFRAME
df = pd.DataFrame(normalised_data, columns = ['Column_A','Column_B','Column_C'])


# In[21]:


# SAVING THE DATA AS CSV
df.to_csv("Final_Trans.csv", index = False, header = False)


# In[70]:


###############################################VISUALISATION################################################################### 


# In[317]:





# In[332]:


# CONVERTING CLUSTERS TEXT FILE TO CSV
finalcluster = pd.read_csv (r"C:\\Users\\risha\\Desktop\\Rishab SSP\\Fincluster.txt", header = None)
finalcluster.columns = ['first_column','second_column','third_column']
finalcluster.to_csv (r'C:\\Users\\risha\\Desktop\\Rishab SSP\\finalcluster.csv', index = False, header = False)


# In[333]:


finalcluster


# In[336]:


# Extracting the cluster ID and cleaning the data
finalcluster['id'] = finalcluster['first_column'].map(lambda x: re.findall(r'^.* ', x))
finalcluster['id'] = finalcluster['id'].apply(str)
finalcluster['id'] = finalcluster['id'].map(lambda x: re.sub(r"\[|\]", '', x))
finalcluster['first_column'] = finalcluster['first_column'].map(lambda x: re.sub(r'^.* ', '', x))
finalcluster['first_column'] = finalcluster['first_column'].map(lambda x: re.sub(r'\[', '', x))
finalcluster['third_column'] = finalcluster['third_column'].map(lambda x: re.sub(r'\]|\t', '', x))


# In[339]:


finalcluster


# In[340]:


# SAVING CHANGES MADE TO CSV FILES
finalcluster.to_csv (r'C:\\Users\\risha\\Desktop\\Rishab SSP\\finalcluster.csv', index = False, header = False)


# In[341]:


finalcluster = pd.read_csv (r"C:\\Users\\risha\\Desktop\\Rishab SSP\\finalcluster.csv", header = None)


# In[342]:


finalcluster


# In[348]:


import plotly.graph_objects as go

PLOT = go.Figure()

for C in list(finalcluster[3].unique()):
    
    PLOT.add_trace(go.Scatter3d(x = finalcluster[finalcluster[3] == C][0],
                                y = finalcluster[finalcluster[3] == C][1],
                                z = finalcluster[finalcluster[3] == C][2],
                                mode = 'markers', marker_size = 8, marker_line_width = 1,
                                name = 'Cluster ' + str(C)))
    

PLOT.update_layout(width = 800, height = 800, autosize = True, showlegend = True,
                   scene = dict(xaxis=dict(title = 'Street Segment Index', titlefont_color = 'black'),
                                yaxis=dict(title = 'Traffic Flow', titlefont_color = 'black'),
                                zaxis=dict(title = 'Average speed on street segment', titlefont_color = 'black')),
                   font = dict(family = "Gilroy", color  = 'black', size = 12))

