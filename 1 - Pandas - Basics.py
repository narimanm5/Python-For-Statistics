#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[2]:


pip install pandas


# In[3]:


import pandas as pd


# ## Importing Excel File into Jupyter

# In[4]:


df = pd.read_excel("data.xlsx")
df
# pd.read_csv("name.csv")


# In[16]:


df.shape


# ## Calling Data Frame Columns, Rows and Cells

# In[5]:


df.columns


# In[6]:


df['Age']


# In[17]:


#Multiple columns
df[['Age','Income']]


# #### DataFrame.loc

# In[7]:


df.loc[0]


# In[8]:


df.loc[0,'Age']


# In[26]:


df.loc[[0,1],['Age','Income']]


# #### DataFrame.iloc

# In[9]:


df.iloc[0]


# In[19]:


df.iloc[0,1]


# In[24]:


df.iloc[[0,1]]


# In[25]:


df.iloc[[0,1],[0,1]]


# ## Sorting Data Frames

# In[12]:


df.sort_values('Age',ascending=True)
df
#inplace = True


# ## Set & Reset Index

# In[14]:


df.reset_index(drop=True)
# or
df.reset_index().drop('index',axis=1)
#inplace = True


# In[13]:


df.set_index('Age')
#inplace = True


# ## Group by a Column and build a new Data Frame

# In[31]:


df.groupby('Education').agg({'Income':'sum','Happiness':'mean'})


# ## Filtering a Data Frame

# In[33]:


filt = (df['Education'] == 'Bachelor')
filt


# In[34]:


df.loc[filt]

