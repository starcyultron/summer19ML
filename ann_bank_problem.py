#!/usr/bin/env python
# coding: utf-8

# In[1]:


# loading data via pandas
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


# In[3]:


# loading data 
df=pd.read_csv("bank.csv")


# In[5]:


df.head()


# In[11]:


sb.countplot(df['Gender'])


# In[4]:


df.hist(figsize=(10,15))


# In[14]:


# features and label of data
features=df.iloc[0:,3:13].values


# In[15]:


features


# In[16]:


# bank exit status that is label
label=df.iloc[:,13].values


# In[17]:


label


# In[18]:


# to conveert string data into numeeric we can apply label encoding
from sklearn.preprocessing import LabelEncoder


# In[20]:


countryenc=LabelEncoder() # function calling


# In[21]:


features[0:,1]=countryenc.fit_transform(features[:,1]) # fit country and transform into a number


# In[22]:


features


# In[28]:


# same for gender
features[0:,2]=countryenc.fit_transform(features[0:,2])


# In[29]:


features


# In[30]:


# creating dummy variable using OneHot encoder
from sklearn.preprocessing import OneHotEncoder


# In[31]:


# callingv fon
counthot=OneHotEncoder(categorical_features=[1])


# In[33]:


# transform
features=counthot.fit_transform(features).toarray()


# In[ ]:


# training and testing
# feature scaling 

